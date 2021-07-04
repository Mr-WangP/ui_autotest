#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wp
# @Time: 2021/5/26 18:24
# @File: test_blog_1.py

import pytest
import allure
from page.blog_page import BlogPage


@allure.feature('博客园首页测试')
class Test_Blogs_Page:
    '''博客园首页'''

    @allure.story('首页页面显示测试')
    @pytest.mark.run(order=2)
    def test_blog_page_case1(self, browser, base_url):
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
            bp.open(base_url)
        with allure.step('等待首页页面显示'):
            bp.get_display(bp.regist_element)
        with allure.step('判断显示是否正确'):
            assert browser.title == "博客园 - 开发者的网上家园"

    @allure.story('首页页面显示错误测试')
    @pytest.mark.run(order=1)
    def test_blog_page_case2(self, browser, base_url):
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
            bp.open(base_url)
        with allure.step('等待首页页面显示'):
            bp.get_display(bp.regist_element)
        with allure.step('判断显示是否正确'):
            assert browser.title == "博客园1 - 开发者的网上家园"


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_blog_1.py"])
