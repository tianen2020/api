#!/usr/bin/env python
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/12 19:04
# @Author  : 蒲天恩
# @File    : do_re.py
import re
from Common.do_config import DoConfig
class Context:
    openid = None

# def dore_replace(data):
#     p ="#(.*?)#"
#     while re.search(p,data):
#         m = re.search(p,data)
#         s = m.group(1)
#         # 读取随机数据或者配置文件进行替换
#         # 根据 s 去配置文件读key 来获取value，再把value进行替换
#         data = re.sub(p,v,data,count=1)
#     return data