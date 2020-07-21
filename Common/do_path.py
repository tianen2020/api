#!/usr/bin/env python
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/4 21:31
# @Author  : 蒲天恩
# @File    : do_path.py

import os
# 顶层目录
base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# data 目录
data_path = os.path.join(base_path,"TestDate")
# 打开配置文件
config_path = os.path.join(base_path,"Config")
# excel
excel_path = os.path.join(base_path, "TestDate", "szyx_api.xlsx")
# global 全局
global_path = os.path.join(base_path, "Config", "global.cfg")
# beta
beta_path = os.path.join(base_path, "Config", "beta.cfg")
# test
test_path = os.path.join(base_path, "Config", "test.ini")


