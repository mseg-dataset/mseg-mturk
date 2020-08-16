
This repo contains the **Amazon Mechanical Turk workflow scripts** for the paper:

**MSeg: A Composite Dataset for Multi-domain Semantic Segmentation** (CVPR 2020, Official Repo) [[PDF]](http://vladlen.info/papers/MSeg.pdf)
<br>
[John Lambert*](https://johnwlambert.github.io/),
[Zhuang Liu*](https://liuzhuang13.github.io/),
[Ozan Sener](http://ozansener.net/),
[James Hays](https://www.cc.gatech.edu/~hays/),
[Vladlen Koltun](http://vladlen.info/)
<br>
Presented at [CVPR 2020](http://cvpr2020.thecvf.com/).  Link to [MSeg Video (3min) ](https://youtu.be/PzBK6K5gyyo)

This repo is the fourth of 4 repos that introduce our work. It provides utilities to perform large-scale Mechanical Turk re-labeling.
- [` mseg-api`](https://github.com/mseg-dataset/mseg-api): utilities to download the MSeg dataset, prepare the data on disk in a unified taxonomy, on-the-fly mapping to a unified taxonomy during training.
- [`mseg-semantic`](https://github.com/mseg-dataset/mseg-semantic): provides HRNet-W48 pre-trained models and training code (sufficient to train a winning entry on the [WildDash](https://wilddash.cc/benchmark/summary_tbl?hc=semantic_rob) benchmark)

One additional repos will be introduced in April and May 2020:
- `mseg-panoptic`: provides Panoptic-FPN and Mask-RCNN training, based on Detectron2

<p align="left">
  <img src="https://user-images.githubusercontent.com/62491525/83895683-094caa00-a721-11ea-8905-2183df60bc4f.gif" height="215">
  <img src="https://user-images.githubusercontent.com/62491525/83893966-aeb24e80-a71e-11ea-84cc-80e591f91ec0.gif" height="215">
</p>
<p align="left">
  <img src="https://user-images.githubusercontent.com/62491525/83895915-57fa4400-a721-11ea-8fa9-3c2ff0361080.gif" height="215">
  <img src="https://user-images.githubusercontent.com/62491525/83895972-73654f00-a721-11ea-8438-7bd43b695355.gif" height="215"> 
</p>

<p align="left">
  <img src="https://user-images.githubusercontent.com/62491525/83893958-abb75e00-a71e-11ea-978c-ab4080b4e718.gif" height="215">
  <img src="https://user-images.githubusercontent.com/62491525/83895490-c094f100-a720-11ea-9f85-cf4c6b030e73.gif" height="215">
</p>

<p align="left">
  <img src="https://user-images.githubusercontent.com/62491525/83895811-35682b00-a721-11ea-9641-38e3b2c1ad0e.gif" height="215">
  <img src="https://user-images.githubusercontent.com/62491525/83896026-8710b580-a721-11ea-86d2-a0fff9c6e26e.gif" height="215">
</p>


### Dependencies

Install the `mseg` module from [`mseg-api`](https://github.com/mseg-dataset/mseg-api).

### Install the MSeg-mturk module:

* `mseg_mturk` can be installed as a python package using

        pip install -e /path_to_root_directory_of_the_repo/

Make sure that you can run `import mseg_mturk` in python, and you are good to go!


## Repo Contents
This repository contains the following items:

-	`mseg_mturk`: Python module with HIT publishing + evaluation scripts
-	`hit_html`: auto-populated HTML to render HIT UI page 
-	`image_elements`: auto-populated HTML element for each mask
-	`instruction_files`: auto-populated instruction HTML pages for workers
-	`template_html`: template HTML code that is used to auto-populate HIT specifications
-	`tests`: unit tests

## Work Statistics

- Total time spent relabeling: 1.34 years of uninterrupted work. 

Most time-intensive tasks:
- 106 days (~3.5 months) COCO "person", 
- 87 days (~3 months) for IDD "rider",
- 20 days for COCO "table,
- 19 days for COCO "chair", 
- 19 days for COCO "counter".
- ...

## Workflow Overview

We design a careful workflow to ensure a high quality bar for annotations submitted by Mechanical Turk workers.

Our re-labeling workflow proceeds in 6 main stages:

	(1) Hand-classify sentinels, and create BatchResult class with SentinelHIT specification.
	(2) Run `mseg_mturk/publish_tasks.py` to generate HIT html, HIT csv, and instructions html.
	(2) Submit HIT on AMT.
	(2) Analyze accuracy of each submitted HIT using `mseg_mturk/eval_result.py`. 
		For each one, for all 100 images, check if sentinel.
		If it is a sentinel, check correctness. Compute mean accuracy per HIT.
		Set status in WorkerHITResult for each HIT to 'Approved' or 'Rejected'
		based on 100% accuracy cutoff.

	(3) Enter WorkerHITResult decisions into 'analyzed' version of csv. Upload analyzed csv to MTurk, and re-assign rejected jobs.
	(4) Analyze multinomial worker agreement. For those HITs that were approved, 
		make a list of assigned labels per URL. Also record the number of approved
		observations per image.
	(5) Take mode from approved, consider this the relabeled category.
	(6) Record relabeled list for each (dataset, original_classname) tuple.


## Class Examplar Images

Via Google Drive, we provide access to the class examplar images we provided to MTurk annotators in their instructions: [animals](https://drive.google.com/open?id=1o1sTZKEYwPmgLHR7Jh12khuEDcNVBCob), [rug vs. carpet](https://drive.google.com/drive/folders/1ulOaibRjqN5-qO11xpRwgVxsagi97IuS?usp=sharing), [cabinet, nightstand, desk, chest-of-drawers, wardrobe](https://drive.google.com/drive/folders/1asUB3zsvJAQ2_vmEF9LCjJizY7EimcVO?usp=sharing), [curtain vs. shower curtain](https://drive.google.com/open?id=1OyVAy-g9WCLUBFhgrJGDrYapISuLZOZX), [mountain vs. hill vs. snow](https://drive.google.com/open?id=11QnCNJVmdmMUejVh1IntdSyhMB-MSjWJ), [fence vs. guardrail](https://drive.google.com/open?id=1gl3HKs8txBnJ4l6wDlNuUnXjxzc-J52o), and [all other shattered classes](https://drive.google.com/open?id=1LLm0T8sB-jM4RBy_t4P1CM36imTycaul).

## Example MTurk UI
<p align="center">
  <img src="https://user-images.githubusercontent.com/16724970/85213302-8c2d5180-b32a-11ea-9cd0-e298d0897918.png" width="950">
  <img src="https://user-images.githubusercontent.com/16724970/85213174-c85fb280-b328-11ea-9261-6e860abc48c6.png" width="860">
  <img src="https://user-images.githubusercontent.com/16724970/85214862-c43e8f80-b33e-11ea-9610-b35ede449f40.jpeg" width=860">
</p>

## Citing MSeg

If you find this code useful for your research, please cite:
```
@InProceedings{MSeg_2020_CVPR,
author = {Lambert, John and Zhuang, Liu and Sener, Ozan and Hays, James and Koltun, Vladlen},
title = {{MSeg}: A Composite Dataset for Multi-domain Semantic Segmentation},
booktitle = {Computer Vision and Pattern Recognition (CVPR)},
year = {2020}
}
```

## Acknowledgements

Many thanks to Qifeng Chen for his [base AMT workflow](https://github.com/CQFIO/PhotographicImageSynthesis/tree/master/mturk_scripts), which he shared with us. We are also grateful to the Amazon Mechanical Turk workers who completed 1.34 years of uninterrupted annotation to make MSeg happen!
