#!/usr/bin/python3

import csv
import glob
from pathlib import Path
from shutil import copyfile
from typing import List, Mapping, Tuple

from mseg_mturk.hit_utils import WorkerHITResult
from mseg_mturk.sentinel_hit import SentinelHIT

from mseg.utils.dir_utils import check_mkdir

"""
Class to process an AMT submitted batch csv.
"""

_ROOT = Path(__file__).resolve().parent.parent

NUM_IMGS_PER_HIT = 100

class BatchResult:
	"""
	Stores results for a single MTurk batch (loaded from a CSV file).
	"""
	def __init__(
		self, 
		split: str, 
		hit_info: SentinelHIT, 
		csv_dir: str, 
		dump_root: str,
		use_prior_labeling: bool,
		accuracy_thresh: int = 100 # acceptance threshold, in percent
	):
		""" 
			Args:
			-	split: string representing dataset split, either 'train' or 'val'
			-	hit_info: 
			-	csv_dir: string representing
			-	dump_root: string representing

			Returns:
			-	None
		"""
		self.split = split
		self.hit_info = hit_info
		self.csv_dir = csv_dir
		self.dump_root = dump_root

		if split == 'train':
			img_dir = hit_info.train_img_dir
			csv_fname = hit_info.train_result_csv
		elif split == 'val':
			img_dir = hit_info.val_img_dir
			csv_fname = hit_info.val_result_csv

		self.img_dir = img_dir
		split_img_fpaths = glob.glob(f'{self.dump_root}/{self.img_dir}/*.png')
		if len(split_img_fpaths) == 0:
			# was jpeg instead!
			split_img_fpaths = glob.glob(f'{self.dump_root}/{self.img_dir}/*.jpg')
		
		if use_prior_labeling:
			split_img_fpaths = filter_to_prev_labeled(hit_info, split, split_img_fpaths)

		self.split_img_fnames = [ Path(fpath).name for fpath in split_img_fpaths ]
		self.num_split_imgs = len(split_img_fpaths)
		self.csv_fname = csv_fname

		self.sentinel_fnames = list(zip(*hit_info.sentinels))[0] # 0th item of each tuple
		self.sentinel_classnames = list(zip(*hit_info.sentinels))[1] # 1st item of each tuple

		self.csv_fpath = f'{csv_dir}/{csv_fname}'
		self.analyzed_csv_fpath = f'{csv_dir}/analyzed_{csv_fname}'

		self.worker_rows = self.read_csv_rows(self.csv_fpath)

		# True/False -- whether to save folders w/ correctness of worker responses
		self.save_tf_worker_answers = True 

		self.duration_acc_tuples = []
		self.acc_thresh = accuracy_thresh # accuracy (percent) required for acceptance
		self.rejection_info_string = f'We required at least {self.acc_thresh} % accuracy '
		self.rejection_info_string += 'on the easiest examples, '
		self.rejection_info_string += 'but you were not able to meet this threshold. We '
		self.rejection_info_string += 'need more careful and precise work.'


	def read_csv_rows(self, csv_fpath: str) -> List[WorkerHITResult]:
		"""
			Args:
			-	csv_fpath

			Returns:
			-	rows: 
		"""
		rows = []
		with open(csv_fpath, 'r') as csv_file:
			csv_reader = csv.DictReader(csv_file)
			for j, row in enumerate(csv_reader):
				rows += [WorkerHITResult(row)]
		return rows


	def analyze_acc(self):
		"""
			Loop through submitted HITs. For all 100 images, check if sentinel.
			If it is a sentinel, check correctness. Compute mean accuracy per HIT.
			Set status in WorkerHITResult for each HIT to 'Approved' or 'Rejected'
			based on 90% accuracy cutoff.

			Per worker, record incorrectly predicted sentinel images for each class.

			Also plot a histogram of worker accuracy.

			Args:
			-	None

			Returns:
			-	None
		"""
		for row in self.worker_rows:
			if row.AssignmentStatus != 'Submitted':
				continue
			correctness_arr = []
			for i in range(NUM_IMGS_PER_HIT):
				key = f'Answer.choice_{i}'
				if key not in row.__dict__:
					print(f'\tMissing {key} ')
					continue
				category = getattr(row,key)
				img_url = getattr(row, f'Input.image_url_{i}')
				img_fname = Path(img_url).name
				
				if self.is_sentinel(img_fname):
					is_correct = self.verify_answer_correctness(img_fname, category)
					correctness_arr += [is_correct]
					self.imwrite_tf_worker_answer(is_correct, img_fname, row, category)

			correctness_arr = np.array(correctness_arr)
			acc = correctness_arr.mean() * 100
			
			print(f'{self.split}: {row.WorkerId}, {row.HITId}')
			print(f'\tWorker Acc={acc:.2f}: {correctness_arr.sum()}/{correctness_arr.size}')
			
			if acc >= self.acc_thresh:
				row.Approve = 'x'
				row.AssignmentStatus = 'Approved'
			else:
				row.Reject = self.rejection_info_string
				row.AssignmentStatus = 'Rejected'
				print('\t Reject!')

			duration_m = get_duration_from_csv_row(row)
			self.duration_acc_tuples += [(duration_m, acc)]

		if len(self.duration_acc_tuples) > 0:
			plot_acc_histogram(self.duration_acc_tuples)


	def imwrite_tf_worker_answer(self, 
		is_correct: bool, 
		img_fname: str, 
		row: WorkerHITResult,
		category: str):
		"""
		TODO: Switch to using os.path() for windows compatibility.

			Args:
			-	is_correct: boolean representing if correct answer choice selected
			-	img_fname
			-	row
			-	category

			Returns:
		"""
		if '/' in category:
			# extra forward slash will screw up the filename
			category = category.replace('/', '_')
		if self.save_tf_worker_answers:
			# save under True/False distinction
			src = f'{_ROOT}/temp_files/{self.hit_info.sentinel_img_dir}/{img_fname}'
			
			new_dirpath = f'{self.dump_root}'
			new_dirpath += f'/{self.hit_info.task_nickname}'
			new_dirpath += f'/{self.split}'
			new_dirpath += f'/{row.WorkerId}'
			new_dirpath += f'/{row.HITId}'
			new_dirpath += f'/{str(is_correct)}'
			new_dirpath += f'/{category}'

			check_mkdir(new_dirpath)
			dst = f'{new_dirpath}/{img_fname}'
			copyfile(src, dst)


	def save_img_classification(self, img_fname: str, category: str):
		"""
			Args:
			-	img_fname
			-	category

			Returns:
			-	
		"""
		src = f'{_ROOT}/temp_files/{self.img_dir}/{img_fname}'
		
		new_dirpath = f'{self.dump_root}'
		new_dirpath += f'/{self.hit_info.task_nickname}'
		new_dirpath += f'/{self.split}'
		new_dirpath += f'/{category}'

		check_mkdir(new_dirpath)
		dst = f'{new_dirpath}/{img_fname}'

		if Path(dst).exists():
			return

		copyfile(src, dst)


	def is_sentinel(self, img_fname):
		"""
			Args:
			-	img_fname

			Returns:
			-	boolean representing if this image is a sentinel
		"""
		return img_fname in self.sentinel_fnames


	def enter_decision(self):
		"""
			Record in CSV which HITs should be accepted or rejected.

			APPROVE ASSIGNMENT: Indicate which assignments to approve by 
			putting an "x" under a column titled "Approve". 

			REJECT ASSIGNMENT: 
			Indicate which assignments to reject by putting your reject 
			feedback under a column titled "Reject".

			Args:
			-	None

			Returns:
			-	None
		"""
		with open(self.analyzed_csv_fpath, 'w', newline='') as csvfile:

			fieldnames = self.worker_rows[0].__dict__.keys()
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			for row in self.worker_rows:

				writer.writerow(row.__dict__)#update_dict) #{'first_name': 'Baked', 'last_name': 'Beans'})


	def verify_answer_correctness(self, img_fname, category):
		"""
		Using sentinels ("gold standard")

			Args:
			-	img_fname

			Returns:
			-	
		"""
		sentinel_idx = self.sentinel_fnames.index(img_fname)
		classname = self.sentinel_classnames[sentinel_idx]
		is_correct = category==classname
		return is_correct


	def count_multinomial_votes_csv(self) -> Tuple[ Mapping[str,str], Mapping[str,int] ]:
		"""

		Loop through each row of the CSV (each corresponding to a single HIT) and
		then loop through each of the 100 submitted answers. 

		Cannot use a default dict for times_seen, because "0" votes is not the 
		default, but rather very useful information (5 votes for and 0 votes against.)

		Discover classes from the csv on the fly.
		Keep a list of the associated classnames from each worker for 
		each image.

			Args:
			-	None

			Returns:
			-	imgurl_label_dict: Mapping[str,str]
			-	times_seen_dict: Mapping[str,int] ]
		"""
		imgurl_label_dict = defaultdict(list)
		times_seen_dict = {}

		for row_idx, row in enumerate(self.worker_rows):
			print(f'On row idx {row_idx}')
			# loop through each completed HIT (each row)
			if row.AssignmentStatus == 'Submitted':
				print('CSV decisions not complete!')
				quit()

			if row.AssignmentStatus != 'Approved':
				assert row.AssignmentStatus == 'Rejected'
				# Skip all of the rejected residual rows
				print('Skipping row since rejected')
				continue

			for i in range(NUM_IMGS_PER_HIT):
				key = f'Answer.choice_{i}'
				if key not in row.__dict__:
					print(f'\tMissing {key} ')
					continue
				category = getattr(row,key)
				img_url = getattr(row, f'Input.image_url_{i}')
				img_fname = Path(img_url).name

				imgurl_label_dict[img_url] += [category]

				if img_url not in times_seen_dict:
					times_seen_dict[img_url] = 0
				times_seen_dict[img_url] += 1

		return imgurl_label_dict, times_seen_dict


	def analyze_multinomial_worker_agreement(self):
		"""
			Analyze multinomial worker agreement. For those HITs that were approved, 
			make a list of assigned labels per URL. Also record the number of approved
			observations per 
			Take mode from approved, consider this the relabeled category.
			Record relabeled list for each (dataset, original_classname) tuple.

			Args:
			-	None

			Returns:
			-	None
		"""
		imgurl_label_dict, times_seen_dict = self.count_multinomial_votes_csv()
		
		plt.title('Num Repeats Per Img')
		plt.hist(list(times_seen_dict.values()), bins=6)
		plt.show()

		# Print out textual version of "times_seen" histogram stats
		# times_seen_arr = np.array(list(times_seen_dict.values()))
		# for i in range(MAX_NUM_WORKER_VOTES):
		# 	count = (times_seen_arr == i).sum()
		# 	if count != 0:
		# 		print(f'Saw {count} exactly {i} times')

		category_lists = defaultdict(list)

		print('Classifying re-labeled images by mode...')
		for i, (imgurl, classname_votes) in enumerate(imgurl_label_dict.items()):

			if i % 100 == 0:
				print(f'On img {i}')

			times_seen = times_seen_dict[imgurl]
			classname_mode, percent = most_frequent(classname_votes)

			if percent >= 80:
				dump_dirname = classname_mode + '_80percent_conf'
			else:
				print(f'\tLOW CONSENSUS {percent}')

			# elif percent >= 60 and percent < 80:
			# 	dump_dirname = classname_mode + '_60to80percent_conf'
			# 	print('LOW')
			# elif percent < 60:
			# 	dump_dirname = classname_mode + '_lessthan60percent_conf'
			# else:
			# 	print('Unknown error, quitting...')
			# 	quit()

			fname = Path(imgurl).name

			if fname in self.split_img_fnames:
				classname_mode = strip_forward_slash(classname_mode)
				self.save_img_classification(fname, classname_mode)
			
			if self.is_sentinel(fname):
				# We don't need consensus on these, since we have ground truth.
				continue
			category_lists[classname_mode] += [fname]
		
		# Also write the Sentinel classification to disk
		for (sentinel_fname, sentinel_classname) in self.hit_info.sentinels:
			sentinel_classname = strip_forward_slash(sentinel_classname)
			if sentinel_fname in self.split_img_fnames:
				assert self.hit_info.sentinel_img_dir == self.img_dir
				category_lists[sentinel_classname] += [sentinel_fname]

		# Sanity check -- ensure sum of total split imgs cardinality is correct.
		num_relabeled_split_imgs = sum([ len(cat_list) for classname,cat_list in category_lists.items() ])

		if num_relabeled_split_imgs != self.num_split_imgs:
			print(f'Found {self.num_split_imgs} imgs in split.')
			print(f'Found {num_relabeled_split_imgs} relabeled imgs.')
			print('Not all images relabeled yet. Cannot write final classifications yet.')
			return

		num_written_imgs = 0
		for classname, img_fnames in category_lists.items():
			save_fname = f'{hit_info.dataset_name}_{self.split}_{hit_info.task_nickname}_to_{classname}.txt'
			dirname = f'{hit_info.dataset_name}_{hit_info.task_nickname}'
			save_dir = f'mturk/verified_reclassification_files/{dirname}'
			check_mkdir(save_dir)
			save_fpath = f'{save_dir}/{save_fname}'
			write_txt_lines(save_fpath, img_fnames)

			num_written_imgs += len(read_txtfile_as_np(save_fpath))

		assert num_written_imgs == self.num_split_imgs
		print('# Written == # Read. Success.')


	def compare_csv_diff(self):
		"""
		Compare original row with modified row ("m_row")
		"""
		self.original_rows = self.read_csv_rows(self.csv_fpath)
		self.modified_rows = self.read_csv_rows(self.analyzed_csv_fpath)

		for row, m_row in zip(self.original_rows, self.modified_rows):
			assert row.__dict__.keys() == m_row.__dict__.keys()

			for k in row.__dict__.keys():
				if getattr(row,k) != getattr(m_row,k):
					print(f'Modified: {k}. {getattr(row,k)} -> {getattr(m_row,k)}')
