#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 - zihao.chen <zihao.chen@moji.com>
'''
Author: zihao.chen
Create Date: 2018-07-02
Modify Date: 2018-07-02
descirption: ""
'''
import os
import shutil
from config.config import *

test_path = '/home/meteo/zihao.chen/data/IEEE_ICDM_2018/download/SRAD2018_submit_sample_2018070414'
P_path = os.path.join(DATA_PATH,'extrapolate_flow_merge')
samples = os.listdir(test_path)

for sample in samples:
    temp_data_path = os.path.join(test_path,sample)
    temp_last_image_path = os.path.join(temp_data_path,sample+'_f006.png')
    if os.path.exists(temp_last_image_path):
        up_load_data_path = temp_data_path.replace('SRAD2018_submit_sample_2018070414','extrapolate_flow_merge')
        if not os.path.exists(up_load_data_path):
            os.makedirs(up_load_data_path)
        save_path = os.path.join(up_load_data_path,sample+'_f00%d.png'%(6))
        shutil.copy(temp_last_image_path,save_path)
