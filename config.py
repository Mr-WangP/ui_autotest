#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wp
# @Time: 2021/5/26 18:24
# @File: config.py

import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))


class RunConfig:
    """
    运行测试配置
    """
    # 项目运行url
    uri = "https://www.cnblogs.com/"

    # 运行测试用例的目录或文件
    cases_path = os.path.join(BASE_PATH, "test_dir", "")
    # cases_path = os.path.join(PRO_PATH, "test_dir", "test_blog_login.py")

    # 配置浏览器驱动类型(chrome/firefox/chrome-headless/firefox-headless)。
    driver_type = "chrome"

    # 数据文件目录
    data_path = os.path.join(BASE_PATH, "data", "")

    # 报告文件目录
    report_path = os.path.join(BASE_PATH, "report", "")

    # 失败重跑次数
    rerun = "1"

    # 当达到最大失败数，停止执行
    max_fail = "5"

    # 浏览器驱动（不需要修改）
    driver = None
