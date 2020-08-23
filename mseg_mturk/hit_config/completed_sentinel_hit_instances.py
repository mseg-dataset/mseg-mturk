#!/usr/bin/python3

from mseg.label_preparation.relabeled_data_containers import DatasetClassUpdateRecord

from mseg_mturk.sentinel_hit import SentinelHIT, RelabeledSentinelHIT


cocop_keyboard_hit = SentinelHIT(
	task_nickname='cocop_keyboard',
	dataset_name='cocop',
	train_img_dir = 'cocopanoptic_mseg_phase2_keyboard_train_2020_03_02',
	sentinel_img_dir ='cocopanoptic_mseg_phase2_keyboard_train_2020_03_02',
	val_img_dir = 'cocopanoptic_mseg_phase2_keyboard_val_2020_03_02',
	train_bucket_name = 'mseg-phase3-cocop-keyboard',
	val_bucket_name = 'mseg-phase3-cocop-keyboard',
	sentinel_bucket_name = 'mseg-phase3-cocop-keyboard',
	classnames = [
		('freestanding-keyboard'),
		('laptop-keyboard')
	],
	sentinels = [
		('000000578107_7502708.png', 'laptop-keyboard'),
		('000000558189_4538941.png', 'laptop-keyboard'),
		('000000263434_5131343.png', 'laptop-keyboard'),
		('000000201940_9015179.png', 'laptop-keyboard'),
		('000000189376_3225158.png', 'laptop-keyboard'),
		('000000534081_10467001.png', 'freestanding-keyboard'),
		('000000488201_2827575.png', 'freestanding-keyboard'),
		('000000480400_12109256.png', 'freestanding-keyboard'),
		('000000455020_7983593.png', 'freestanding-keyboard'),
		('000000454915_3885911.png', 'freestanding-keyboard'),
		('000000434900_3881526.png', 'freestanding-keyboard')
	],
	#train_result_csv='Batch_3977925_cocop_keyboard_2020_04_01_21_37_12_mturk_100_img_hit_train_AdjustPrices.csv',
	train_result_csv='Batch_3977925_cocop_keyboard_2020_04_01_21_37_12_mturk_100_img_hit_train_AdjustPrices.csv',
	val_result_csv='Batch_3977943_cocop_keyboard_2020_04_01_21_37_12_mturk_100_img_hit_val_AdjustPrices.csv'
)




COCOP_tent_hit = SentinelHIT(
	task_nickname='cocop_tent',
	dataset_name='cocop',
	train_img_dir =    'cocopanoptic_mseg_phase2_tent_train_2020_03_02',
	sentinel_img_dir = 'cocopanoptic_mseg_phase2_tent_train_2020_03_02',
	val_img_dir = 	   'cocopanoptic_mseg_phase2_tent_val_2020_03_02',
	train_bucket_name = 'mseg-phase3-cocop-tent',
	val_bucket_name = 'mseg-phase3-cocop-tent',
	sentinel_bucket_name = 'mseg-phase3-cocop-tent',
	classnames = [
		'tent',
		'awning'
	],
	sentinels = [
		('000000345136_5664562.png', 'tent'),
		('000000347496_4542780.png', 'tent'),
		('000000318108_8938531.png', 'tent'),
		('000000298051_10593185.png', 'tent'),
		('000000275502_11966866.png', 'tent'),
		('000000248911_8430014.png', 'tent'),
		('000000229583_12628401.png', 'tent'),
		('000000159026_14606561.png', 'tent'),
		('000000117690_13290961.png', 'tent'),
		('000000039847_4739152.png', 'awning'),
		('000000007095_7437697.png', 'awning')
	],
	#train_result_csv='Batch_3977987_cocop_tent_2020_04_01_22_29_57_mturk_100_img_hit_train_AdjustPrices.csv',
	#train_result_csv = 'Batch_3977987_cocop_tent_2020_04_01_22_29_57_mturk_100_img_hit_train_AdjustPrices_v2.csv',
	train_result_csv = 'Batch_3977987_cocop_tent_2020_04_01_22_29_57_mturk_100_img_hit_train_AdjustPrices_v3.csv',
	val_result_csv='Batch_3977995_cocop_tent_2020_04_01_22_29_57_mturk_100_img_hit_val_AdjustPrices_v2.csv'
)



MapillaryAcademic_water_hit = SentinelHIT(
	task_nickname='mapillary_academic_water',
	dataset_name='mapill_acad',
	train_img_dir = 'mseg_phase3_cluster_fixed2ndbug_mapillary_water_training_2020_03_10',
	sentinel_img_dir ='mseg_phase3_cluster_fixed2ndbug_mapillary_water_training_2020_03_10',
	val_img_dir = 'mseg_phase3_cluster_fixed2ndbug_mapillary_water_validation_2020_03_10',
	train_bucket_name = 'mseg-phase3-mapillaryacademic-water',
	val_bucket_name = 'mseg-phase3-mapillaryacademic-water',
	sentinel_bucket_name = 'mseg-phase3-mapillaryacademic-water',
	classnames = [
		'fountain',
		'sea',
		'river-lake',
		'water-other'
	],
	sentinels = [
		('mapillary_iAVuK_0ZiOR3qLxVFg6DCQ_7936.jpg', 'water-other'),
		('mapillary_66IVU5xKoGOibtPMsMrhGA_7936.jpg', 'water-other'),
		('mapillary_c-jNh3jdL-eiZoRTZTqSyQ_7936.jpg', 'water-other'),
		('mapillary_ekzhmixRO9yKPBHLrr5vYA_7936.jpg', 'water-other'),
		('mapillary_gTmuuT10eEm4W0LomwK11g_7936.jpg', 'water-other'),
		('mapillary_wm6ZlnhVacwmeUzpbyHcJQ_7936.jpg', 'river-lake'),
		('mapillary_ztaR_O637iVPndNgjR7nZA_7936.jpg', 'river-lake'),
		('mapillary_aDailxp-VC9IbQWfIp-8Rw_7936.jpg', 'river-lake'),
		('mapillary_54IkMGDSUV5J6LZX_XsJtw_7936.jpg', 'river-lake'),
		('mapillary_FGRMHxrdSIy2rwmvEOTeGA_7936.jpg', 'river-lake')
	],
	train_result_csv='Batch_3988717_mapillary_academic_water_2020_04_10_06_13_02_mturk_100_img_hit_train_AdjustPrices.csv',
	val_result_csv='Batch_3988716_mapillary_academic_water_2020_04_10_06_13_02_mturk_100_img_hit_val_AdjustPrices.csv'
)




coco_waterother_hit = SentinelHIT(
	task_nickname='cocop_waterother',
	dataset_name='cocop',
	train_img_dir = 'cocopanoptic_mseg_phase2_water-other_train_2020_03_02',
	sentinel_img_dir ='cocopanoptic_mseg_phase2_water-other_train_2020_03_02',
	val_img_dir = 'cocopanoptic_mseg_phase2_water-other_val_2020_03_02',
	train_bucket_name = 'mseg-phase3-cocop-water-other-bucket',
	val_bucket_name = 'mseg-phase3-cocop-water-other-bucket',
	sentinel_bucket_name = 'mseg-phase3-cocop-water-other-bucket',
	classnames = [
		'sea',
		'river-lake',
		'swimming-pool',
		'waterfall',
		'water-other'
	],
	sentinels = [
		('000000504143_4078637.png', 'river-lake'),
		('000000492562_5855313.png', 'river-lake'),
		#('000000501790_8556426.png', 'water-other'), # artificial, might be lake
		('000000486355_13286840.png', 'water-other'), # fire hydrant water
		('000000486163_5329233.png', 'water-other'), # puddle
		('000000431573_11385784.png', 'water-other'),
		('000000422515_14079186.png', 'water-other'),
		('000000481749_11052899.png', 'swimming-pool'),
		('000000473745_8873795.png', 'swimming-pool'),
		('000000434045_9327164.png', 'swimming-pool'),
		('000000401591_9997354.png', 'swimming-pool')
	],
	train_result_csv='Batch_3970709_cocop_waterother_2020_03_26_19_31_02_mturk_100_img_hit_train_AdjustPrices.csv',
	val_result_csv='Batch_3970708_cocop_waterother_2020_03_26_19_31_02_mturk_100_img_hit_val_AdjustPrices.csv'
)



ADE20k_plaything_hit = SentinelHIT(
	task_nickname='ade20k_plaything',
	dataset_name='ade20k',
	train_img_dir = 'mseg_phase2_ade20k_plaything_train_2019_12_16',
	sentinel_img_dir ='mseg_phase2_ade20k_plaything_train_2019_12_16',
	val_img_dir = 'mseg_phase2_ade20k_plaything_val_2019_12_16',
	train_bucket_name = 'mseg-phase3-ade20k-plaything',
	val_bucket_name = 'mseg-phase3-ade20k-plaything',
	sentinel_bucket_name = 'mseg-phase3-ade20k-plaything',
	classnames = [
		'plaything-other',
		'teddy-bear'
	],
	sentinels = [
		('ADE_train_00010120_255.png', 'plaything-other'),
		('ADE_train_00016087_219.png', 'plaything-other'),
		('ADE_train_00000576_232.png', 'plaything-other'),
		('ADE_train_00005464_98.png', 'plaything-other'),
		('ADE_train_00005483_247.png', 'plaything-other'),
		('ADE_train_00006613_62.png', 'plaything-other'),
		('ADE_train_00005490_255.png', 'teddy-bear'),
		('ADE_train_00013486_37.png', 'teddy-bear'),
		('ADE_train_00019617_255.png', 'teddy-bear'),
		('ADE_train_00005502_255.png', 'teddy-bear')
	],
	train_result_csv='Batch_3963151_ade20k_plaything_2020_03_19_23_47_36_mturk_100_img_hit_train_AdjustPrices_v2000.csv',
	val_result_csv='Batch_3962567_ade20k_plaything_2020_03_19_23_47_36_mturk_100_img_hit_val_AdjustPrices.csv'
)




COCO_pavementrunway_hit = SentinelHIT(
	task_nickname='cocop_pavementrunway',
	dataset_name='cocop',
	train_img_dir = '',
	sentinel_img_dir ='',
	val_img_dir = '',
	train_bucket_name = '',
	val_bucket_name = '',
	sentinel_bucket_name = '',
	classnames = [
		'airport_runway',
		'runway_other',
		'road',
		'pavement_sidewalk'
	],
	sentinels = [
	],
	train_result_csv='',
	val_result_csv=''
)



COCO_roadrunway_hit = SentinelHIT(
	task_nickname='cocop_roadrunway',
	dataset_name='cocop',
	train_img_dir = 'cocopanoptic_mseg_phase2_SEARCH_RUNWAY_from_road_train_2020_03_02',
	sentinel_img_dir ='cocopanoptic_mseg_phase2_SEARCH_RUNWAY_from_road_train_2020_03_02',
	val_img_dir = 'cocopanoptic_mseg_phase2_SEARCH_RUNWAY_from_road_val_2020_03_02',
	train_bucket_name = '',
	val_bucket_name = '',
	sentinel_bucket_name = '',
	classnames = [
		'airport_runway',
		'runway_other',
		'road',
		'pavement_sidewalk'
	],
	sentinels = [
	],
	train_result_csv='',
	val_result_csv=''
)





COCO_platform_hit = SentinelHIT(
	task_nickname='cocop_platform',
	dataset_name='cocop',
	train_img_dir = 'cocopanoptic_mseg_phase2_platform_train_2020_03_02',
	sentinel_img_dir ='cocopanoptic_mseg_phase2_platform_train_2020_03_02',
	val_img_dir = 'cocopanoptic_mseg_phase2_platform_val_2020_03_02',
	train_bucket_name = 'mseg-phase3-cocop-platform',
	val_bucket_name = 'mseg-phase3-cocop-platform',
	sentinel_bucket_name = 'mseg-phase3-cocop-platform',
	classnames = [
		'bridge',
		'pier-wharf',
		'platform'
	],
	sentinels = [
		('000000453352_6186853.png', 'platform'),
		('000000419284_12694438.png', 'platform'),
		('000000327479_8028297.png', 'platform'),
		('000000190546_8424085.png', 'platform'),
		('000000116633_8421501.png', 'platform'),
		('000000548013_6317423.png', 'platform'),
		('000000515360_8035505.png', 'platform'),
		('000000246809_5334654.png', 'pier-wharf'),
		('000000012455_1645086.png', 'pier-wharf'),
		('000000564459_6712682.png', 'pier-wharf')
	],
	#train_result_csv='Batch_3962044_cocop_platform_2020_03_18_23_51_23_mturk_100_img_hit_train_AdjustPrices.csv',
	train_result_csv = 'Batch_3962044_cocop_platform_2020_03_18_23_51_23_mturk_100_img_hit_train_AdjustPrices_V100.csv',
	val_result_csv='Batch_3961279_cocop_platform_2020_03_18_23_51_23_mturk_100_img_hit_val_AdjustPrices.csv'
)



COCO_bridge_hit = SentinelHIT(
	task_nickname='cocop_bridge',
	dataset_name='cocop',
	train_img_dir = 'cocopanoptic_mseg_phase2_bridge_train_2020_03_02',
	sentinel_img_dir ='cocopanoptic_mseg_phase2_bridge_train_2020_03_02',
	val_img_dir = 'cocopanoptic_mseg_phase2_bridge_val_2020_03_02',
	train_bucket_name = 'mseg-phase3-cocop-bridge',
	val_bucket_name = 'mseg-phase3-cocop-bridge',
	sentinel_bucket_name = 'mseg-phase3-cocop-bridge',
	classnames = [
		'bridge',
		'pier-wharf'
	],
	sentinels = [
		('000000256815_7960689.png', 'bridge'),
		('000000345980_3685963.png', 'bridge'),
		('000000448253_3684408.png', 'bridge'),
		('000000156370_5065033.png', 'bridge'),
		('000000002640_4014915.png', 'bridge'),
		('000000000349_9800586.png', 'bridge'),
		('000000577512_2761499.png', 'bridge'),
		('000000214958_3487799.png', 'pier-wharf'),
		('000000067788_6511704.png', 'pier-wharf'),
		('000000053840_1776430.png', 'pier-wharf')
	],
	#train_result_csv='Batch_3962057_cocop_bridge_2020_03_19_00_03_16_mturk_100_img_hit_train_AdjustPrices.csv',
	train_result_csv = 'Batch_3962057_cocop_bridge_2020_03_19_00_03_16_mturk_100_img_hit_train_AdjustPrices_v100.csv',
	val_result_csv='Batch_3961287_cocop_bridge_2020_03_19_00_03_16_mturk_100_img_hit_val_AdjustPrices.csv'
)





sunrgbd_counter_hit = SentinelHIT(
	task_nickname='sunrgbd_counter',
	dataset_name='sunrgbd',
	train_img_dir = 'mseg_phase2_sunrgbd_counter_shatter_train_2020_03_14',
	sentinel_img_dir ='mseg_phase2_sunrgbd_counter_shatter_train_2020_03_14',
	val_img_dir = '',
	train_bucket_name = 'mseg-phase2-sunrgbd-counter',
	val_bucket_name = '',
	sentinel_bucket_name = 'mseg-phase2-sunrgbd-counter',
	classnames = [
		'kitchen-island',
		'bathroom-counter',
		'counter-other',
		'multiple-categories-highlighted'
	],
	sentinels = [
		('img-004739_11.jpg', 'bathroom-counter'),
		('img-003665_11.jpg', 'bathroom-counter'),
		('img-005055_11.jpg', 'bathroom-counter'),
		('img-002380_11.jpg', 'counter-other'),
		('img-001773_11.jpg', 'counter-other'),
		('img-000166_11.jpg', 'counter-other'),
		('img-003475_11.jpg', 'counter-other'),
		('img-002670_11.jpg', 'counter-other')
	],
	#train_result_csv='Batch_3955821_sunrgbd_counter_2020_03_14_13_47_54_mturk_100_img_hit_train_AdjustPrices.csv',
	train_result_csv = 'Batch_3955821_sunrgbd_counter_2020_03_14_13_47_54_mturk_100_img_hit_train_AdjustPrices_v5.csv',
	val_result_csv=''
)




sunrgbd_chair_hit = SentinelHIT(
	task_nickname='sunrgbd_chair',
	dataset_name='sunrgbd',
	train_img_dir = 'mseg_phase2_sunrgbd_chair_shatter_train_2020_03_14',
	sentinel_img_dir ='mseg_phase2_sunrgbd_chair_shatter_train_2020_03_14',
	val_img_dir = 'mseg_phase2_sunrgbd_chair_shatter_test_2020_03_17',
	train_bucket_name = 'mseg-phase2-sunrgbd-chair',
	val_bucket_name = 'mseg-phase2-sunrgbd-chair',
	sentinel_bucket_name = 'mseg-phase2-sunrgbd-chair',
	classnames = [
		'stool',
		'seat',
		'swivel-chair',
		'armchair',
		'chair-other',
		'bench',
		'multiple-categories-highlighted'
	],
	sentinels = [
		('img-000885_4.jpg', 'armchair'),
		('img-001417_4.jpg', 'armchair'),
		('img-000838_4.jpg', 'armchair'),
		#('img-000719_4.jpg', 'armchair'),
		#('img-002701_4.jpg', 'chair-other'),
		('img-004706_4.jpg', 'chair-other'),
		('img-000510_4.jpg', 'chair-other'),
		('img-001121_4.jpg', 'swivel-chair'),
		('img-000725_4.jpg', 'swivel-chair'),
		('img-001795_4.jpg', 'seat')
	],
	#train_result_csv='Batch_3955838_sunrgbd_chair_2020_03_14_14_05_19_mturk_100_img_hit_train_AdjustPrices.csv',
	#train_result_csv = 'Batch_3955838_sunrgbd_chair_2020_03_14_14_05_19_mturk_100_img_hit_train_AdjustPrices_v2.csv',
	train_result_csv = 'Batch_3955838_sunrgbd_chair_2020_03_14_14_05_19_mturk_100_img_hit_train_AdjustPrices_v5.csv',
	#val_result_csv='Batch_3959428_sunrgbd_chair_2020_03_17_17_09_03_mturk_100_img_hit_val_AdjustPrices_v100.csv'
	#val_result_csv = 'Batch_3959428_sunrgbd_chair_2020_03_17_17_09_03_mturk_100_img_hit_val_AdjustPrices_v500.csv'
	#val_result_csv = 'Batch_3959428_sunrgbd_sunrgbd_chair_2020_03_17_17_09_03_mturk_100_img_hit_val_AdjustPrices_2000.csv'
	val_result_csv = 'Batch_3959428_sunrgbd_chair_2020_03_17_17_09_03_mturk_100_img_hit_val_AdjustPrices_7000.csv'
)






sunrgbd_lamp_hit = SentinelHIT(
	task_nickname='sunrgbd_lamp',
	dataset_name='sunrgbd',
	train_img_dir = 'mseg_phase2_sunrgbd_lamp_shatter_train_2020_03_14',
	sentinel_img_dir ='mseg_phase2_sunrgbd_lamp_shatter_train_2020_03_14',
	val_img_dir = 'mseg_phase2_sunrgbd_lamp_shatter_test_2020_03_17',
	train_bucket_name = 'mseg-phase2-sunrgbd-lamp',
	val_bucket_name = 'mseg-phase2-sunrgbd-lamp',
	sentinel_bucket_name = 'mseg-phase2-sunrgbd-lamp',
	classnames = [
		'sconce',
		'chandelier',
		'lamp',
		'light-other',
		'multiple-categories-highlighted'
	],
	sentinels = [
		('img-003911_34.jpg', 'lamp'),
		('img-004446_34.jpg', 'lamp'),
		('img-001026_34.jpg', 'lamp'),
		('img-000902_34.jpg', 'lamp'),
		('img-001205_34.jpg', 'lamp'),
		('img-002016_34.jpg', 'lamp'),
		('img-001949_34.jpg', 'lamp'),
		('img-001012_34.jpg', 'lamp'),
		('img-003171_34.jpg', 'light-other'),
		('img-004159_34.jpg', 'sconce'),
		('img-004491_34.jpg', 'sconce')
	],
	#train_result_csv='Batch_3955843_sunrgbd_lamp_2020_03_14_14_19_34_mturk_100_img_hit_train_AdjustPrices.csv',
	train_result_csv = 'Batch_3955843_sunrgbd_lamp_2020_03_14_14_19_34_mturk_100_img_hit_train_AdjustPrices_v3.csv',
	val_result_csv='Batch_3959426_sunrgbd_lamp_2020_03_17_17_09_03_mturk_100_img_hit_val_AdjustPrices_v3.csv'
)




cocop_table_merged_hit = SentinelHIT(
	task_nickname='cocop_table-merged',
	dataset_name='cocop',
	train_img_dir=	 'cocopanoptic_mseg_phase2_table-merged_train_2020_02_12',
	sentinel_img_dir='cocopanoptic_mseg_phase2_table-merged_train_2020_02_12',
	val_img_dir=	 'cocopanoptic_mseg_phase2_table-merged_val_2020_02_12',
	
	train_bucket_name=	 'mseg-phase2-cocop-tablemerged',
	val_bucket_name=  	 'mseg-phase2-cocop-tablemerged',
	sentinel_bucket_name='mseg-phase2-cocop-tablemerged',
	classnames = [
		'kitchen-island',
		'bathroom-counter',
		'desk',
		'table',
		'counter-other',
		'desk-and-table',
		'nightstand',
		'table-annotation-error'
	],
	sentinels = [
		#('000000555368_14736085.png', 'table'), # ccould have been a counter.
		('000000247782_723983.png',  'table'),
		('000000212787_5462908.png', 'table'),

		('000000205577_9278615.png', 'counter-other'),
		('000000197257_5996963.png', 'counter-other'),
		('000000458199_5863838.png', 'counter-other'),
		('000000577934_3303546.png', 'counter-other'),
		('000000199783_2305330.png', 'nightstand'),
		('000000180908_923158.png',  'nightstand'),
		('000000563656_3752003.png', 'nightstand'),
		('000000280799_2840974.png', 'kitchen-island')

		#('000000227497_6849170.png', 'desk-and-table'),
		#('000000190722_3766432.png', 'desk-and-table'),
		#('000000254134_2903409.png', 'desk'),
		#('000000561399_8551034.png', 'counter-other'), confuses ppl since is also table
		#('000000219269_6186612.png', 'desk'), bad example for sentinel since has 2 types in it
		#('000000232661_2970239.png', 'table'), confuses ppl since laptop on it

	],
	#train_result_csv='Batch_3941241_cocop_table-merged_2020_03_02_23_50_29_mturk_100_img_hit_train_AdjustPrices_v1.csv',
	#train_result_csv = 'Batch_3941241_cocop_table-merged_2020_03_02_23_50_29_mturk_100_img_hit_train_AdjustPrices_v3.csv',
	#train_result_csv='Batch_3941241_cocop_table-merged_2020_03_02_23_50_29_mturk_100_img_hit_train_AdjustPrices_v7.csv',
	#train_result_csv = 'Batch_3941241_cocop_table-merged_2020_03_02_23_50_29_mturk_100_img_hit_train_AdjustPrices_v15.csv',
	#train_result_csv = 'Batch_3941241__cocop_table-merged_2020_03_02_23_50_29_mturk_100_img_hit_train_AdjustPrices_v100.csv',
	#train_result_csv = 'Batch_3941241__cocop_table-merged_2020_03_02_23_50_29_mturk_100_img_hit_train_AdjustPrices_v200.csv',
	#train_result_csv = 'Batch_3941241_cocop_table-merged_2020_03_02_23_50_29_mturk_100_img_hit_train_AdjustPrices_v400.csv',
	train_result_csv = 'Batch_3941241__cocop_table-merged_2020_03_02_23_50_29_mturk_100_img_hit_train_AdjustPrices_v3000.csv',
	# submitted val set rejections (round 1) on feb 24 @ 10:47 pm EST
	# Round 1'Batch_3930540_cocop_table-merged_2020_02_23_03_25_21_mturk_100_img_hit_val.csv'
	#val_result_csv = #'Batch_3930540_cocop_table-merged_2020_02_23_03_25_21_mturk_100_img_hit_val_v2.csv'
	# 'Batch_3930540_round2_cocop_table-merged_2020_02_23_03_25_21_mturk_100_img_hit_val.csv'
	#val_result_csv = 'Batch_3930540_cocop_table-merged_2020_02_23_03_25_21_mturk_100_img_hit_val_v3.csv'
	# Re-made HIT
	#val_result_csv = 'Batch_3939108_cocop_table-merged_2020_03_01_03_04_50_mturk_100_img_hit_val_try2.csv'
	#val_result_csv = 'Batch_3939108_cocop_table-merged_2020_03_01_03_04_50_mturk_100_img_hit_val_try2_v2.csv'
	val_result_csv = 'Batch_3939108_cocop_table-merged_2020_03_01_03_04_50_mturk_100_img_hit_val_try2_V4000.csv'
)




idd_rider_hit = SentinelHIT(
	task_nickname='idd_rider',
	dataset_name='idd',
	train_img_dir = 'iddnew_rider_shatter_slurmjob_train_2020_03_10',
	sentinel_img_dir ='iddnew_rider_shatter_slurmjob_val_2020_03_10',
	val_img_dir = 'iddnew_rider_shatter_slurmjob_val_2020_03_10',
	train_bucket_name = 'mseg-phase2-idd-rider-bucket',
	val_bucket_name = 'mseg-phase2-idd-rider-bucket',
	sentinel_bucket_name = 'mseg-phase2-idd-rider-bucket',
	classnames = [
		'person-non-rider',
		'motorcyclist',
		'bicyclist',
		'rider-other'
	],
	sentinels = [
		('seq18_020886_leftImg8bit_58.jpg', 'motorcyclist'),
		('seq24_642575_leftImg8bit_86.jpg', 'motorcyclist'),
		('seq47_000897_leftImg8bit_94.jpg', 'motorcyclist'),
		# need to give instructions for 2nd person in back
		#('seq67_018331_leftImg8bit_72.jpg', 'motorcyclist'), 
		('seq150_029989_leftImg8bit_140.jpg', 'motorcyclist'),
		('seq172_166552_leftImg8bit_60.jpg', 'motorcyclist'),
		('seq24_060280_leftImg8bit_79.jpg', 'motorcyclist'),
		('seq21_086776_leftImg8bit_87.jpg', 'motorcyclist'),
		('seq21_240284_leftImg8bit_73.jpg', 'motorcyclist'),
		('seq21_318479_leftImg8bit_82.jpg', 'bicyclist')
	],
	#train_result_csv='Batch_3952468_idd_rider_2020_03_11_08_42_35_mturk_100_img_hit_train_AdjustPrices_v1.csv',
	train_result_csv = 'Batch_3952468_idd_rider_2020_03_11_08_42_35_mturk_100_img_hit_train_AdjustPrices_v3000.csv',
	#val_result_csv='Batch_3951986_idd_rider_2020_03_11_01_55_55_mturk_100_img_hit_val_AdjustPrices_v1.csv'
	val_result_csv = 'Batch_3951986_idd_rider_2020_03_11_01_55_55_mturk_100_img_hit_val_AdjustPrices.csv'
)



coco_light_hit = SentinelHIT(
	task_nickname='cocop_light',
	dataset_name='cocop',
	train_img_dir = 'cocopanoptic_mseg_phase2_light_train_2020_02_29',
	sentinel_img_dir ='cocopanoptic_mseg_phase2_light_train_2020_02_29',
	val_img_dir = 'cocopanoptic_mseg_phase2_light_val_2020_02_29',
	train_bucket_name = 'cocop-msegphase2-light',
	val_bucket_name = 'cocop-msegphase2-light',
	sentinel_bucket_name = 'cocop-msegphase2-light',
	classnames = [
		'sconce',
		'chandelier',
		'lamp',
		'light-other',
		'streetlight'
	],
	sentinels = [
		('000000369826_7961724.png', 'light-other'),
		('000000454631_8819098.png', 'light-other'),
		('000000459794_16448507.png', 'light-other'),
		('000000218931_8626356.png', 'light-other'), # ceiling fluorescent long
		('000000123855_14412268.png', 'light-other'), # ceiling fluorescent long
		('000000149918_9487334.png', 'sconce'), # bathroom light
		('000000033345_11065332.png', 'sconce'),
		('000000226611_9818347.png', 'sconce'),
		('000000083256_5728901.png', 'sconce'),
		('000000050323_8559792.png', 'lamp'), # w/ shade
		('000000463327_8956354.png', 'lamp'),
		('000000444233_10467786.png', 'lamp'),
		('000000081841_1776956.png', 'lamp'),
		('000000083968_10794436.png', 'chandelier'),
		('000000098679_4473924.png', 'streetlight')
	],
	#train_result_csv='Batch_3941237_cocop_light_2020_03_02_23_47_57_mturk_100_img_hit_train_AdjustPrices.csv',
	#train_result_csv = 'Batch_3941237_cocop_light_2020_03_02_23_47_57_mturk_100_img_hit_train_AdjustPrices_v15.csv',
	#train_result_csv = 'Batch_3941237_cocop_light_2020_03_02_23_47_57_mturk_100_img_hit_train_AdjustPrices_v30.csv',
	#train_result_csv = 'Batch_3941237_cocop_light_2020_03_02_23_47_57_mturk_100_img_hit_train_AdjustPrices_v400.csv',
	train_result_csv = 'Batch_3941237_cocop_light_2020_03_02_23_47_57_mturk_100_img_hit_train_AdjustPrices_v3000.csv',
	#val_result_csv='Batch_3939104_cocop_light_2020_03_01_02_50_07_mturk_100_img_hit_val_v2.csv'
	val_result_csv = 'Batch_3939104_cocop_light_2020_03_01_02_50_07_mturk_100_img_hit_val_v3000.csv'
	#'Batch_3939104_cocop_light_2020_03_01_02_50_07_mturk_100_img_hit_val.csv'
)



ADE20K_food_hit = SentinelHIT(
	task_nickname='ade20k_food',
	dataset_name='ADE20K',
	train_img_dir=	 'ade20k_phase2_food_train_2019_02_13',
	sentinel_img_dir='ade20k_phase2_food_train_2019_02_13',
	val_img_dir=	 'ade20k_phase2_food_val_2019_02_13',
	
	train_bucket_name=	 'mseg-phase2-ade20k-food',
	val_bucket_name=  	 'mseg-phase2-ade20k-food',
	sentinel_bucket_name='mseg-phase2-ade20k-food',
	classnames = [
		'banana','apple','sandwich','orange','broccoli',
		'carrot','hot dog','pizza','donut','cake',
		'fruit-other','food-other', 'vegetation'
	],
	
	sentinels = [
		('ADE_train_00011668_151.png', 'food-other'), # meat or fish
		('ADE_train_00014389_153.png', 'food-other'), # sushi
		('ADE_train_00006635_132.png', 'food-other'), # raw sausage
		('ADE_train_00002170_150.png', 'pizza'),
		('ADE_train_00013182_170.png', 'fruit-other'),
		('ADE_train_00011751_116.png', 'food-other'), # parsley/greens
		('ADE_train_00011691_197.png', 'food-other'), # onions and pumpkins
		('ADE_train_00010703_222.png', 'None_of_these'), # a hat
		('ADE_train_00002159_166.png', 'sandwich'),
		('ADE_train_00000931_123.png', 'food-other'), # cabbage/lettuce
		('ADE_train_00000931_123.png', 'vegetation'), # garden
	],
	#train_result_csv='Batch_3932681_ADE20K_ade20k_food_2020_02_25_00_32_40_mturk_100_img_hit_train.csv',
	train_result_csv = 'Batch_3932681_ade20k_food_2020_02_25_00_32_40_mturk_100_img_hit_train.csv',
	val_result_csv='Batch_3932678_ade20k_food_2020_02_25_00_32_40_mturk_100_img_hit_val_v3000.csv'
)



coco_counter_hit = SentinelHIT(
	task_nickname='cocop_counter',
	dataset_name='cocop',
	train_img_dir = 'cocopanoptic_mseg_phase2_counter_train_2020_03_02',
	sentinel_img_dir ='cocopanoptic_mseg_phase2_counter_train_2020_03_02',
	val_img_dir = 'cocopanoptic_mseg_phase2_counter_val_2020_03_02',
	train_bucket_name = 'mseg-phase2-cocop-counter',
	val_bucket_name = 'mseg-phase2-cocop-counter',
	sentinel_bucket_name = 'mseg-phase2-cocop-counter',
	classnames = [
		'kitchen-island',
		'bathroom-counter',
		'counter-other',
		'multiple-categories-highlighted'
	],
	sentinels = [
		('000000036968_5727838.png', 'counter-other'),
		('000000001392_4012856.png', 'counter-other'),
		('000000000987_11978190.png', 'counter-other'),
		('000000009668_9084347.png', 'counter-other'),
		('000000093140_9414329.png', 'counter-other'),
		('000000014282_4220033.png', 'bathroom-counter'),
		('000000033074_7252932.png', 'bathroom-counter'),
		('000000083002_2833752.png', 'bathroom-counter'),
		('000000108254_9413566.png', 'bathroom-counter'),
		('000000001355_4808837.png', 'kitchen-island')

	],
	train_result_csv='Batch_3955561_cocop_counter_2020_03_14_02_36_06_mturk_100_img_hit_train_AdjustPrices.csv',
	val_result_csv='Batch_3955559_cocop_counter_2020_03_14_02_36_06_mturk_100_img_hit_val_AdjustPrices.csv'
)




ADE20K_glass_hit = SentinelHIT(
	task_nickname='ade20k_glass',
	dataset_name='ADE20K',
	train_img_dir=	 'ade20k_phase2_glass_train_2019_02_12',
	sentinel_img_dir='ade20k_phase2_glass_train_2019_02_12',
	val_img_dir='ade20k_phase2_glass_val_2019_02_12',
	
	train_bucket_name='mseg-phase2-ade20k-glass',
	val_bucket_name=  'mseg-phase2-ade20k-glass',
	classnames = [
		'wine_glass', 'cup', 'glass-window/glass-surface'
	],
	sentinel_bucket_name='mseg-phase2-ade20k-glass',
	sentinels = [
		('ADE_train_00015799_220.png', 'wine_glass'),
		('ADE_train_00006886_209.png', 'wine_glass'),
		('ADE_train_00015811_158.png', 'wine_glass'),
		('ADE_train_00007186_169.png', 'wine_glass'),
		('ADE_train_00007078_228.png', 'wine_glass'),
		('ADE_train_00000189_231.png', 'cup'),
		('ADE_train_00002765_128.png', 'cup'),
		('ADE_train_00006831_235.png', 'cup'),
		('ADE_train_00006919_175.png', 'cup'),
		('ADE_train_00019916_198.png', 'cup'),
		('ADE_train_00002707_245.png', 'cup'),
		('ADE_train_00000644_68.png', 'cup'),
		('ADE_train_00009402_62.png', 'cup'),
		('ADE_train_00006109_120.png', 'cup'),
		('ADE_train_00018059_204.png', 'glass-window/glass-surface')
	],
	# train: analyzed and resubmitted on 2/19/2020 at 11pm
	#train_result_csv='Batch_3919790_ADE20K_ade20k_glass_2020_02_13_02_54_11_mturk_100_img_hit_train.csv',
	train_result_csv = 'Batch_3919790_ade20k_glass_2020_02_13_02_54_11_mturk_100_img_hit_train.csv',
	# val: all approved on 2/19/2020 at 11pm
	#val_result_csv='Batch_3919781_ADE20K_ade20k_glass_2020_02_13_02_54_11_mturk_100_img_hit_val.csv'
	val_result_csv = 'Batch_3919781_ade20k_glass_2020_02_13_02_54_11_mturk_100_img_hit_val_v1000.csv'
)



coco_chair_hit = SentinelHIT(
	task_nickname='cocop_chair',
	dataset_name='cocop',
	train_img_dir = 'cocopanoptic_mseg_phase2_chair_train_2020_02_29',
	sentinel_img_dir ='cocopanoptic_mseg_phase2_chair_train_2020_02_29',
	val_img_dir = 'cocopanoptic_mseg_phase2_chair_val_2020_02_29',
	train_bucket_name =	'mseg-phase2-cocop-chair',
	val_bucket_name = 'mseg-phase2-cocop-chair',
	sentinel_bucket_name = 'mseg-phase2-cocop-chair',
	classnames = [
		'stool',
		'seat',
		'swivel-chair',
		'armchair',
		'chair-other'
	],
	sentinels = [
		('000000002842_12680009.png', 'seat'),
		#('000000002842_8673855.png', 'seat'),
		('000000008329_9147002.png', 'seat'),
		('000000027241_12888726.png', 'seat'),
		('000000049985_921953.png', 'seat'),
		('000000011987_3621983.png', 'chair-other'),
		('000000036278_4611715.png', 'chair-other'),
		('000000014812_662829.png', 'stool'),
		('000000023731_2305153.png', 'swivel-chair'),
		('000000044266_2170912.png', 'swivel-chair'),
		('000000030434_3305645.png', 'armchair'),
		('000000052132_7046550.png', 'armchair')
	],
	#train_result_csv='Batch_3941206_cocop_chair_2020_03_02_22_59_19_mturk_100_img_hit_train_AdjustPrices.csv',
	#train_result_csv ='Batch_3941206_cocop_chair_2020_03_02_22_59_19_mturk_100_img_hit_train_AdjustPrices_v2.csv',
	#train_result_csv = 'Batch_3941206_cocop_chair_2020_03_02_22_59_19_mturk_100_img_hit_train_AdjustPrices_v3.csv',
	#train_result_csv = 'Batch_3941206_cocop_chair_2020_03_02_22_59_19_mturk_100_img_hit_train_AdjustPrices_v4.csv',
	#train_result_csv = 'Batch_3941206_cocop_chair_2020_03_02_22_59_19_mturk_100_img_hit_train_AdjustPrices_v5.csv',
	#train_result_csv = 'Batch_3941206_cocop_chair_2020_03_02_22_59_19_mturk_100_img_hit_train_AdjustPrices_v10.csv',
	#train_result_csv = 'Batch_3941206_cocop_chair_2020_03_02_22_59_19_mturk_100_img_hit_train_AdjustPrices_v15.csv',
	train_result_csv = 'Batch_3941206_cocop_chair_2020_03_02_22_59_19_mturk_100_img_hit_train_AdjustPrices_v3000.csv',
	#val_result_csv='Batch_3939096_cocop_chair_2020_03_01_01_55_23_mturk_100_img_hit_val_v2.csv'
	#val_result_csv = 'Batch_3939096_cocop_chair_2020_03_01_01_55_23_mturk_100_img_hit_val_v10.csv'
	val_result_csv = 'Batch_3939096_cocop_chair_2020_03_01_01_55_23_mturk_100_img_hit_val_v3000.csv'
	#'Batch_3939096_cocop_chair_2020_03_01_01_55_23_mturk_100_img_hit_val.csv'
)



cocop_diningtable_hit = SentinelHIT(
	task_nickname='cocop_diningtable',
	dataset_name='cocop',
	train_img_dir=	 'cocopanoptic_mseg_phase2_diningtable_train_2020_03_02',
	sentinel_img_dir='cocopanoptic_mseg_phase2_diningtable_train_2020_03_02',
	val_img_dir=	 'cocopanoptic_mseg_phase2_diningtable_val_2020_03_02',
	train_bucket_name= 'mseg-phase2-cocop-diningtable',
	val_bucket_name= 'mseg-phase2-cocop-diningtable',
	sentinel_bucket_name= 'mseg-phase2-cocop-diningtable',
	classnames = [
		'kitchen-island',
		'bathroom-counter',
		'desk',
		'table',
		'counter-other',
		'desk-and-table',
		'nightstand',
		'table-annotation-error'
	],
	sentinels = [
		('000000138910_2966119.png', 'table'), # low coffee table
		('000000191717_7961731.png', 'table'), # kitchen dining table
		('000000211107_5334378.png', 'table'), # low coffee table
		('000000279477_5658713.png', 'table'), # round restaurant table
		('000000403459_10857130.png', 'table'), # round table
		('000000535856_10203577.png', 'table'), # round restaurant table
		('000000078260_8947592.png', 'kitchen-island'),
		('000000102315_7571339.png', 'kitchen-island'),
		('000000124004_4221872.png', 'kitchen-island'),
		('000000150594_2511480.png', 'kitchen-island'),
		#('000000144056_2770270.png', 'kitchen-island')
	],
	#train_result_csv='Batch_3947732_cocop_diningtable_2020_03_03_00_21_20_mturk_100_img_hit_train_AdjustPrices.csv',
	#train_result_csv = 'Batch_3947732_cocop_diningtable_2020_03_03_00_21_20_mturk_100_img_hit_train_AdjustPrices.csv',
	#train_result_csv = 'Batch_3947732_cocop_diningtable_2020_03_03_00_21_20_mturk_100_img_hit_train_AdjustPrices_v30.csv',
	#train_result_csv = 'Batch_3947732_cocop_diningtable_2020_03_03_00_21_20_mturk_100_img_hit_train_AdjustPrices_v35.csv',
	#train_result_csv = 'Batch_3947732_cocop_diningtable_2020_03_03_00_21_20_mturk_100_img_hit_train_AdjustPrices_v40.csv',
	#train_result_csv = 'Batch_3947732_cocop_diningtable_2020_03_03_00_21_20_mturk_100_img_hit_train_AdjustPrices_v50.csv',
	#train_result_csv = 'Batch_3947732_cocop_diningtable_2020_03_03_00_21_20_mturk_100_img_hit_train_AdjustPrices_v70.csv',
	#train_result_csv = 'Batch_3947732_cocop_diningtable_2020_03_03_00_21_20_mturk_100_img_hit_train_AdjustPrices_v300.csv',
	#train_result_csv = 'Batch_3947732_cocop_diningtable_2020_03_03_00_21_20_mturk_100_img_hit_train_AdjustPrices_v500.csv',
	train_result_csv = 'Batch_3947732_cocop_diningtable_2020_03_03_00_21_20_mturk_100_img_hit_train_AdjustPrices_v3000.csv',
	#val_result_csv = 'Batch_3941264_cocop_diningtable_2020_03_03_00_21_20_mturk_100_img_hit_val_AdjustPrices.csv'
	#val_result_csv = 'Batch_3941264_cocop_diningtable_2020_03_03_00_21_20_mturk_100_img_hit_val_AdjustPrices_v10.csv'
	#val_result_csv = 'Batch_3941264_cocop_diningtable_2020_03_03_00_21_20_mturk_100_img_hit_val_AdjustPrices_v5.csv'
	#val_result_csv = 'Batch_3941264_cocop_diningtable_2020_03_03_00_21_20_mturk_100_img_hit_val_AdjustPrices_v60.csv'
	val_result_csv = 'Batch_3941264_cocop_diningtable_2020_03_03_00_21_20_mturk_100_img_hit_val_AdjustPrices_v3000.csv'
)


ADE20K_table_hit = SentinelHIT(
	task_nickname='ade20k_table',
	dataset_name='ade20k',
	train_img_dir = 'mseg_phase2_ade20k_table_train_2019_12_16',
	sentinel_img_dir ='mseg_phase2_ade20k_table_train_2019_12_16',
	val_img_dir = 'mseg_phase2_ade20k_table_val_2019_12_16',
	train_bucket_name = 'mseg-phase2-ade20k-table-bucket',
	val_bucket_name = 'mseg-phase2-ade20k-table-bucket',
	sentinel_bucket_name = 'mseg-phase2-ade20k-table-bucket',
	classnames = [
		'table',
		'nightstand',
		'cabinet',
		'kitchen-island',
		'bathroom-counter',
		'desk',
		'desk-and-table',
		'counter-other',
		'wardrobe'
	],
	sentinels = [
		('ADE_train_00003582_98.png', 'nightstand'),
		('ADE_train_00003599_232.png', 'nightstand'),
		('ADE_train_00000224_135.png', 'nightstand'),
		('ADE_train_00000390_80.png', 'nightstand'),
		('ADE_train_00000443_113.png', 'nightstand'),
		('ADE_train_00003236_96.png', 'nightstand'),
		('ADE_train_00003533_90.png', 'nightstand'),
		('ADE_train_00003609_119.png', 'nightstand'),
		('ADE_train_00004518_118.png', 'table'),
		('ADE_train_00006106_255.png', 'table'),
		('ADE_train_00006836_88.png', 'table'),
		('ADE_train_00011000_109.png', 'table'),
		('ADE_train_00004294_108.png', 'table')
	],
	#train_result_csv='Batch_3949080_ade20k_table_2020_03_07_21_39_19_mturk_100_img_hit_train_AdjustPrices_v2.csv',
	#train_result_csv = 'Batch_3949080_ade20k_table_2020_03_07_21_39_19_mturk_100_img_hit_train_AdjustPrices_v500.csv',
	#train_result_csv = 'Batch_3949080_ade20k_table_2020_03_07_21_39_19_mturk_100_img_hit_train_AdjustPrices_v1100.csv',
	train_result_csv = 'Batch_3949080_ade20k_table_2020_03_07_21_39_19_mturk_100_img_hit_train_AdjustPrices_v1000.csv',
	#val_result_csv='Batch_3947858_ade20k_table_2020_03_07_21_39_19_mturk_100_img_hit_val_AdjustPrices.csv'
	#val_result_csv = 'Batch_3947858_ade20k_table_2020_03_07_21_39_19_mturk_100_img_hit_val_AdjustPrices_v300.csv'
	val_result_csv = 'Batch_3947858_ade20k_table_2020_03_07_21_39_19_mturk_100_img_hit_val_AdjustPrices_v1000.csv'
)


ADE20K_animal_hit = SentinelHIT(
	task_nickname='ade20k_animal',
	dataset_name='ADE20K',
	train_img_dir='ade20k_phase2_animal_train_2019_12_16',
	val_img_dir='ade20k_phase2_animal_val_2019_12_16',
	sentinel_img_dir='ade20k_phase2_animal_train_2019_12_16',
	train_bucket_name='mseg-phase2-ade20k-animal-train',
	val_bucket_name='mseg-phase2-ade20k-animal-val',
	classnames = [
		'bird','cat','dog','horse','sheep','cow','elephant','bear','zebra','giraffe','animal-other'
	],
	sentinel_bucket_name='mseg-phase2-ade20k-animal-train',
	sentinels = [
		('ADE_train_00015024_128.png', 'bird'),
		('ADE_train_00005697_157.png', 'bird'),
		('ADE_train_00013625_191.png', 'elephant'),
		('ADE_train_00005583_116.png', 'elephant'),
		('ADE_train_00013027_204.png', 'elephant'),
		('ADE_train_00015267_162.png', 'sheep'),
		('ADE_train_00019887_85.png', 'giraffe'),
		('ADE_train_00020210_187.png', 'zebra'),
		('ADE_train_00015270_59.png', 'cow'),
		('ADE_train_00016122_255.png', 'animal-other'), # lion
		('ADE_train_00013365_204.png', 'animal-other'), # hippo
		('ADE_train_00020207_170.png', 'animal-other') # gorilla
	],
	#train_result_csv='Batch_3908640_ADE20K_ade20k_animal_2020_02_01_23_27_11_mturk_100_img_hit_train.csv',
	#train_result_csv='Batch_3908640_ADE20K_ade20k_animal_2020_02_08_mturk_100_img_hit_train.csv',
	#val_result_csv='Batch_3908638_ADE20K_ade20k_animal_2020_02_01_23_27_11_mturk_100_img_hit_val.csv'
	train_result_csv = 'Batch_3908640_ade20k_animal_2020_02_01_23_27_11_mturk_100_img_hit_train_v3.csv',
	val_result_csv = 'Batch_3908638_ade20k_animal_2020_02_01_23_27_11_mturk_100_img_hit_val_v3.csv'
)



ADE20K_chest_of_drawers_hit = SentinelHIT(
	task_nickname='ade20k_chest_of_drawers',
	dataset_name='ade20k',
	train_img_dir = 'mseg_phase2_ade20k_chest_of_drawers_train_2019_12_16',
	sentinel_img_dir ='mseg_phase2_ade20k_chest_of_drawers_train_2019_12_16',
	val_img_dir = 'mseg_phase2_ade20k_chest_of_drawers_val_2019_12_16',
	train_bucket_name = 'mseg-phase2-ade20k-chestofdrawers',
	val_bucket_name = 'mseg-phase2-ade20k-chestofdrawers',
	sentinel_bucket_name = 'mseg-phase2-ade20k-chestofdrawers',
	classnames = [
		'cabinet', 'chest-of-drawers'
	],
	sentinels = [
		('ADE_train_00010434_112.png', 'cabinet'),
		('ADE_train_00010401_165.png', 'cabinet'),
		('ADE_train_00010428_187.png', 'cabinet'),
		('ADE_train_00010426_105.png', 'cabinet'),
		('ADE_train_00010452_232.png',  'cabinet'),
		('ADE_train_00003950_137.png', 'chest-of-drawers'),
		('ADE_train_00003217_99.png', 'chest-of-drawers'),
		('ADE_train_00000294_51.png', 'chest-of-drawers'),
		('ADE_train_00008602_139.png', 'chest-of-drawers'),
		('ADE_train_00005528_142.png', 'chest-of-drawers')
	],
	train_result_csv='Batch_3951661_ade20k_chest_of_drawers_2020_03_10_18_22_18_mturk_100_img_hit_train_AdjustPrices.csv',
	val_result_csv='Batch_3951659_ade20k_chest_of_drawers_2020_03_10_18_22_18_mturk_100_img_hit_val_AdjustPrices.csv'
)



# published
cityscapes_rider_hit = SentinelHIT(
	task_nickname='cityscapes_rider',
	dataset_name='cityscapes',
	train_img_dir = 'cityscapes_rider_shatter_slurmjob_train_2020_03_10',
	sentinel_img_dir ='cityscapes_rider_shatter_val_2020_03_10',
	val_img_dir = 'cityscapes_rider_shatter_val_2020_03_10',
	train_bucket_name = 'mseg-phase2-cityscapes-rider-bucket',
	val_bucket_name = 'mseg-phase2-cityscapes-rider-bucket',
	sentinel_bucket_name = 'mseg-phase2-cityscapes-rider-bucket',
	classnames = [
		'person-non-rider',
		'motorcyclist',
		'bicyclist',
		'rider-other'
	],
	sentinels = [
		('seqmunster_munster_000039_000019_leftImg8bit_51.jpg', 'bicyclist'),
		('seqmunster_munster_000069_000019_leftImg8bit_135.jpg', 'bicyclist'),
		('seqmunster_munster_000140_000019_leftImg8bit_73.jpg', 'bicyclist'),
		('seqfrankfurt_frankfurt_000001_016462_leftImg8bit_60.jpg', 'bicyclist'),
		('seqfrankfurt_frankfurt_000001_060906_leftImg8bit_50.jpg', 'bicyclist'),
		('seqmunster_munster_000026_000019_leftImg8bit_133.jpg', 'bicyclist'),
		('seqmunster_munster_000055_000019_leftImg8bit_93.jpg', 'bicyclist'),
		('seqmunster_munster_000077_000019_leftImg8bit_64.jpg', 'bicyclist'),
		('seqfrankfurt_frankfurt_000001_083199_leftImg8bit_122.jpg', 'motorcyclist'),
		('seqmunster_munster_000094_000019_leftImg8bit_169.jpg', 'motorcyclist')
	],
	#train_result_csv='Batch_3952352_cityscapes_rider_2020_03_11_10_46_02_mturk_100_img_hit_train_AdjustPrices_v3.csv',
	train_result_csv = 'Batch_3952352_cityscapes_rider_2020_03_11_10_46_02_mturk_100_img_hit_train_AdjustPrices_v20.csv',
	val_result_csv='Batch_3951976_cityscapes_rider_2020_03_11_01_42_56_mturk_100_img_hit_val_AdjustPrices_V1.csv'
)



bdd_rider_hit = SentinelHIT(
	task_nickname='bdd_rider',
	dataset_name='bdd',
	train_img_dir = 'mseg_phase2_bdd_rider_shatter_train_2020_03_06',
	sentinel_img_dir ='mseg_phase2_bdd_rider_shatter_train_2020_03_06',
	val_img_dir = 'mseg_phase2_bdd_rider_shatter_val_2020_03_06',
	train_bucket_name = 'mseg-phase2-bdd-rider-shatter-bucket',
	val_bucket_name = 'mseg-phase2-bdd-rider-shatter-bucket',
	sentinel_bucket_name = 'mseg-phase2-bdd-rider-shatter-bucket',
	classnames = [
		'person-non-rider',
		'motorcyclist',
		'bicyclist',
		'rider-other',
		'annotation-error'
	],
	sentinels = [
		('33ac83ac-3f0d3a59_12.jpg', 'bicyclist'),
		('bdb658c2-01af4ab1_12.jpg', 'bicyclist'),
		('0d242d07-6298ac79_12.jpg', 'bicyclist'),
		('3c0413b4-0ee0647c_12.jpg', 'bicyclist'),
		('09cdd188-4e98738e_12.jpg', 'bicyclist'),
		('51fff027-6598f6c1_12.jpg', 'motorcyclist'),
		('c96e0b6a-f3d8aa78_12.jpg', 'motorcyclist'),
		#('8413f861-580b500d_12.jpg', 'person-non-rider')
		('1a63c3c1-d2545a08_12.jpg', 'annotation-error')
	],
	#train_result_csv='Batch_3947671_bdd_rider_2020_03_07_16_12_46_mturk_100_img_hit_train_AdjustPrices.csv',
	train_result_csv='Batch_3947671_bdd_rider_2020_03_07_16_12_46_mturk_100_img_hit_train_AdjustPrices_v2.csv',
	#val_result_csv='Batch_3946988_bdd_rider_2020_03_06_18_27_18_mturk_100_img_hit_val_AdjustPrices.csv'
	val_result_csv = 'Batch_3947674_bdd_rider_2020_03_07_16_12_46_mturk_100_img_hit_val_AdjustPrices.csv'
)




bdd_person_hit = SentinelHIT(
	task_nickname='bdd_person',
	dataset_name='bdd',
	train_img_dir = 'mseg_phase2_bdd_person_shatter_train_2020_03_06',
	sentinel_img_dir ='mseg_phase2_bdd_person_shatter_train_2020_03_06',
	val_img_dir = 'mseg_phase2_bdd_person_shatter_val_2020_03_06',
	train_bucket_name = 'mseg-phase2-bdd-person',
	val_bucket_name = 'mseg-phase2-bdd-person',
	sentinel_bucket_name = 'mseg-phase2-bdd-person',
	classnames = [
		'person-non-rider',
		'person-annotation-error',
		'motorcyclist',
		'bicyclist',
		'rider-other',
		'multiple-different-categories-highlighted'
	],
	sentinels = [
		('be26ac57-35dabb9c_11.jpg', 'person-non-rider'),
		('80b3fc35-c3496b02_11.jpg', 'person-non-rider'),
		('7a59a6f8-00000000_11.jpg', 'person-non-rider'),
		('0cafe7ab-e22edf50_11.jpg', 'person-non-rider'),
		('051d6f8d-ab210001_11.jpg', 'person-non-rider'),
		('314db341-693a7d4d_11.jpg', 'person-non-rider'),
		('1edd9c50-b4b5d22b_11.jpg', 'person-non-rider'),
		#('5f697884-f3f9d519_11.jpg', 'person-annotation-error'),
		
		#('348b0361-241cdc35_11.jpg', 'person-annotation-error'),
		#('c57363a5-1237e193_11.jpg', 'multiple-different-categories-highlighted')
		#('7f6e302c-f0cec2b1_11.jpg', 'person-annotation-error'), IS CAR

	],
	#train_result_csv='Batch_3947638_bdd_person_2020_03_06_17_39_17_mturk_100_img_hit_train_AdjustPrices.csv',
	train_result_csv = 'Batch_3947638_bdd_person_2020_03_06_17_39_17_mturk_100_img_hit_train_AdjustPrices_v2.csv',# 'Batch_3947638_bdd_person_2020_03_06_17_39_17_mturk_100_img_hit_train_AdjustPrices.csv',
	val_result_csv='Batch_3946926_bdd_person_2020_03_06_17_39_17_mturk_100_img_hit_val_AdjustPrices.csv'
)




# Analyzed Feb 19, 2020
# instructions did not specify for what to do 
# (for erson not on moto but wearing helmet (is not motorcyclist)
COCOP_MotorcyclistBicyclist_HIT = RelabeledSentinelHIT(
	task_nickname='cocop_motorcyclist_bicyclist',
	dataset_name='cocopanoptic',
	train_img_dir='cocopanoptic_mseg_phase2_personmotorcyclebicycle_train',
	val_img_dir='cocopanoptic_mseg_phase2_personmotorcyclebicycle_val',
	sentinel_img_dir='cocopanoptic_mseg_phase2_personmotorcyclebicycle_train',
	train_bucket_name='mseg-phase2-ade20k-cocop-person-moto-bicycle',
	val_bucket_name='mseg-phase2-ade20k-cocop-person-moto-bicycle',
	# these are the new classname choices
	classnames = [
		'motorcyclist',
		'bicyclist',
		'person-non-rider',
		'rider-other'],
	sentinel_bucket_name='mseg-phase2-ade20k-cocop-person-moto-bicycle',
	sentinels=[
		('000000078364_7694175.png', 'motorcyclist'),
		('000000005638_7565690.png', 'motorcyclist'),
		('000000004355_4275002.png', 'motorcyclist'),
		('000000001232_2367770.png', 'motorcyclist'),
		('000000237894_8553367.png', 'motorcyclist'),
		('000000022228_6447726.png', 'bicyclist'),
		('000000004376_6639172.png', 'bicyclist'),
		('000000012818_6119782.png', 'bicyclist'),
		('000000001722_2699047.png', 'bicyclist'),

		('000000385779_9936295.png', 'rider-other'),
		('000000421131_1448476.png', 'person-non-rider'),
		#('000000460470_3420726.png', 'person-non-rider'), # needed instruction
		('000000531735_6379861.png', 'person-non-rider'), # needed more examples of this 
		('000000536179_3813197.png', 'person-non-rider')
		#('000000581189_4013373.png', 'None_of_these'),
		# MAKE SENTINEL OF PEOPLE IN CARS
	],
	# relabeled class is rider
	train_prior_record=DatasetClassUpdateRecord('cocopanoptic', 'train', 'person', 'rider', 'phase1/person_rider_classification/2019_08_08_coco_riders_80percentconfidence_trainsplit.txt'),
	val_prior_record=DatasetClassUpdateRecord('cocopanoptic', 'val', 'person', 'rider',   'phase1/person_rider_classification/2019_08_15_coco_rider_80percentconfidence_valsplit.txt'),
	# below shows round 2
	#train_result_csv='Batch_3932637_cocop_motorcyclist_bicyclist_2020_02_23_03_21_33_mturk_100_img_hit_train.csv',
	#train_result_csv='Batch_3932637_cocop_motorcyclist_bicyclist_2020_02_23_03_21_33_mturk_100_img_hit_train_v2.csv',
	train_result_csv='Batch_3932637_cocop_motorcyclist_bicyclist_2020_02_23_03_21_33_mturk_100_img_hit_train_v3.csv',
	# THROW AWAY train_result_csv='Batch_3919772_cocopanoptic_cocop_motorcyclist_bicyclist_2020_02_13_02_33_15_mturk_100_img_hit_train.csv',
	# Round 1 'Batch_3930537_cocop_motorcyclist_bicyclist_2020_02_23_03_21_33_mturk_100_img_hit_val.csv'
	# Round 2 below
	val_result_csv = 'Batch_3930537_Round2_cocop_motorcyclist_bicyclist_2020_02_23_03_21_33_mturk_100_img_hit_val.csv'
	# THROW AWAY val_result_csv='Batch_3919759_cocopanoptic_cocop_motorcyclist_bicyclist_2020_02_13_02_03_06_mturk_100_img_hit_val.csv',
)



# relabel COCOPanoptic "person" later -- would use these
COCOP_PersonNonRider_HIT = RelabeledSentinelHIT(
	task_nickname='cocop_nonrider',
	dataset_name='cocopanoptic',
	train_img_dir='cocopanoptic_mseg_phase2_personmotorcyclebicycle_train',
	val_img_dir='cocopanoptic_mseg_phase2_personmotorcyclebicycle_val',
	sentinel_img_dir='cocopanoptic_mseg_phase2_personmotorcyclebicycle_train',
	train_bucket_name='mseg-phase2-ade20k-cocop-person-moto-bicycle',
	val_bucket_name='mseg-phase2-ade20k-cocop-person-moto-bicycle',
	# these are the new classname choices
	classnames = [
		'motorcyclist',
		'bicyclist',
		'person-non-rider',
		'rider-other'],
	sentinel_bucket_name='mseg-phase2-ade20k-cocop-person-moto-bicycle',
	sentinels=[
		('000000001232_2367770.png', 'motorcyclist'),
		('000000004355_4275002.png', 'motorcyclist'),
		('000000005638_7565690.png', 'motorcyclist'),
		('000000078364_7694175.png', 'motorcyclist'),
		('000000237894_8553367.png', 'motorcyclist'),
		('000000004376_6639172.png', 'bicyclist'),
		('000000001722_2699047.png', 'bicyclist'),
		('000000012818_6119782.png', 'bicyclist'),
		('000000022228_6447726.png', 'bicyclist'),
		('000000385779_9936295.png', 'rider-other'),
		('000000421131_1448476.png', 'person-non-rider'),
		#('000000460470_3420726.png', 'person-non-rider'), # needed insturciton
		('000000531735_6379861.png', 'person-non-rider'), # needed more examples of this 
		('000000536179_3813197.png', 'person-non-rider')
		#('000000581189_4013373.png', 'None_of_these'),
		# MAKE SENTINEL OF PEOPLE IN CARS
	],
	# relabeled class is PERSON
	train_prior_record=DatasetClassUpdateRecord('cocopanoptic', 'train', 'person', 'person','phase1/person_rider_classification/2019_08_08_coco_person_80percentconfidence_trainsplit.txt'),
	val_prior_record=DatasetClassUpdateRecord('cocopanoptic', 'val', 'person', 'person',  'phase1/person_rider_classification/2019_08_15_coco_person_80percentconfidence_valsplit.txt'),
	
	# below shows round 2
	train_result_csv='Batch_3937661_cocop_nonrider_2020_02_28_00_50_10_mturk_100_img_hit_train.csv',
	val_result_csv ='Batch_3937046_cocop_nonrider_2020_02_28_00_50_10_mturk_100_img_hit_val.csv'
)






ADE20K_motorcyclist_bicyclist_hit = RelabeledSentinelHIT(
	task_nickname='ade20k_motorcyclist_bicyclist',
	dataset_name='ADE20K',
	train_img_dir='mseg_phase2_ade20k_motorcyclist_bicyclist_etc_2020_03_06_train',
	val_img_dir='mseg_phase2_ade20k_motorcyclist_bicyclist_etc_2020_03_06_val',
	sentinel_img_dir='mseg_phase2_ade20k_motorcyclist_bicyclist_etc_2020_03_06_train',
	train_bucket_name='mseg-phase2-ade20k-motorcyclist-bicyclist-bucket-2020-03-06',
	val_bucket_name='mseg-phase2-ade20k-motorcyclist-bicyclist-bucket-2020-03-06',
	sentinel_bucket_name='mseg-phase2-ade20k-motorcyclist-bicyclist-bucket-2020-03-06',
	classnames = [
		'motorcyclist',
		'bicyclist',
		'person-non-rider',
		'rider-other'
	],
	sentinels = [
		('ADE_train_00015455_255.png', 'person-non-rider'),
		('ADE_train_00017749_150.png', 'bicyclist'),
		('ADE_train_00018345_153.png', 'person-non-rider'),
		('ADE_train_00017542_31.png', 'person-non-rider'),
		('ADE_train_00015963_37.png', 'motorcyclist'),
		('ADE_train_00017179_201.png', 'motorcyclist'),
		('ADE_train_00007553_185.png', 'person-non-rider'),
		('ADE_train_00007553_162.png', 'person-non-rider'),
		('ADE_train_00016686_213.png', 'person-non-rider'),
		('ADE_train_00012358_242.png', 'bicyclist'),
		('ADE_train_00013713_181.png', 'bicyclist'),
		('ADE_train_00016686_156.png', 'bicyclist'),
		('ADE_train_00017218_133.png', 'bicyclist')
	],
	# RELABELED CLASS IS RIDER
	train_prior_record=DatasetClassUpdateRecord('ade20k', 'train', 'person', 'rider', 'phase1/person_rider_classification/2019_10_31_ade20k_rider_trainsplit.txt'),
	val_prior_record=DatasetClassUpdateRecord('ade20k', 'val', 'person', 'rider',   'phase1/person_rider_classification/2019_10_31_ade20k_rider_valsplit.txt'),
	train_result_csv='Batch_3946348_ade20k_motorcyclist_bicyclist_2020_03_06_10_51_46_mturk_100_img_hit_train_AdjustPrices.csv',
	val_result_csv='Batch_3946342_ade20k_motorcyclist_bicyclist_2020_03_06_10_51_46_mturk_100_img_hit_val_AdjustPrices.csv'
)


# relabel COCOPanoptic "person" later -- would use these
ADE20K_PersonNonRider_HIT = RelabeledSentinelHIT(
	task_nickname='ade20k_nonrider',
	dataset_name='ade20k',
	train_img_dir='mseg_phase2_ade20k_motorcyclist_bicyclist_etc_2020_03_06_train',
	val_img_dir='mseg_phase2_ade20k_motorcyclist_bicyclist_etc_2020_03_06_val',
	sentinel_img_dir='mseg_phase2_ade20k_motorcyclist_bicyclist_etc_2020_03_06_train',
	train_bucket_name='mseg-phase2-ade20k-motorcyclist-bicyclist-bucket-2020-03-06',
	val_bucket_name='mseg-phase2-ade20k-motorcyclist-bicyclist-bucket-2020-03-06',
	sentinel_bucket_name='mseg-phase2-ade20k-motorcyclist-bicyclist-bucket-2020-03-06',
	# these are the new classname choices
	classnames = [
		'motorcyclist',
		'bicyclist',
		'person-non-rider',
		'rider-other'],
	sentinels=[
		('ADE_train_00015455_255.png', 'person-non-rider'),
		('ADE_train_00017749_150.png', 'bicyclist'),
		('ADE_train_00018345_153.png', 'person-non-rider'),
		('ADE_train_00017542_31.png', 'person-non-rider'),
		('ADE_train_00015963_37.png', 'motorcyclist'),
		('ADE_train_00017179_201.png', 'motorcyclist'),
		('ADE_train_00007553_185.png', 'person-non-rider'),
		('ADE_train_00007553_162.png', 'person-non-rider'),
		('ADE_train_00016686_213.png', 'person-non-rider'),
		('ADE_train_00012358_242.png', 'bicyclist'),
		('ADE_train_00013713_181.png', 'bicyclist'),
		('ADE_train_00016686_156.png', 'bicyclist'),
		('ADE_train_00017218_133.png', 'bicyclist')
	],
	# relabeled class is PERSON
	train_prior_record=DatasetClassUpdateRecord('ade20k', 'train', 'person', 'person','phase1/person_rider_classification/2019_10_31_ade20k_person_trainsplit.txt'),
	val_prior_record=DatasetClassUpdateRecord('ade20k', 'val', 'person', 'person',  'phase1/person_rider_classification/2019_10_31_ade20k_person_valsplit.txt'),
	train_result_csv = 'Batch_3946380_ade20k_nonrider_2020_03_06_11_15_47_mturk_100_img_hit_train_AdjustPrices.csv',
	val_result_csv ='Batch_3946376_ade20k_nonrider_2020_03_06_11_15_47_mturk_100_img_hit_val_AdjustPrices.csv'
)