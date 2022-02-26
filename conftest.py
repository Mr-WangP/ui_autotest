#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wp
# @Time: 2021/5/26 18:24
# @File: conftest.py

import os
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as CH_Options
from selenium.webdriver.firefox.options import Options as FF_Options
from config import RunConfig


# 启动浏览器
@pytest.fixture(scope='session', autouse=True)
def browser():
    """
    全局定义浏览器驱动
    :return:
    """
    global driver

    # try:
    #     if RunConfig.driver_type == "chrome":
    #         # 添加log
    #         driver = webdriver.Chrome(options=chrome_options)
    #     else:
    #         # 添加log
    #         driver = getattr(webdriver, RunConfig.driver_type)()
    # except Exception as e:
    #     # 添加log
    #     print(e)
    #     driver = webdriver.Chrome()
    # return driver

    if RunConfig.driver_type == "chrome":
        # 本地chrome浏览器
        driver = webdriver.Chrome()
        driver.maximize_window()

    elif RunConfig.driver_type == "firefox":
        # 本地firefox浏览器
        driver = webdriver.Firefox()
        driver.maximize_window()

    elif RunConfig.driver_type == "chrome-headless":
        # chrome headless模式
        chrome_options = CH_Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(options=chrome_options)

    elif RunConfig.driver_type == "firefox-headless":
        # firefox headless模式
        firefox_options = FF_Options()
        firefox_options.headless = True
        driver = webdriver.Firefox(firefox_options=firefox_options)

    elif RunConfig.driver_type == "grid":
        # 通过远程节点分布式运行
        caps = {
            "browserName": "chrome",
            "version": "",
            "platform": "WINDOWS"
        }
        driver = webdriver.Remote('http://localhost:4444/wd/hub', caps)
        driver.set_window_size(1920, 1080)

    else:
        raise NameError("driver驱动类型定义错误！")

    RunConfig.driver = driver

    return driver


# 关闭浏览器
@pytest.fixture(scope="session", autouse=True)
def browser_close():
    yield driver
    driver.quit()
    print("test end!")


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    失败用例截图
    :param item:测试用例
    :return:
    """
    outcome = yield
    report = outcome.get_result()
    # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            with allure.step('添加失败截图...'):
                allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)

    # if rep.when == "call" and rep.failed:
    #     mode = "a" if os.path.exists("failures") else "w"
    #     with open("failures", mode) as f:
    #         if "tmpdir" in item.fixturenames:
    #             extra = " (%s)" % item.funcargs["tmpdir"]
    #         else:
    #             extra = ""
    #         f.write(rep.nodeid + extra + "\n")
    #     with allure.step('添加失败截图...'):
    #         allure.attach(
    #             driver.get_screenshot_as_png(),
    #             "失败截图",
    #             allure.attachment_type.PNG)
