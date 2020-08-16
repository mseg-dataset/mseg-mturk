#!/usr/bin/python3

import glob
import numpy as np
import pdb
from mseg.utils.csv_utils import read_csv


def count_hours():
	""" """

	bucket_names = []
	bucket_counts = []

	mseg_hours = 0
	for dirpath in [
		'/Users/johnlamb/Downloads/part1_csvs',
		'/Users/johnlamb/Downloads/part2_csvs'
	]:
		csv_fpaths = glob.glob(f'{dirpath}/*.csv')
		print(f'Found {len(csv_fpaths)} csv files.')
		for csv_fpath in csv_fpaths:
			rows = read_csv(csv_fpath, delimiter=',')
			bucket_name = rows[0]['Input.image_url_1']
			batch_sec = 0
			for row in rows:
				sec = int(row['WorkTimeInSeconds'])
				batch_sec += sec

			batch_hours = batch_sec / (60*60)
			mseg_hours += batch_hours
			batch_days = batch_hours / 24
			#print(f'Batch took {batch_days:.2f} days -> {bucket_name}')
			bucket_names += [bucket_name]
			bucket_counts += [batch_days]

	mseg_days = mseg_hours/24
	print(f'MSeg took {mseg_days} days')

	bucket_names = np.array(bucket_names)
	bucket_counts = np.array(bucket_counts)
	sort_idxs = np.argsort(-bucket_counts)
	
	sorted_bucket_names = bucket_names[sort_idxs]
	sorted_bucket_counts = bucket_counts[sort_idxs]

	for b_name, b_days in zip(sorted_bucket_names,sorted_bucket_counts):
		print(f'{b_days:.2f} for {b_name}')


if __name__ == '__main__':
	count_hours()


