#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 2022-07-15 11:38
IMAGE_H = 288
IMAGE_W = 512
MEAN = (0.485, 0.456, 0.406)
STD = (0.229, 0.224, 0.225)

ORIG_IMAGE_H = 720
ORIG_IMAGE_W = 1280
SEG_WIDTH = 10

DATA_PATH = "/data/datasets/tusimple"

EPOCH = 5
BATCH = 32
LR = 1e-3
MAX_LR = 5e-1
