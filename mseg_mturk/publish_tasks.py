#!/usr/bin/python3

import csv
import glob
import math
import os
from pathlib import Path
import pdb
import random
from typing import Any, Dict, List, Mapping, Union

import imageio
import matplotlib.pyplot as plt
import numpy as np

from mseg.utils.csv_utils import read_csv, write_csv
from mseg.utils.txt_utils import generate_all_img_label_pair_fpaths

from mseg_mturk.hit_utils import generate_datetime_string, read_txt_file
from mseg_mturk.sentinel_hit import SentinelHIT
from mseg_mturk.hit_config.completed_sentinel_hit_instances import (
	COCOP_PersonNonRider_HIT,
	COCOP_MotorcyclistBicyclist_HIT,
	ADE20K_motorcyclist_bicyclist_hit,
	ADE20K_PersonNonRider_HIT,
	bdd_person_hit,
	bdd_rider_hit,
	cityscapes_rider_hit,
	ADE20K_chest_of_drawers_hit,
	ADE20K_animal_hit,
	ADE20K_table_hit,
	cocop_diningtable_hit,
	coco_chair_hit,
	ADE20K_glass_hit,
	coco_counter_hit,
	ADE20K_food_hit,
	coco_light_hit,
	idd_rider_hit,
	cocop_table_merged_hit,
	sunrgbd_counter_hit,
	sunrgbd_chair_hit,
	sunrgbd_lamp_hit,
	COCO_platform_hit,
	COCO_bridge_hit,
	ADE20k_plaything_hit,
	coco_waterother_hit,
	cocop_keyboard_hit,
	COCOP_tent_hit,
	MapillaryAcademic_water_hit
)


NUM_IMGS_PER_HIT = 100
REMIND_EVERY_N_IMGS = 20 # Remind worker to look at instructions every 20 lines.


"""
No need to label 'table' vs. 'nightstand' in ADE20K since we are not using the 'table'
class anyways. This was because of the VOC 'diningtable' nonsense...

do not need to include the segmentid because when there is a nighstand, there
is generally no other table present.
"""


def is_last_line(line):
	""" """
	return '</crowd-image-classifier>' in line


def write_qifeng_template_html(
	task_html_filename: str, 
	header_filename: str, 
	image_element_filename: str, 
	footer_filename: str,
	instructions_url: str
):
	""" Use Qifeng's Bootstrap HTML template.

		Args:
		-	task_html_filename: str, 
		-	header_filename: str, 
		-	image_element_filename: str, 
		-	footer_filename: str,
		-	instructions_url: str

		Returns:
		-	None
	"""
	header_lines = read_txt_file(f'mturk/{header_filename}')
	instr_reminder_lines = read_txt_file(f'mturk/instructions_reminder.html')

	key = 'INSTRUCTIONS_URL'
	with open(f'mturk/hit_populated_html_files/{task_html_filename}', 'w') as f:

		for header_line in header_lines:
			if key in header_line:
				header_line = header_line.replace(key, instructions_url)
			f.write(header_line) 
		f.write('\n')

		for i in range(NUM_IMGS_PER_HIT):

			if (i % REMIND_EVERY_N_IMGS == 0) and (i > 0):
				# dump a reminder every so often
				for r_line in instr_reminder_lines:
					if key in r_line:
						r_line = r_line.replace(key, instructions_url)
					f.write(r_line) 
				f.write('\n')

			lines = read_txt_file(image_element_filename)
			for line in lines:
				if 'image_url' in line:
					line = line.replace('image_url', f'image_url_{i}')

				if 'choice_i' in line:
					line = line.replace('choice_i', f'choice_{i}')

				f.write(line)
				if is_last_line(line):
					f.write('\n')

		lines = read_txt_file(f'mturk/{footer_filename}')
		f.writelines(lines)


def prepare_instructions(hit_info: SentinelHIT):
	"""
		Args:
		-	hit_info

		Returns:
		-	instructions_url
	"""
	lines = [
		'<?xml version="1.0" encoding="utf-8"?>',
		'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"',
		' "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">',
		'<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">',
		' <head>',
		' <title>MTURK Instructions</title>',
		' </head>',
		' <body>',
		'      <h2>Our goal is to classify the highlighted-in-pink <i>mask</i> (blob of pixels). </h2>',
		'      You will see 2 versions of the same image, arranged in a row. From left to right, they will be the original image,',
		'		then the blob of pixels highlighted in pink in the image.',
		'      Sometimes the pink pixels will be hard to find. <b> You will sometimes need to zoom in to see clearly. </b>',
		'      <h2> We will show a few examples of each category below: </h2>'
	]

	bucket_url = 'https://mseg-phase2-instruction-figs.s3-us-west-1.amazonaws.com'

	csv_fpath = 'mseg_instructions_db.tsv'
	with open(csv_fpath, 'r') as csvfile:
		reader = csv.DictReader(csvfile, delimiter='\t')
		for row in reader:
			classname = row['universal_classname']
			defn = row['defn']
			if classname in hit_info.classnames:
			
				lines += [f'      <h3><font style="color:red"> {classname}</font>: {defn}</h3>','      <div>']

				for i in range(1,4):
					key = f'img{i}_filename'
					if row[key] != '':
						fname = row[key]
						lines += [
							# f'      <p><b> Below: {classname}. </b></p>',
							f'      <img src="{bucket_url}/{fname}" height="200px">',
						]
				lines += ['      </div>']
	lines += [
		' </body>',
		'</html>'
	]
	save_fname = f'{hit_info.task_nickname}_instructions.html'
	save_fpath = f'mturk/instruction_files/{save_fname}'
	f = open(save_fpath, 'w')
	for line in lines:
		f.write(line + '\n')
	f.close()

	instructions_url = bucket_url + '/' + save_fname
	return instructions_url


def prepare_image_element_html(hit_info, include_unlabel_choice=True):
	"""
	"""
	image_element_fpath = f'mturk/image_elements/{hit_info.task_nickname}_image_element'
	f = open(image_element_fpath, 'w')
	start_lines = [
		'<div class="row">',
		'	<div class="col-xs-12 col-sm-6 col-md-6">',
		'		<div class="form-group">',
		'			<label class="btn btn-default img-btn">',
		'				<span class="clearfix img-label">'
	]
	for start_line in start_lines:
		f.write(start_line + '\n')
	
	for classname in hit_info.classnames + ['None_of_these']:
		class_lines = [
			f'<input autocomplete="off" class="pull-left img-options" id="itemA" name="choice_i" required="" type="radio" value="{classname}" />',
			'<span class="pull-left">',
			f'	<strong>{classname.capitalize()} |</strong>',
			'</span>'
		]
		for class_line in class_lines:
			f.write( '\t' + '\t' + '\t' + '\t' + class_line + '\n')

	end_lines = [
		'				</span> ',
		'				<span class="img-wrap"> ',
		'					<img alt="Image A" src="${image_url}"  style="width: 1100px; " /> ',
		'				</span> ',
		'			</label>',
		'		</div>',
		'	</div>',
		'</div>'
	]
	for end_line in end_lines:
		f.write(end_line + '\n')
	f.close()
	return image_element_fpath


def prepare_hit_html(hit_info: SentinelHIT, instructions_url: str) -> None:
	"""
		Args:
		-	hit_info
		-	instructions_url

		Returns:
		-	None
	"""
	task_html_filename = f'100_{hit_info.task_nickname}_img_hit.html'
	header_filename = 'MSeg_hit_header.txt'
	footer_filename = 'footer_qifengtemplate.txt'
	image_element_fpath = prepare_image_element_html(hit_info)

	write_qifeng_template_html(
		task_html_filename, 
		header_filename, 
		image_element_fpath, 
		footer_filename,
		instructions_url)


def filter_to_prev_labeled(hit_info, split, fpaths):
	""" Relabel only previously labeled images.

		Args:
		-	hit_info
		-	split
		-	fpaths

		Returns:
		-	pruned_fpaths
	"""
	print('Use prior relabeling!')
	prior_img_list = hit_info.train_prior_record.img_list if split == 'train' else hit_info.val_prior_record.img_list
	#append the new ones here only if in prior list
	pruned_fpaths = [fpath for fpath in fpaths if Path(fpath).name in prior_img_list]
	return pruned_fpaths


def write_hit_w_sentinels(hit_info, use_prior_relabeling: bool) -> None:
	"""
	# 10 of 100 entries should be sentinels
	load a list of fnames with ground truth labels

		Write out CSV for Human Intelligence Tasks (HIT).
		We use 100-image HITs. We will pay for each HIT.

		Args:
		-	task_nickname
		-	train_img_dir
		-	val_img_dir
		-	train_bucket_name
		-	val_bucket_name

		Returns:
		-	None
	"""
	splits = ['train','val']
	split_dirnames = [hit_info.train_img_dir,hit_info.val_img_dir]
	creation_datetime = generate_datetime_string()
	for split, split_dirname in zip(splits, split_dirnames):
		fpaths = glob.glob(f'temp_files/{split_dirname}/*.png')
		if len(fpaths) == 0:
			# look for jpeg instead
			fpaths = glob.glob(f'temp_files/{split_dirname}/*.jpg')
		# sort images to make sure they are in order; less cognitive load
		fpaths.sort()

		if use_prior_relabeling:
			fpaths = filter_to_prev_labeled(hit_info, split, fpaths)

		csv_save_fname = f'{hit_info.dataset_name}_{hit_info.task_nickname}_{creation_datetime}_mturk_100_img_hit_{split}_AdjustPrices.csv'
		csv_save_fpath = f'mturk/csvs/{csv_save_fname}'
		create_write_hit_specs(split, csv_save_fpath, hit_info, fpaths, sentinel_percentage=10)


		verify_num_unique_urls(split, csv_save_fpath, hit_info, fpaths)

	return


def verify_num_unique_urls(
		split: str, 
		csv_save_fpath: str, 
		hit_info: SentinelHIT, 
		split_fpaths: List[str]
	) -> None:
	"""
		Args:
		-	split: str, 
		-	csv_save_fpath: str, 
		-	hit_info: SentinelHIT, 
		-	split_fpaths: List[str]

		Returns:
		-	None
	"""
	split_fnames = [ Path(fpath).name for fpath in split_fpaths]
	rows = read_csv(csv_save_fpath)
	
	unique_found_fnames = set()
	for row in rows:
		for k in row.keys():
			url = row[k]
			fname = Path(url).name
			unique_found_fnames.add(fname)

	sent_fnames = list(zip(*hit_info.sentinels))[0] # sentinel fnames
	found_plus_sent = unique_found_fnames.union(set(sent_fnames))
	split_plus_sent = set(split_fnames).union(set(sent_fnames))
	assert found_plus_sent == split_plus_sent
	print('All expected URLS found in published csv. Success...')


def create_write_hit_specs(
	split: str,
	csv_save_fpath: str,
	hit_info: SentinelHIT, 
	fpaths: List[str], 
	sentinel_percentage: int = 10
) -> None:
	""" We generally set NUM_IMGS_PER_HIT to 100, and a 10% sentinel pctg., such
		that 90% of the HIT is legitimate work.

		Args:
		-	split: str,
		-	csv_save_fpath: str,
		-	hit_info: SentinelHIT, 
		-	fpaths: List[str], 
		-	sentinel_percentage: int = 10

		Returns:
		-	None
	"""
	if split == 'val':
		split_bucket_name = hit_info.val_bucket_name
	elif split == 'train':
		split_bucket_name = hit_info.train_bucket_name

	row_keys = [ f'image_url_{i}' for i in range(NUM_IMGS_PER_HIT) ]
	num_nonsentinels = NUM_IMGS_PER_HIT - int(sentinel_percentage * NUM_IMGS_PER_HIT / 100)
	csv_row_dicts = []

	hit_start_idxs = range(0,len(fpaths), num_nonsentinels)
	# count off 90 at a time 
	for batch_idx, start_idx in enumerate(hit_start_idxs):

		# choose up to 90 imgs, set ending index to be one greater than last valid idx
		end_idx = min(start_idx + num_nonsentinels, len(fpaths)) 
		print(f'Forming Hit {batch_idx} of {split}: from {start_idx}->{end_idx}')
		hit_urls = accumulate_hit_urls(
			hit_info, 
			hit_fpaths=fpaths[start_idx:end_idx], 
			split_bucket_name=split_bucket_name
		)

		# at least 10% are Sentinels/Gold Standard
		# choose 10 random sentinels (or more to pad batch to 100)
		num_req_sents = NUM_IMGS_PER_HIT - len(hit_urls) # number of requested sentinels
		print(f'\t Need to add sentinels. Current len: {len(hit_urls)}')
		hit_urls.extend(accumulate_hit_urls_from_sentinels(hit_info, num_req_sents))
		print(f'\t Added sentinels. Current len: {len(hit_urls)}')
		# random shuffle random choice
		#
		if batch_idx == len(hit_start_idxs) - 1:
			# we're on the last one
			# may have duplicates from sentinels. dont want them adjacent to one another.
			random.shuffle(hit_urls)
		else:
			# wont have duplicates. sorting is fine then.
			hit_urls.sort()
		csv_row_dict = { k:url for k,url in zip(row_keys, hit_urls)} 
		csv_row_dicts += [csv_row_dict]

	write_csv(csv_save_fpath, dict_list=csv_row_dicts)

	written_rows = read_csv(csv_save_fpath)
	num_hits = len(written_rows)
	assert num_hits == math.ceil( len(fpaths) / num_nonsentinels )


def accumulate_hit_urls(hit_info: SentinelHIT, hit_fpaths: List[str], split_bucket_name: str):
	"""
		Args:
		-	hit_info:
		-	hit_fpaths:

		Returns:
		-	hit_urls:
	"""
	hit_fnames = [Path(hit_fpath).name for hit_fpath in hit_fpaths]
	bucket_name = split_bucket_name

	bucket_url = f'https://{bucket_name}.s3-us-west-1.amazonaws.com'
	hit_urls = [f'{bucket_url}/{hit_fname}' for hit_fname in hit_fnames]
	return hit_urls


def accumulate_hit_urls_from_sentinels(hit_info: SentinelHIT, num_req_sents: int):
	"""
		Args:
		-	hit_info:
		-	num_req_sents: number of requested sentinels

		Returns:
		-	sentinel_urls:
	"""
	num_sentinel_choices = len(hit_info.sentinels)
	sent_indices = np.random.choice(a=num_sentinel_choices, size=num_req_sents)
	sentinel_tuples = [hit_info.sentinels[sent_idx] for sent_idx in sent_indices]
	sentinel_fnames = [st[0] for st in sentinel_tuples]
	bucket_name = hit_info.sentinel_bucket_name

	bucket_url = f'https://{bucket_name}.s3-us-west-1.amazonaws.com'
	sentinel_urls = [f'{bucket_url}/{s_fname}' for s_fname in sentinel_fnames]
	return sentinel_urls


def publish_hits():
	"""
		(ADE20K_animal_hit, False) # not previously relabeled
		(ADE20K_glass_hit, False) # not previously relabeled
		(COCOP_MotorcyclistBicyclist_HIT, True) # was previously relabeled
		(COCOP_PersonNonRider_HIT,True) # was previously relabeled

		Unenforceable:
			(COCO_building_hit, False)
			(COCO_house_hit, False)
	"""
	hits = [
		(coco_counter_hit,False)
		(ADE20K_PersonNonRider_HIT, True)
		(ADE20K_PersonNonRider_HIT, True)
		(ADE20K_motorcyclist_bicyclist_hit, True)
		(cocop_diningtable_hit, False)
		(coco_chair_hit, False)
		(ADE20K_food_hit, False)
		(cityscapes_rider_hit, False)
		(ADE20K_chest_of_drawers_hit, False)
		(bdd_rider_hit, False)
		(bdd_person_hit, False)
		(ADE20K_table_hit, False)
		(coco_light_hit, False)
		(cocop_table_merged_hit, False)
		(idd_rider_hit, False)
		(sunrgbd_counter_hit, False)
		(sunrgbd_chair_hit, False),
		(sunrgbd_lamp_hit, False)
		(coco_waterother_hit, False)
		(ADE20k_plaything_hit, False)
		(COCO_platform_hit,False)
		(COCO_bridge_hit, False)
		(cocop_keyboard_hit, False)
		(COCOP_tent_hit, False)
		(MapillaryAcademic_water_hit,False)
	]

	for (hit_info, is_relabeled) in hits:
		write_hit_w_sentinels(hit_info, is_relabeled)
		instructions_url = prepare_instructions(hit_info)
		prepare_hit_html(hit_info, instructions_url)


if __name__ == '__main__':
	""" """
	publish_hits()


