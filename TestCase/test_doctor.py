#!/usr/bin/env python
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/3 23:12
# @Author  : 蒲天恩
# @File    : test_doctor.py
import unittest
from Common.http_request import HttpRequests
from ddt import ddt, data, unpack
from Common.do_excel import DoExcel
from Common.do_path import excel_path
from TestDate.doctor_data import *
import json
from Common.do_re import Context
from Common.do_log import load_my_logging_cfg
@ddt
class TestDoctor(unittest.TestCase):
    cases = DoExcel(excel_path).read_excel("doctor")

    @classmethod
    def setUpClass(cls):
        cls.hr = HttpRequests("api", "pre_url")
    @data(*cases)
    def test_doctor(self, case):
        load_my_logging_cfg("医师").info("case传入为：{}".format(case.data))
        if case.url == '/am/v2/doctor/syn':
            case.data = json.loads(case.data)
            doctorname = nameRandomGenerator()
            phone = phoneNORandomGenerator()
            uid = CreateIDCard()
            depart = department()
            doctortype = doctor_id_type()
            doctitle = doc_title()
            doccode = doc_title_code()
            case.data["body"]["doctorName"] = doctorname
            case.data["body"]["phone"] = phone
            case.data["body"]["doctorId"] = phone
            case.data["body"]["uid"] = uid
            case.data["body"]["department"] = depart
            case.data["body"]["doctorIdType"] = doctortype
            case.data["body"]["title"] = doctitle
            case.data["body"]["titleCode"] = doccode
            res = self.hr.http_request(case.method, case.url, data=case.data)
            # 日志
            print("响应", res)
            acture = res["message"]
            expect = case.expect
            self.assertEqual(expect, acture)
            setattr(Context, "openid", res["data"]["openId"])
        else:
            try:
                if hasattr(Context,"openid"):
                    openid = getattr(Context,"openid")
                    # 替换
                    case.data = json.loads(case.data)
                    load_my_logging_cfg("医师").info(f"当前传入的data：{case.data}")
                    case.data["openId"] = openid
                    load_my_logging_cfg("医师").info(f"当前传入的openid：{case.data['openId']}")
            except Exception as e:
                # 日志记录
                load_my_logging_cfg("医师").error(f"openid不存在")
            res = self.hr.http_request(case.method, case.url, data=case.data)
            load_my_logging_cfg("医师").info(f"返回的值是：{res}")
            acture = res["message"]
            expect = case.expect
            self.assertEqual(expect, acture)

    @classmethod
    def tearDownClass(cls):
        pass

