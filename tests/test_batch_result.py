#!/usr/bin/python3

import pdb
from pathlib import Path

from mseg_mturk.sentinel_hit import SentinelHIT
from mseg_mturk.batch_result import BatchResult

_ROOT = Path(__file__).resolve().parent


def test_BatchResult_enter_decision():
	"""
		accept the first HIT (100% acc)
		reject the second HIT (50% acc)
		ignore the third HIT (since was previously rejected)
	"""
	unittest_hit = SentinelHIT(
		task_nickname='sentinel_unit_tests_imgs',
		dataset_name='', # irrelevant for test
		train_img_dir=f'{_ROOT}/test_data/sentinel_unit_tests',
		val_img_dir=f'{_ROOT}/test_data/sentinel_unit_tests',
		sentinel_img_dir=f'{_ROOT}/test_data/sentinel_unit_tests',
		train_bucket_name='', # irrelevant for test
		val_bucket_name='', # irrelevant for test
		classnames = [
			'bird','horse','sheep','elephant'
		],
		sentinel_bucket_name='mseg-phase2-ade20k-animal-train',
		sentinels = [
			('ADE_train_00005697_157.png', 'bird'),
			('ADE_train_00013625_191.png', 'elephant')
		],
		train_result_csv='Batch_UnitTest_Sentinels.csv',
		val_result_csv='Batch_UnitTest_Sentinels.csv'
	)

	acceptance_thresh = 100 # acceptance threshold, in percent

	csv_dir = f'{_ROOT}/test_data'
	dump_root = f'{_ROOT}/tmp'

	for split in ['train','val']:

		br = BatchResult(
			split=split,
			hit_info=unittest_hit,
			csv_dir=csv_dir,
			dump_root=dump_root,
			use_prior_labeling=False,
			accuracy_thresh=acceptance_thresh
		)
		
		br.analyze_acc()
		pdb.set_trace()
		assert len(br.duration_acc_tuples) == 2
		assert np.allclose(br.duration_acc_tuples[0][0], (1/60), atol=1e-1) # 1 sec
		assert np.allclose(br.duration_acc_tuples[0][1], 100.0, atol=1e-2)

		assert np.allclose(br.duration_acc_tuples[1][0], 1.0, atol=1e-2) # 1 min
		assert np.allclose(br.duration_acc_tuples[1][1], 50.0, atol=1e-2)
		
		br.enter_decision()
		br.compare_csv_diff()



if __name__ == '__main__':
	test_BatchResult_enter_decision()

