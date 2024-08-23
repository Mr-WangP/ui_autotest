#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : wp
# @Time : 2022/3/19 15:14
# @File : browser_options.py

from selenium import webdriver
from config import RunConfig


# Browser_Options类的封装
class Browser_Options:

    def chrome_options(self):
        options = webdriver.ChromeOptions()
        # 默认启动的driver窗口最大化
        options.add_argument('--start-maximized')
        # 隐身模式
        options.add_argument('--incognito')
        # 添加无头指令
        # options.add_argument('--headless')
        # 禁用GPU加速
        options.add_argument('--disable-gpu')
        # 指定窗口大小
        # options.add_argument('--window-size=2000,4000')
        # 默认浏览器启动的坐标位置
        # options.add_argument('--window-position=200,400')
        # 去掉提示正在执行自动化的警告
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option('useAutomationExtension', False)
        prefs = {}
        # 去掉密码弹窗管理
        prefs["credentials_enable_service"] = False
        prefs["profile.password_manager_enabled"] = False
        # 修改下载文件路径
        prefs["profile.default_content_settings.popups"] = 0
        prefs["files.default_directory"] = str(RunConfig.download_path)
        options.add_experimental_option("prefs", prefs)
        # 页面加载策略：normal/eager/none
        options.page_load_strategy = 'eager'

        return options

    def edge_options(self):
        options = webdriver.EdgeOptions()
        options.use_chromium = True
        # 默认启动的driver窗口最大化
        options.add_argument('--start-maximized')
        # 隐身模式
        options.add_argument('--incognito')
        # 添加无头指令
        # options.add_argument('--headless')
        # 禁用GPU加速
        options.add_argument('--disable-gpu')
        # 指定窗口大小
        # options.add_argument('--window-size=2000,4000')
        # 默认浏览器启动的坐标位置
        # options.add_argument('--window-position=200,400')
        # 去掉提示正在执行自动化的警告
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option('useAutomationExtension', False)
        prefs = {}
        # 去掉密码弹窗管理
        prefs["credentials_enable_service"] = False
        prefs["profile.password_manager_enabled"] = False
        # 修改下载文件路径
        prefs["profile.default_content_settings.popups"] = 0
        prefs["files.default_directory"] = RunConfig.download_path
        options.add_experimental_option("prefs", prefs)
        # 页面加载策略
        options.page_load_strategy = 'eager'

        return options

    def firefox_options(self):
        options = webdriver.FirefoxOptions()
        # 默认启动的driver窗口最大化
        options.add_argument('--start-maximized')
        # 隐身模式
        options.add_argument('--incognito')
        # 添加无头指令
        # options.add_argument('--headless')
        # 禁用GPU加速
        options.add_argument('--disable-gpu')
        # 页面加载策略
        options.page_load_strategy = 'eager'

        return options

    def remote_options(self):
        options = webdriver.ChromeOptions()
        options.browser_name = 'chrome'
        # options = webdriver.EdgeOptions()
        # options.browser_name = 'MicrosoftEdge'
        options.browser_version = '125.0'
        options.platform_name = 'linux'
        options.javascript_enabled = True
        # 页面加载策略
        options.page_load_timeout = "eager"
        cloud_options = dict()
        cloud_options['build'] = "my_test_build"
        cloud_options['name'] = "my_test_name"
        options.set_capability('cloud:options', cloud_options)
