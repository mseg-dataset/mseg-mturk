#!/usr/bin/python3

from mseg_mturk.sentinel_hit import SentinelHIT, RelabeledSentinelHIT


"""
Phase 1 HITS
"""


"""
'100_curtain_img_hit.html'
https://curtain-instruction-figures.s3-us-west-1.amazonaws.com/curtain_instructions.html
"""
ade20k_phase1_curtain = SentinelHIT(
	task_nickname = 'ade20k_SHOWERCURTAIN-OTHERCURTAIN',
	dataset_name = 'ade20k',
	train_img_dir = 'ade20k_CURTAIN_verify_classes_double_train_2019_10_29',
	val_img_dir = 'ade20k_CURTAIN_verify_classes_double_val_2019_10_29',
	sentinel_img_dir = '',
	train_bucket_name = f'ade20k-train-curtain-2019-10-31',
	val_bucket_name = f'ade20k-val-curtain-2019-10-31',
	classnames = ["shower-curtain", "other-curtain"],
	sentinel_bucket_name='',
	sentinels = [],
	train_result_csv = 'Batch_3820594_ade20k_SHOWERCURTAIN-OTHERCURTAIN_2019_10_31_12_32_36_mturk.csv',
	# not 'Batch_3819940_batch_results.csv'
	val_result_csv = 'Batch_3819940_batch_results_ade20k_val_curtain.csv'
)


ade20k_phase1_fenceguardrail = SentinelHIT(
	task_nickname='ade20k_FENCEGUARDRAIL',
	dataset_name='ADE20K',
	train_img_dir='ade20k_CARFENCE-GUARDRAIL_verify_classes_double_train_2019_10_31',
	val_img_dir='ade20k_CARFENCE-GUARDRAIL_verify_classes_double_val_2019_10_31',
	sentinel_img_dir='',
	train_bucket_name='ade20k-fence-guardrail-train',
	val_bucket_name='ade20k-fence-guardrail-va',
	classnames = [
	'fence','guardrail'
	],
	sentinel_bucket_name='',
	sentinels = [],
	train_result_csv = 'Batch_3829975_batch_results_ade20k_FENCEGUARDRAIL_2019_11_09_16_50_24_mturk_100_img_hit_train.csv',
	val_result_csv = 'Batch_3829849_batch_results_ade20k_FENCEGUARDRAIL_2019_11_09_16_50_24_mturk_100_img_hit_val.csv'
)


ade20k_phase1_mountainhillsnow = SentinelHIT(
	task_nickname='ade20k_MOUNTAIN-HILL-SNOW',
	dataset_name='ADE20K',
	train_img_dir='ade20k_MOUNTAIN-HILL-SNOW_verify_classes_double_train_2019_10_31',
	val_img_dir='ade20k_MOUNTAIN-HILL-SNOW_verify_classes_double_val_2019_10_31',
	sentinel_img_dir='',
	train_bucket_name='ade20k-train-mountainhillsnow-2019-11-8',
	val_bucket_name='ade20k-val-mountainhillsnow-2019-11-8',
	classnames = [
		'mountain-hill', 'snow'
	],
	sentinel_bucket_name='',
	sentinels = [],
	train_result_csv = 'Batch_3829400_batch_results_ade20k_MOUNTAIN-HILL-SNOW_2019_11_08_21_40_48_mturk_100_img_hit_train.csv',
	val_result_csv = 'Batch_3829398_batch_results_ade20k_MOUNTAIN-HILL-SNOW_2019_11_08_21_40_48_mturk_100_img_hit_val.csv'
)


ade20k_phase1_personrider = SentinelHIT(
	task_nickname = 'ade20k_PERSONRIDER',
	dataset_name = 'ade20k',
	train_img_dir = 'ade20k_PERSONRIDER_verify_classes_double_train_2019_10_29',
	val_img_dir = 'ade20k_PERSONRIDER_verify_classes_double_val_2019_10_29',
	sentinel_img_dir = '',
	train_bucket_name = f'ade20k-train-personbicycleminibike-2019-10-30',
	val_bucket_name = f'ade20k-val-personbicycleminibike-2019-10-30',
	classnames = ['person', 'rider'],
	sentinel_bucket_name='',
	sentinels = [],
	train_result_csv='Batch_3819441_ade20k_PERSONRIDER_2019_10_30_22_10_58_train.csv',
	# older were 'Batch_3819384_batch_results_1.csv', 'Batch_3819384_batch_results.csv'
	val_result_csv='Batch_3819384_ade20k_PERSONRIDER_2019_10_30_22_10_58_val.csv'
)



cocop_phase1_cabinetmerged = SentinelHIT(
	task_nickname='cocop_CABINETMERGED',
	dataset_name='cocopanoptic',
	train_img_dir = 'cocopanoptic_CABINET-MERGED_verify_classes_double_train_2019_10_30',
	val_img_dir = 'cocopanoptic_CABINET-MERGED_verify_classes_double_val_2019_10_30',
	sentinel_img_dir = '',
	train_bucket_name = f'coco-panoptic-cabinetmerged-train',
	val_bucket_name = f'coco-panoptic-cabinetmerged-val',
	classnames = ['nightstand','dresser','cabinet','desk','counter','unlabel','wardrobe','bookshelf','table'],
	sentinel_bucket_name='',
	sentinels = [],
	train_result_csv = 'Batch_3829985_batch_results_cocopanoptic_CABINETMERGED_2019_11_09_20_36_04_mturk_100_img_hit_train.csv',
	val_result_csv = 'Batch_3829944_batch_results_cocopanoptic_CABINETMERGED_2019_11_09_20_36_04_mturk_100_img_hit_val.csv'
)



cocop_phase1_curtain = SentinelHIT(
	task_nickname = 'cocop_curtain',
	dataset_name = 'cocopanoptic',
	train_img_dir = 'coco_CURTAIN_verify_classes_triple_train_2019_08_14',
	val_img_dir = 'coco_CURTAIN_verify_classes_triple_val_2019_08_14',
	sentinel_img_dir = ''
	train_bucket_name = 'coco-panoptic-train-curtain-08-14',
	val_bucket_name = 'coco-panoptic-val-curtain-08-14',
	classnames = ["shower-curtain", "other-curtain"],
	sentinel_bucket_name='',
	sentinels = [],
	# 'Batch_3737456_batch_results.csv'
	#  'Batch_3737400_batch_results_1.csv'
	#  'Batch_3737400_batch_results.csv'
	train_result_csv = '', # Batch_247932_batch_results.csv ?
	val_result_csv = 'Batch_3737400_batch_results.csv'
)

cocop_phase1_fenceguardrail = SentinelHIT(
	task_nickname='cocop_FENCEGUARDRAIL',
	dataset_name='cocopanoptic',
	train_img_dir='cocopanoptic_FENCE-GUARDRAIL_verify_classes_double_train_2019_10_30',
	val_img_dir='cocopanoptic_FENCE-GUARDRAIL_verify_classes_double_val_2019_10_30',
	sentinel_img_dir='',
	train_bucket_name='coco-panoptic-fence-guardrail-train',
	val_bucket_name='coco-panoptic-fence-guardrail-val',
	classnames = [
		'fence', 'guardrail'
	],
	sentinel_bucket_name='',
	sentinels = [],
	train_result_csv = 'Batch_3829971_batch_results_cocopanoptic_FENCEGUARDRAIL_2019_11_09_16_55_59_mturk_100_img_hit_train.csv',
	val_result_csv = 'Batch_3829854_batch_results_cocopanoptic_FENCEGUARDRAIL_2019_11_09_16_55_59_mturk_100_img_hit_val.csv'
)


"""
these 3 should be riders:
000000400915_1449507.png
000000400915_1841690.png
000000400915_1842977.png
000000402381_2832011.png

# MY LABELED GROUND TRUTH fname = 'Batch_246756_batch_results.csv'
"""
cocop_phase1_personrider_hit = SentinelHIT(
	task_nickname = 'cocop_PERSONRIDER',
	dataset_name = 'cocopanoptic',
	train_img_dir = 'coco_PERSON_verify_classes_triple_train_2019_08_05',
	val_img_dir = 'coco_PERSON_verify_classes_triple_val_2019_08_05',
	sentinel_img_dir = '',
	train_bucket_name = f'coco-panoptic-train-personandmotorcycle-or-personandbike-8-05',
	val_bucket_name = f'coco-panoptic-val-personandmotorcycle-or-personandbicycle-8-05',
	classnames = ['rider', 'person'],
	sentinel_bucket_name='',
	sentinels = [],
	# fname = 'Batch_3727549_batch_results_final.csv'
	#fname = 'Batch_3726947_batch_results_1.csv'
	#fname = 'Batch_3725430_batch_results.csv'
	# fname = 'Batch_247005_batch_results.csv'
	# fname = 'Batch_3724950_batch_results_2019_08_03_1016.csv'
	# fname = 'Batch_3724950_batch_results.csv'
	train_result_csv = '',
	val_result_csv = 'combined_coco_val_rider_Batch_3726947_Batch_3735822_batch_results.csv'
)


cocop_phase1_rugmerged = SentinelHIT(
	task_nickname = 'cocop_rugmerged'
	dataset_name = 'cocopanoptic',
	train_img_dir = 'cocopanoptic_RUG-MERGED_verify_classes_double_train_2019_10_30',
	val_img_dir = 'cocopanoptic_RUG-MERGED_verify_classes_double_val_2019_10_30',
	sentinel_img_dir = ''
	train_bucket_name = f'cocopanoptic-train-rugmerged-2019-11-1',
	val_bucket_name = f'cocopanoptic-val-rugmerged-2019-11-1',
	classnames = '',
	sentinel_bucket_name = '',
	sentinels = [],
	train_result_csv = 'Batch_3829957_batch_results_cocopanoptic_RUGMERGED_2019_11_01_00_13_57_mturk_100_img_hit_train.csv',
	val_result_csv = ''
)



def prep_rugmerged_html_qifeng_template():
	"""
	"""
	task_html_filename = '100_rugmerged_img_hit.html'
	header_filename = 'rug-merged_header.txt'
	image_element_filename = 'rugmerged_image_element.txt'

def prep_mountainhillsnow_html_qifeng_template():
	""" """
	task_html_filename = '100_mountainhillsnow_img_hit.html'
	header_filename = 'mountainhillsnow_header.txt'
	image_element_filename = 'mountainhillsnow_image_element.txt'

def prep_fenceguardrail_html_qifeng_template():
	""" """
	task_html_filename = '100_fenceguardrail_img_hit.html'
	header_filename = 'fenceguardrail_header.txt'
	image_element_filename = 'fenceguardrail_image_element.txt'

def prep_person_rider_html_qifeng_template():
	"""	"""
	task_html_filename = '100_img_hit.html'
	header_filename = 'binary_person_rider_header_qifengtemplate.txt'
	image_element_filename = 'binary_person_rider_image_element_qifengtemplate.txt'
	footer_filename = 'footer_qifengtemplate.txt'




