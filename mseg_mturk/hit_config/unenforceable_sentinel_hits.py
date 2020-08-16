#!/usr/bin/python3

from mseg_mturk.sentinel_hit import SentinelHIT, RelabeledSentinelHIT

"""
COCO Panoptic "roof" unnecesssary because merged house, building, and roof
COCO Panoptic "wine glass" is already accurate
COCO Panoptic "cup" is already accurate
# no need for coco laptop, can keep as it, fairly good.
"""


COCO_building_hit = SentinelHIT(
	task_nickname='cocop_building',
	dataset_name='cocop',
	train_img_dir = 'cocopanoptic_mseg_phase2_building-other-merged_train_2020_03_02',
	sentinel_img_dir ='cocopanoptic_mseg_phase2_building-other-merged_train_2020_03_02',
	val_img_dir = 'cocopanoptic_mseg_phase2_building-other-merged_val_2020_03_02',
	train_bucket_name = 'mseg-phase3-cocop-building-other-merged',
	val_bucket_name = 'mseg-phase3-cocop-building-other-merged',
	sentinel_bucket_name = 'mseg-phase3-cocop-building-other-merged',
	classnames = [
		'house',
		'building_other',
		'skyscraper',
		'booth',
		'tower',
		'grandstand',
		'bridge',
		'seat'
	],
	sentinels = [
		('000000220050_7108454.png', 'grandstand'),
		('000000213312_7102300.png', 'grandstand'),
		('000000240403_4606015.png', 'grandstand'),
		('000000244082_4871251.png', 'grandstand'),
		('000000237372_6972252.png', 'building_other'),
		('000000305959_6977150.png', 'building_other'),
		('000000315202_6780799.png', 'building_other'),
		('000000420634_6909813.png', 'building_other'),
		('000000452685_8424598.png', 'building_other'),
		('000000466942_7499890.png', 'building_other'),
		('000000218649_8952746.png', 'building_other'),
		('000000256364_7432809.png', 'building_other')
	],
	train_result_csv='',
	#val_result_csv='Batch_3966667_cocop_building_2020_03_23_19_20_40_mturk_100_img_hit_val_AdjustPrices.csv'
	#val_result_csv = 'Batch_3966667_cocop_building_2020_03_23_19_20_40_mturk_100_img_hit_val_AdjustPrices_v2.csv'
	#val_result_csv = 'Batch_3966667_cocop_building_2020_03_23_19_20_40_mturk_100_img_hit_val_AdjustPrices_v3.csv'
	#val_result_csv = 'Batch_3966667_cocop_building_2020_03_23_19_20_40_mturk_100_img_hit_val_AdjustPrices_v100.csv'
	val_result_csv = 'Batch_3966667_cocop_building_2020_03_23_19_20_40_mturk_100_img_hit_val_AdjustPrices_v1000.csv'
)




COCO_house_hit = SentinelHIT(
	task_nickname='cocop_house',
	dataset_name='cocop',
	train_img_dir = 'cocopanoptic_mseg_phase2_house_train_2020_03_02',
	sentinel_img_dir ='cocopanoptic_mseg_phase2_house_train_2020_03_02',
	val_img_dir = 'cocopanoptic_mseg_phase2_house_val_2020_03_02',
	train_bucket_name = 'mseg-phase3-cocop-house-bucket',
	val_bucket_name = 'mseg-phase3-cocop-house-bucket',
	sentinel_bucket_name = 'mseg-phase3-cocop-house-bucket',
	classnames = [
		'house',
		'building_other',
		'skyscraper',
		'booth',
		'tower',
		'grandstand',
		'wall'
	],
	sentinels = [
		('000000058465_7368300.png', 'house'),
		('000000080147_9079683.png', 'house'),
		('000000179405_9605778.png', 'house'),
		#('000000446232_5260098.png', 'house'),
		('000000488146_9673887.png', 'house'),
		('000000495374_8620937.png', 'house'),
		('000000477243_8814724.png', 'house'),
		('000000155806_4672080.png', 'house'),
		('000000126263_7039852.png', 'house'),
		('000000114686_8885397.png', 'house'),
		('000000103549_11381170.png', 'building_other')
	],
	train_result_csv='Batch_3966841_cocop_house_2020_03_23_20_05_31_mturk_100_img_hit_train_AdjustPrices_v5.csv',
	val_result_csv='Batch_3966693_cocop_house_2020_03_23_20_05_31_mturk_100_img_hit_val_AdjustPrices.csv'
)





bdd_car_hit = SentinelHIT(
	task_nickname='bdd_car',
	dataset_name='bdd',
	train_img_dir = '',
	sentinel_img_dir ='',
	val_img_dir = '',
	train_bucket_name = '',
	val_bucket_name = '',
	sentinel_bucket_name = '',
	classnames = [
	],
	sentinels = [
	],
	train_result_csv='',
	val_result_csv=''
)




idd_person_hit = SentinelHIT(
	task_nickname='idd_person',
	dataset_name='idd',
	train_img_dir = '',
	sentinel_img_dir ='iddnew_person_shatter_slurmjob_val_2020_03_10',
	val_img_dir = 'iddnew_person_shatter_slurmjob_val_2020_03_10',
	train_bucket_name = '',
	val_bucket_name = '',
	sentinel_bucket_name = '',
	classnames = [
		'person-non-rider',
		'motorcyclist',
		'bicyclist',
		'rider-other'
	],
	sentinels = [
		('seq67_003556_leftImg8bit_51.jpg', 'person-non-rider'),
		('seq67_027650_leftImg8bit_82.jpg', 'person-non-rider'),
		('seq119_171342_leftImg8bit_37.jpg', 'person-non-rider'),
		('seq148_001519_leftImg8bit_54.jpg', 'person-non-rider'),
		('seq148_001519_leftImg8bit_53.jpg', 'person-non-rider'),
		('seq150_862362_leftImg8bit_166.jpg', 'person-non-rider'),
		('seq18_001786_leftImg8bit_39.jpg', 'person-non-rider'),
		('seq18_001786_leftImg8bit_45.jpg', 'person-non-rider'),
		('seq18_007402_leftImg8bit_31.jpg', 'person-non-rider'),
		('seq18_017087_leftImg8bit_81.jpg', 'person-non-rider')
	],
	train_result_csv='',
	val_result_csv=''
)


cityscapes_person_hit = SentinelHIT(
	task_nickname='cityscapes_person',
	dataset_name='cityscapes',
	train_img_dir = '',
	sentinel_img_dir ='',
	val_img_dir = '',
	train_bucket_name = '',
	val_bucket_name = '',
	sentinel_bucket_name = '',
	classnames = [
		'person-non-rider',
		'motorcyclist',
		'bicyclist',
		'rider-other'
	],
	sentinels = [
	],
	train_result_csv='',
	val_result_csv=''
)





# from coco door-stuff
COCO_doorstuff_showerdoor_hit = SentinelHIT(
	task_nickname='coco_doorstuff_showerdoor',
	dataset_name='coco',
	train_img_dir = '',
	sentinel_img_dir ='',
	val_img_dir = '',
	train_bucket_name = '',
	val_bucket_name = '',
	sentinel_bucket_name = '',
	classnames = [
	],
	sentinels = [
		('000000539710_8689316.png', 'door'),
		('000000542325_8624040.png', 'door'),
		('000000551358_8751499.png', 'door'),
		('000000231905_11977934.png', 'door'),
		('000000129507_8948106.png', 'door'),
		('000000071328_4876156.png', 'door'),
		('000000027578_7964562.png', 'door'),
		('000000015764_7966625.png', 'door'),
		('000000037509_2837846.png', 'shower_door'),
		('000000221307_5329744.png', 'shower_door'),
		('000000465591_6453383.png', 'shower_door'),
		('000000523876_5273489.png', 'shower_door'),
	],
	train_result_csv='',
	val_result_csv=''
)



COCO_car_pickuptruck_hit = SentinelHIT(
	task_nickname='cocop_car_pickuptruck',
	dataset_name='coco',
	train_img_dir = '',
	sentinel_img_dir ='',
	val_img_dir = '',
	train_bucket_name = '',
	val_bucket_name = '',
	sentinel_bucket_name = '',
	classnames = [
	],
	sentinels = [
	],
	train_result_csv='',
	val_result_csv=''
)



COCO_truck_pickuptruck_hit = SentinelHIT(
	task_nickname='cocop_car_pickuptruck',
	dataset_name='coco',
	train_img_dir = '',
	sentinel_img_dir ='',
	val_img_dir = '',
	train_bucket_name = '',
	val_bucket_name = '',
	sentinel_bucket_name = '',
	classnames = [
	],
	sentinels = [
	],
	train_result_csv='',
	val_result_csv=''
)







# RV
# pickup truck
# floor mat
# rug
# carpet