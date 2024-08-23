#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wp
# @Time: 2021/5/26 18:24
# @File: conftest.py

import time
from pathlib import Path
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.optionsUtils.browser_options import Browser_Options
from config import RunConfig
from utils.logUtils.logControl import log


# 启动浏览器
@pytest.fixture(scope='session', autouse=True)
def browser(request):
    """
    全局定义浏览器驱动
    :return:
    """
    global driver

    # 定义teardown函数
    # 函数建议末尾使用finalizer命名
    # def browser_finalizer():
    #     log().info("测试结束，关闭浏览器")
    #     driver.quit()
    #
    # # 将teardown函数进行注册
    # request.addfinalizer(browser_finalizer)

    # 定义setup部分
    # browser_type = {
    #     'Chrome': ['Chrome', 'chrome', 'gc', '谷歌浏览器'],
    #     'Edge': ['Edge', 'edge'],
    #     'Firefox': ['Firefox', 'firefox', 'fx', '火狐浏览器']
    # }
    # for key, value in browser_type.items():
    #     if RunConfig.driver_type in value:
    #         RunConfig.driver_type = key

    # 新版本selenium会先自动下载chromedriver，导致运行很慢
    # try:
    #     driver = getattr(webdriver, RunConfig.driver_type)()
    #     log().info("创建浏览器")
    # except:
    #     service = Service(r'D:\Python\chromedriver.exe')
    #     options = Browser_Options().chrome_options()
    #     driver = webdriver.Chrome(options=options,service=service)
    #     log().info("创建默认Chrome浏览器")

    service = Service(r'D:\Python\chromedriver.exe')
    options = Browser_Options().chrome_options()
    driver = webdriver.Chrome(options=options, service=service)
    log().info("创建默认Chrome浏览器")

    RunConfig.driver = driver
    yield driver
    log().info("测试结束，关闭浏览器")
    driver.quit()


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的 item 的 name 和 node_id 的中文显示在控制台上
    :param items:测试用例
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
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


def pytest_terminal_summary(terminalreporter):
    """
    收集测试结果
    """
    try:
        _PASSED = len([i for i in terminalreporter.stats.get('passed', []) if i.when != 'teardown'])
        _ERROR = len([i for i in terminalreporter.stats.get('error', []) if i.when != 'teardown'])
        _FAILED = len([i for i in terminalreporter.stats.get('failed', []) if i.when != 'teardown'])
        _SKIPPED = len([i for i in terminalreporter.stats.get('skipped', []) if i.when != 'teardown'])
        _XFAILED = len([i for i in terminalreporter.stats.get('xfailed', []) if i.when != 'teardown'])
        _XPASSED = len([i for i in terminalreporter.stats.get('xpassed', []) if i.when != 'teardown'])
        _TOTAL = terminalreporter._numcollected
        _TIMES = time.time() - terminalreporter._sessionstarttime

        log().info(f"成功用例数: {_PASSED}")
        log().error(f"异常用例数: {_ERROR}")
        log().error(f"失败用例数: {_FAILED}")
        log().warning(f"跳过用例数: {_SKIPPED}")
        log().warning(f"预期失败用例数: {_XFAILED}")
        log().warning(f"预期成功用例数: {_XPASSED}")
        log().info("用例执行时长: %.2f" % _TIMES + "s")

        _RATE = round(_PASSED / _TOTAL * 100, 2)
        log().info("用例成功率: %.2f" % _RATE + "%")
    except Exception as e:
        log().error("收集测试结果失败", e)
