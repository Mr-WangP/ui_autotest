#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wp
# @Time: 2021/5/26 18:24
# @File: test_blog_home.py

import pytest
import allure
from page.blog_page import BlogPage
from logs.log import log


@allure.feature('博客园首页测试')
class Test_Home_Blog:
    """博客园首页"""

    @allure.story('首页页面显示测试')
    @pytest.mark.home
    @pytest.mark.run(order=2)
    def test_blog_page_case1(self, browser):
        """
        名称：博客园首页页面测试
        步骤：
        1、打开博客园页面
        2、检查首页页面
        检查点：
        * 检查首页页面是否包含关键字。
        """
        bp = BlogPage(browser)
        with allure.step('打开url'):
            bp.open(bp.url)
        with allure.step('等待首页页面显示'):
            bp.get_display(bp.regist_element)
        with allure.step('判断显示是否正确'):
            title = browser.title
            assert title == "博客园 - 开发者的网上家园"
            log().info('✅ 断言成功：{} == "博客园 - 开发者的网上家园"'.format(title))

    @allure.story('首页页面显示错误测试')
    @pytest.mark.home
    @pytest.mark.xfail(condition=True, reason='标记为预期失败')
    @pytest.mark.run(order=1)
    def test_blog_page_case2(self, browser):
        """
        名称：博客园首页页面测试
        步骤：
        1、打开博客园页面
        2、检查首页页面
        检查点：
        * 检查首页页面是否包含关键字。
        """
        bp = BlogPage(browser)
        with allure.step('打开url'):
            print(bp.url)
            bp.open(bp.url)
        with allure.step('等待首页页面显示'):
            bp.get_display(bp.regist_element)
        with allure.step('判断显示是否正确'):
            title = browser.title
            assert title == "博客园1 - 开发者的网上家园"
            log().info('✅ 断言成功：{} == "博客园1 - 开发者的网上家园"'.format(title))


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_blog_home.py"])
