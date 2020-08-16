#!/usr/bin/python3

from pathlib import Path
from mseg_mturk.hit_utils import (
	most_frequent,
	read_txtfile_as_np,
	WorkerHITResult
)

_ROOT = Path(__file__).resolve().parent



def test_WorkerHITResult():
	"""
	"""
	test_dict = {
		'WorkerID': 123,
		'HITID': 456,
		'AssignmentStatus': 'submitted'
	}
	whr = WorkerHITResult(test_dict)

	for k,v in test_dict.items():
		assert v == getattr(whr, k)

	assert len(whr.__dict__.keys()) == len(test_dict.keys())


def test_most_frequent1():
	""" """
	x = ['cat', 'dog', 'puppy', 'cat']
	y, percent = most_frequent(x)
	assert y == 'cat'
	assert percent == 50

def test_most_frequent2():
	""" """
	x = ['dog', 'dog', 'dog', 'dog']
	y, percent = most_frequent(x)
	assert y == 'dog'
	assert percent == 100

def test_most_frequent3():
	""" """
	x = [1,2,3,4,3]
	y, percent = most_frequent(x)
	assert y == 3
	assert percent == 40


def test_read_txtfile_as_np1():
	""" """
	fpath = f'{_ROOT}/test_data/image_ids_3line_noblank.txt'
	str_list = read_txtfile_as_np(fpath)
	assert(len(str_list)) == 3
	gt_str_list = ['image1.png','image2.png','image3.png']
	assert str_list == gt_str_list


def test_read_txtfile_as_np2():
	""" """
	fpath = f'{_ROOT}/test_data/image_ids_1line_1blank.txt'
	str_list = read_txtfile_as_np(fpath)
	assert(len(str_list)) == 1
	gt_str_list = ['image2.png']
	assert str_list == gt_str_list


def test_read_txtfile_as_np3():
	""" """
	fpath = f'{_ROOT}/test_data/image_ids_1line_noblank.txt'
	str_list = read_txtfile_as_np(fpath)
	assert(len(str_list)) == 1
	gt_str_list = ['image1.png']
	assert str_list == gt_str_list


if __name__ == '__main__':
	# test_most_frequent1()
	# test_most_frequent2()
	# test_most_frequent3()

	# test_read_txtfile_as_np1()
	# test_read_txtfile_as_np2()
	# test_read_txtfile_as_np3()
	test_WorkerHITResult()


