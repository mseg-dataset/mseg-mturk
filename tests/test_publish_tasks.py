#!/usr/bin/python3

import glob
import numpy as np
import os
from pathlib import Path

from sentinel_hits import SentinelHIT
from publish_tasks import create_write_hit_specs


def test_create_write_hit_specs():
	"""
	"""
	csv_save_fpath = 'test_data/temp_csv_hit_specs.csv'
	hit_info = 	SentinelHIT(
		task_nickname='unit_test_hit',
		dataset_name='UnitTestDataset',
		train_img_dir =	'unit_test_hit',
		sentinel_img_dir='unit_test_hit_sentinelsonly',
		val_img_dir = '',
		train_bucket_name='mseg-phase2-unit-test-hit',
		val_bucket_name=  'mseg-phase2-unit-test-hit',
		classnames = [
			'desk', 'table', 'counter'
		],
		sentinel_bucket_name='mseg-phase2-unit-test-hit',
		sentinels = [
			('sentinel_counter1.png', 'counter'),
			('sentinel_desk1.png', 'desk'),
			('sentinel_table1.png', 'table')
		],
		train_result_csv='', val_result_csv=''
	)

	fpaths = glob.glob(f'temp_files/{hit_info.train_img_dir}/*.png')
	# sort images to make sure they are in order; less cognitive load
	fpaths.sort()
	split = 'train'
	sentinel_percentage = 15
	create_write_hit_specs(split, csv_save_fpath, hit_info, fpaths, sentinel_percentage)
	rows = read_csv(csv_save_fpath)

	# Verify everything is as expected.
	s_fnames = list(zip(*hit_info.sentinels))[0] # sentinel fnames

	for i, row in enumerate(rows):
		for j, (col_name,url) in enumerate(row.items()):
			print(col_name)
			assert col_name == f'image_url_{j}'
			assert f'https://{hit_info.train_bucket_name}' in url
			assert '.png' in url
		assert len(row) == NUM_IMGS_PER_HIT
		is_sentinel = [True if Path(url).name in s_fnames else False for (k,url) in row.items() ]
		expected_num_sents = int(sentinel_percentage * NUM_IMGS_PER_HIT / 100)
		if i == len(rows) - 1: # last row
			expected_num_sents = NUM_IMGS_PER_HIT - (len(fpaths) % 85) # remainder may be >15
		assert np.array(is_sentinel).sum() == expected_num_sents

	os.remove(csv_save_fpath)




def test_accumulate_hit_urls():
	""" """
	hit_info = SentinelHIT(
		task_nickname='unit_test_hit',
		dataset_name='UnitTestDataset',
		train_img_dir =	'unit_test_hit',
		sentinel_img_dir='unit_test_hit',
		val_img_dir = 'unit_test_hit',
		train_bucket_name='mseg-phase2-unit-test-train',
		val_bucket_name=  'mseg-phase2-unit-test-val',
		classnames = [
			'desk', 'table', 'counter'
		],
		sentinel_bucket_name='mseg-phase2-unit_test_hit',
		sentinels = [], train_result_csv='', val_result_csv=''
	)

	hit_fpaths = glob.glob(f'temp_files/{hit_info.train_img_dir}/*.png')
	# sort images to make sure they are in order; less cognitive load
	hit_fpaths.sort()

	hit_urls = accumulate_hit_urls(hit_info, hit_fpaths, hit_info.train_bucket_name)
	# in alphabetical order
	gt_hit_urls = [
		'https://mseg-phase2-unit-test-train.s3-us-west-1.amazonaws.com/counter2.png',
		'https://mseg-phase2-unit-test-train.s3-us-west-1.amazonaws.com/desk4.png',
		'https://mseg-phase2-unit-test-train.s3-us-west-1.amazonaws.com/desk5.png',
		'https://mseg-phase2-unit-test-train.s3-us-west-1.amazonaws.com/table1.png',
		'https://mseg-phase2-unit-test-train.s3-us-west-1.amazonaws.com/table2.png'
	]
	assert hit_urls == gt_hit_urls



def test_accumulate_hit_urls_from_sentinels():
	"""
	Ensure that given a specification of a SentinelHIT, we can construct
	a list of sentinel URLS that meet the specification (correct cardinality).
	We specify the random seeds to ensure the correct order.
	"""
	hit_info = SentinelHIT(
		task_nickname='unit_test_hit',
		dataset_name='UnitTestDataset',
		train_img_dir =	'unit_test_hit',
		sentinel_img_dir='unit_test_hit',
		val_img_dir = 'unit_test_hit',
		train_bucket_name='mseg-phase2-unit-test-hit',
		val_bucket_name=  'mseg-phase2-unit-test-hit',
		classnames = [
			'desk', 'table', 'counter'
		],
		sentinel_bucket_name='mseg-phase2-unit_test_hit',
		sentinels = [
			('table1.png', 'table'),
			('table2.png', 'table'),
			('counter2.png', 'counter'),
			('desk4.png', 'desk'),
			('desk5.png', 'desk')
		],
		train_result_csv='', val_result_csv=''
	)
	random.seed(0)
	np.random.seed(0)
	sentinel_urls = accumulate_hit_urls_from_sentinels(hit_info, num_req_sents=6)

	gt_s_url_list = [
		'https://mseg-phase2-unit_test_hit.s3-us-west-1.amazonaws.com/desk5.png',
		'https://mseg-phase2-unit_test_hit.s3-us-west-1.amazonaws.com/table1.png',
		'https://mseg-phase2-unit_test_hit.s3-us-west-1.amazonaws.com/desk4.png',
		'https://mseg-phase2-unit_test_hit.s3-us-west-1.amazonaws.com/desk4.png',
		'https://mseg-phase2-unit_test_hit.s3-us-west-1.amazonaws.com/desk4.png',
		'https://mseg-phase2-unit_test_hit.s3-us-west-1.amazonaws.com/table2.png'
	]
	assert gt_s_url_list == sentinel_urls


if __name__ == '__main__':
	""" """
	test_accumulate_hit_urls()
	#test_accumulate_hit_urls_from_sentinels()
	#test_create_write_hit_specs()


