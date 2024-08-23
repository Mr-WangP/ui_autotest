#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wp
# @Time: 2021/5/26 18:24
# @File: config.py

from pathlib import Path
from utils.readFilesUtils.read_conf import ConfigUtil


class RunConfig:
    """
    运行测试配置
    """
    # 项目路径
    root_path = Path(__file__).resolve().parent

    # 项目运行url
    conf_path = Path(root_path, "common", "conf_env.ini")
    uri = ConfigUtil(conf_path).read_config('DEFAULTS', 'url')

    # 运行测试用例的目录或文件
    cases_path = Path(root_path, "test_dir")

    # 配置浏览器驱动类型(Chrome/Edge/Remote)。
    driver_type = "Chrome"

    # 数据文件目录
    data_path = Path(root_path, "data")

    util_path = Path(root_path, "utils")
    # 日志文件目录
    log_path = Path(root_path, "logs")

    # 报告文件目录
    report_path = Path(root_path, "report")

    # cookie保存文件
    cookies_path = Path(root_path, "cookies")

    # 上传、下载文件保存目录
    download_path = Path(root_path, "files")
    upload_path = Path(root_path, "files")
    # 失败重跑次数
    rerun = "1"

    # 当达到最大失败数，停止执行
    max_fail = "3"

    # 浏览器驱动（不需要修改）
    driver = None
