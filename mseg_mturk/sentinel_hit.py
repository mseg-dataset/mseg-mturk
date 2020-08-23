#!/usr/bin/python3

from typing import List, NamedTuple, Tuple

from mseg.label_preparation.relabeled_data_containers import DatasetClassUpdateRecord


class SentinelHIT(NamedTuple):
	""" """
	task_nickname: str
	dataset_name: str
	classnames: List[str]
	train_img_dir: str
	val_img_dir: str
	train_bucket_name: str
	val_bucket_name: str
	sentinels: List[Tuple[str,str]] # represents (filename, correct category)
	sentinel_bucket_name: Str
	sentinel_img_dir: str
	train_result_csv: str
	val_result_csv: str


# TODO: could inherit from class above for simplicity
# Sending through the pipeline for a second or third time.
class RelabeledSentinelHIT(NamedTuple):
	""" """
	task_nickname: str
	dataset_name: str
	train_img_dir: str
	val_img_dir: str
	sentinel_img_dir: str
	train_bucket_name: str
	val_bucket_name: str
	classnames: List[str]
	sentinel_bucket_name: str
	sentinels: List[Tuple[str,str]] # represents (filename, correct category)
	train_prior_record: DatasetClassUpdateRecord
	val_prior_record: DatasetClassUpdateRecord
	train_result_csv: str
	val_result_csv: str
