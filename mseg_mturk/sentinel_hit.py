#!/usr/bin/python3

import collections
from mseg.label_preparation.relabeled_data_containers import DatasetClassUpdateRecord


SentinelHIT = collections.namedtuple(
	typename='SentinelHIT',
	field_names='task_nickname dataset_name classnames train_img_dir val_img_dir' + \
		' train_bucket_name val_bucket_name sentinels sentinel_bucket_name' + \
		' sentinel_img_dir train_result_csv val_result_csv'
)


# Sending through the pipeline for the second time.
RelabeledSentinelHIT = collections.namedtuple(
	typename='RelabeledSentinelHIT',
	field_names=
		'task_nickname' + \
		' dataset_name' + \
		' train_img_dir' + \
		' val_img_dir' + \
		' sentinel_img_dir' + \
		' train_bucket_name' + \
		' val_bucket_name' + \
		' classnames' + \
		' sentinel_bucket_name' + \
		' sentinels' + \
		' train_prior_record' + \
		' val_prior_record' + \
		' train_result_csv' + \
		' val_result_csv'
)
