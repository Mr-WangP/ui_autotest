#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wp
# @Time: 2021/5/26 18:24
# @File: run_tests.py

import os
import pytest
from config import RunConfig
from logs.log import log

'''
说明：
1、用例创建原则，测试文件名必须以“test”开头，测试函数必须以“test”开头。
2、运行方式：
  > python run_tests.py
'''


def run():

    log().info("测试开始执行！")
    pytest.main(["-vs", RunConfig.cases_path,
                 "--alluredir", './temp/',
                 "--clean-alluredir",
                 "--maxfail", RunConfig.max_fail,
                 "--reruns", RunConfig.rerun,
                 "--reruns-delay", "2"])

    os.system('allure generate ./temp/ -o ./report/ --clean')
    log().info("运行结束，生成测试报告！")


if __name__ == '__main__':
    run()
