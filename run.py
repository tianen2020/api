
import unittest
from Common.do_path import testcase_path
from Common.do_path import report_path
import HTMLTestRunner

discover = unittest.defaultTestLoader.discover(start_dir=testcase_path, pattern="test_*.py")
with open(report_path,mode ="wb") as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream =file,
                                           description='接口测试',
                                           title="自动化测试")
    runner.run(discover)