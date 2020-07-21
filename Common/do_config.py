#!/usr/bin/env python
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/5 19:53
# @Author  : 蒲天恩
# @File    : do_config.py
from configparser import ConfigParser
from Common import do_path
class DoConfig:
    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read(do_path.global_path)
        switch = self.cf.getboolean("switch", "on")
        if switch:
            # 读测试环境
            self.cf.read(do_path.beta_path)
        else:
            # 读集成环境
            self.cf.read(do_path.test_path)
    # 读取整数
    def get_Intvalue(self, section, option):
        return self.cf.getint(section,option)
    # 读取字符串
    def get_Strvalue(self, section, option):
        return self.cf.get(section, option)
    # 读取所有的section
    def get_section(self):
        return self.cf.sections()
    # 读取所有的option
    def get_option(self):
        return self.cf.options()
    # 读取布尔值
    def get_boolean(self,section, option):
        return self.cf.getboolean(section, option)
