# coding=utf-8
import os
import time
from conftest import log
import pytest
from config import RunConfig

'''
说明：
1、用例创建原则，测试文件名必须以“test”开头，测试函数必须以“test”开头。
2、运行方式：
  > python run_tests.py
'''

def run():
    log().info("测试开始执行！")
    # now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
    # RunConfig.NEW_REPORT = os.path.join(REPORT_DIR, now_time)

    pytest.main(["-v", RunConfig.cases_path,
                 "--alluredir", './temp/',
                 "--clean-alluredir",
                 "--maxfail", RunConfig.max_fail,
                 "--reruns", RunConfig.rerun,
                 "--reruns-delay", "2"])

    os.system('allure generate ./temp/ -o ./report/ --clean')
    log().info("运行结束，生成测试报告！")


if __name__ == '__main__':
    run()
