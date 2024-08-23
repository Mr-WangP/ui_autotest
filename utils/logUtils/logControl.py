#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : wp
# @Time : 2022/2/25 16:25
# @File : logs.py

import logging
import pathlib

import colorlog
from config import RunConfig
from pathlib import Path
import time


def log():

    # 创建日志器
    logger = logging.getLogger('logger')
    # 设置日志输出最低等级，低于当前等级就会忽略
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        # 创建处理器
        sh = logging.StreamHandler()
        fh = logging.FileHandler(
            filename='{0}_{1}'.format(
                str(Path(RunConfig.log_path, "log")),
                time.strftime(
                    '%Y_%m_%d_%H_%M_%S',
                    time.localtime())),
            encoding='utf-8')
        # 创建一个格式器
        log_colors_config = {
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red'
        }
        sh_formatter = colorlog.ColoredFormatter(
            '%(log_color)s[%(asctime)s] [%(filename)s] [%(funcName)s] [%(levelname)s]: %(message)s',
            log_colors=log_colors_config)
        fh_formatter = logging.Formatter(
            fmt='%(asctime)s %(filename)s %(funcName)s %(levelname)s %(message)s',
            datefmt='%Y-%m-%d-%X')
        sh.setFormatter(sh_formatter)
        fh.setFormatter(fh_formatter)
        logger.addHandler(sh)
        logger.addHandler(fh)

    return logger

def getLogger():
    # 配置文件的路径
    # file = './log_conf.ini'
    file_path = pathlib.Path(__file__).parents[0].resolve() / 'log_conf.ini'

    logging.config.fileConfig(file_path, encoding='utf-8')
    logger = logging.getLogger() #获取日志记录器
    return logger
