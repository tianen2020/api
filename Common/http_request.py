#!/usr/bin/env python
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/3 23:10
# @Author  : 蒲天恩
# @File    : http_request.py
import requests
import json
from Common.do_config import DoConfig
class HttpRequests:
    def __init__(self,option,section):
        self.s = requests.Session()
        self.url = DoConfig().get_Strvalue(option,section)
    def http_request(self, method, url, params=None, data=None):

        method = method.upper()
        if type(data) == str:
            data = json.loads(data)
        url = self.url + url
        if method == "GET":
            # 发送get请求
            res = self.s.get(url=url, params=params, verify=False)
            return res.json()
        elif method == "POST":
            # 发送post请求
            res = self.s.post(url=url, json=data, verify=False)
            return res.json()
        else:
            # 日志提示输入的不请求方式不正确
            print(f'输入不正确的请求方式为：{method}')

