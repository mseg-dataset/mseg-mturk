#!/usr/bin/python3

from collections import Counter
import datetime
import numpy as np
from typing import Any, List, Mapping, Tuple


class WorkerHITResult:
	def __init__(self, row_dict: Mapping[str,Any]):
		"""
			Args:
			-	row_dict: dictionary representing a single row
					from a CSV Reader.

			Returns:
			-	None
		"""
		for k,v in row_dict.items():
			setattr(self, k, v)


def generate_datetime_string() -> str:
    """Generate a formatted datetime string.
    Returns:
        String with of the format YYYY_MM_DD_HH_MM_SS with 24-hour time used
    """
    return f"{datetime.datetime.now():%Y_%m_%d_%H_%M_%S}"


def read_txt_file(fpath):
	""" """
	with open(fpath, 'r') as f:
		return f.readlines()


def strip_forward_slash(category):
	""" """
	if '/' in category:
		# extra forward slash will screw up the filename
		category = category.replace('/', '_')
	return category


def most_frequent(x: List[Any]) -> Tuple[str,float]: 
	""" 
		Returns percent as x%, instead of decimal

		Args:
		-	x

		Returns:
		-	val
		-	percent, floating point number in range [0,100]
	"""
	num_items = len(x)
	occurence_count = Counter(x) 
	val, count = occurence_count.most_common(1)[0]
	percent = (count / num_items) * 100
	return val, percent


def read_txtfile_as_np(fpath):	
	"""
		Args:
		-	
		Returns:
		-	
	"""
	np_str_arr = np.genfromtxt(fpath, delimiter='\n', dtype=str)

	if np_str_arr.size == 1:
		return [str(np_str_arr)]
	else:
		return list(np_str_arr)
