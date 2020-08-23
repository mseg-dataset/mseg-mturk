#!/usr/bin/python3

from collections import defaultdict
import csv
from datetime import datetime
from pathlib import Path
import pdb
from shutil import copyfile
from typing import Any, List, Mapping, Tuple

import matplotlib.pyplot as plt
import numpy as np

from mseg.utils.csv_utils import read_csv
from mseg.utils.txt_utils import write_txt_lines
from mseg.utils.dir_utils import check_mkdir

from mseg_mturk.batch_result import BatchResult
from mseg_mturk.publish_tasks import filter_to_prev_labeled
from mseg_mturk.hit_utils import (
	most_frequent,
	read_txtfile_as_np,
	strip_forward_slash
)
from mseg_mturk.sentinel_hit import SentinelHIT
from mseg_mturk.hit_config.completed_sentinel_hit_instances import (
	COCOP_PersonNonRider_HIT,
	COCOP_MotorcyclistBicyclist_HIT,
	ADE20K_PersonNonRider_HIT,
	ADE20K_motorcyclist_bicyclist_hit,
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


MAX_NUM_WORKER_VOTES = 10

	
def render_each_worker_annotations(
	dir_savename: str,
	batch_csv_fname: str,
	img_dirpath: str,
	folder_per_hit: bool = True
):
	"""
		In train set, had to discard:
			worker_id = 'A2R2YZTSME1K3F', hit_id = '3SSN80MU8CPEVNHI370TAPO2EATKXE'

	"""
	csv_dirpath = '/Users/johnlamb/Downloads'
	csv_fpath = f'{csv_dirpath}/{batch_csv_fname}'
	dump_root = 'temp_files'

	with open(csv_fpath, 'r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		for row in csv_reader:
			worker_id = row['WorkerId']

			hit_id = row['HITId']

			for i in range(100):
				for key in row.keys():
					if key == f'Answer.choice_{i}':
						category = row[key]
						image_url = row[f'Input.image_url_{i}']
						split = 'val' if 'val' in image_url else 'train'
						fname = Path(image_url).name
						dump_dirname = category

						split_img_dirpath = img_dirpath.replace('SPLIT', f'{split}')
						src = f'temp_files/{split_img_dirpath}/{fname}'
						new_dirpath = f'{dump_root}/{dir_savename}/{worker_id}/{dump_dirname}'
						if folder_per_hit:
							new_dirpath += f'/{hit_id}'
						dst = f'{new_dirpath}/{fname}'
						check_mkdir(new_dirpath)
						copyfile(src, dst)


def plot_acc_histogram(duration_acc_tuples: List[Tuple[float,float]]) -> None:
	"""
		Args:
		-	duration_acc_tuples: List of 2-tuples, each 2-tuple consisting of
			(duration in minutes, accuracy percent)

		Returns:
		-	None
	"""
	accs = list(zip(*duration_acc_tuples))[1]
	plt.hist(accs)
	plt.xlabel('Worker Accuracy (%)')
	plt.ylabel('Counts')
	plt.title('Histogram of Worker Accuracy (%)')
	plt.show()
	plt.close('all')

	plot_acc_vs_duration(duration_acc_tuples)


def plot_acc_vs_duration(duration_acc_tuples) -> None:
	""" Form a scatter plot to show correlation between HIT duration
		and HIT accuracy.

		Args:
		-	duration_acc_tuples: List of 2-tuples, each 2-tuple consisting of
			(duration in minutes, accuracy percent)

		Returns:
		-	None
	"""
	duration_m, acc = zip(*duration_acc_tuples)
	plt.scatter(duration_m, acc, 10, marker='.', color='r')
	plt.xlabel('HIT Duration (minutes)')
	plt.ylabel('Accuracy (%)')
	plt.title('Accuracy vs. HIT Duration (minutes)')
	plt.show()


def get_duration_from_csv_row(row):
	"""
	AWS uses 'Sat Feb 01 22:37:06 PST 2020'
	Library crashes w/ leap years (e.g. 29 days in Feb.)

		Args:

		Returns:
		-	duration_m: float representing duration in minutes
	"""
	# string format time
	# strftime = '%a %b %d %X %Z %Y'
	# strftime = '%a %b %d %H:%M:%S %Z %Y'
	strftime = '%a %b %d %H:%M:%S'

	try:
		# string parse time 'Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p'
		datetime_obj_accept = datetime.strptime(row.AcceptTime[:-9], strftime)
		datetime_obj_submit = datetime.strptime(row.SubmitTime[:-9], strftime)

		duration_s = (datetime_obj_submit - datetime_obj_accept).total_seconds()
		duration_m = duration_s / 60
		np.absolute(duration_m) # otherwise is negative time
	except:
		return 0


def test_get_duration_from_csv_row() -> None:
	"""
	"""
	row = {}
	row['AcceptTime'] = 'Sat Feb 01 22:37:06 PST 2020'
	row['SubmitTime'] = 'Sat Feb 01 23:37:06 PST 2020'
	duration_m = get_duration_from_csv_row(row)
	gt_duration_m = 60
	EPSILON = 1e-2
	assert (duration_m - gt_duration_m) < EPSILON


def analyze_sentinel_acc_per_hit(hit_info: SentinelHIT, csv_dir: str, is_relabeled: bool):
	"""
		Args:
		-	hit_info
		-	csv_dir

		Returns:
		-	None
	"""
	dump_root = 'temp_files'
	for split in ['train']: #'val']:#  ]:#, 
		br = BatchResult(split, hit_info, csv_dir, dump_root, is_relabeled)

		br.analyze_acc()
		br.enter_decision()
		# since analyze_acc will modify the contents of each row,
		# worker agreement must come before all else,
		br.analyze_multinomial_worker_agreement()


if __name__ == '__main__':
	"""
	Completed:
		(bdd_rider_hit, False)
		(COCOP_MotorcyclistBicyclist_HIT, True)
		(COCOP_PersonNonRider_HIT,True)
		(ADE20K_PersonNonRider_HIT,True)
		(ADE20K_motorcyclist_bicyclist_hit, True)
		(bdd_person_hit, False)
		(cityscapes_rider_hit, False)
		(ADE20K_chest_of_drawers_hit, False)
		(ADE20K_animal_hit, False)
		(ADE20K_table_hit,False)
		(cocop_diningtable_hit, False)
		(coco_chair_hit, False)
		(ADE20K_glass_hit,False)
		(coco_counter_hit, False)
		(ADE20K_food_hit, False)
		(coco_light_hit, False)
		(idd_rider_hit, False)
		(COCO_platform_hit, False)
		(COCO_bridge_hit, False)
		(ADE20k_plaything_hit,False)
		(cocop_table_merged_hit,False)
		(sunrgbd_counter_hit,False)
		(sunrgbd_chair_hit,False)
		(sunrgbd_lamp_hit,False)
	"""
	""" """
	# test_WorkerHITResult()
	# test_get_duration_from_csv_row()
	# test_most_frequent()
	# test_BatchResult_enter_decision()

	# test_read_txtfile_as_np()

	csv_dir = '/Users/johnlamb/Downloads'
	hits = [
		#(COCO_building_hit, False)
		#(COCO_house_hit, False)
		#(coco_waterother_hit, False)
		(cocop_keyboard_hit, False)
		#(COCOP_tent_hit, False)
		#(MapillaryAcademic_water_hit, False)
	]

	for (hit_info,is_relabeled) in hits:

		analyze_sentinel_acc_per_hit(hit_info, csv_dir, is_relabeled)
	

