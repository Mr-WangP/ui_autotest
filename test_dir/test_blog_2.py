#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wp
# @Time: 2021/5/26 18:24
# @File: test_blog_2.py

import os
import pytest
import allure
from page.login_page import LoginPage
from test_dir.yaml_util import YamlUtil

PRO_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@allure.feature('博客园登录功能测试')
class Test_Login_Blog:
    '''博客园登录页'''

    @allure.story('登录页面测试')
    def test_blog_login_case(self, browser, base_url):
        """
        名称：博客园登陆测试
        步骤：
        1、打开博客园页面
        2、点击登录
        3、打开登录页面
        检查点：
        * 检查登录页面标题是否包含关键字。
        """
        lp = LoginPage(browser)
        with allure.step('打开url'):
            lp.open(base_url)
        with allure.step('等待首页页面显示'):
            lp.get_display(lp.login_element)
        with allure.step('进入登录页面'):
            lp.click(lp.login_element)
        with allure.step('等待登录页面显示'):
            lp.get_display(lp.login_title_element)
        with allure.step('判断是否正确进入登录页面'):
            assert browser.title == "用户登录 - 博客园"

    @allure.story('登录测试')
    @pytest.mark.parametrize('args', YamlUtil(PRO_PATH + '/data/data_file.yaml').read_yaml())
    @pytest.mark.skip
    def test_blog_login_case2(self, browser, base_url, args):
        """
        名称：博客园登陆测试
        步骤：
        1、打开博客园页面
        2、点击登录
        3、打开登录页面
        4、输入用户名和密码
        5、点击登录
        检查点：
        * 检查是否错误用户名密码导致登录失败。
        """
        lp = LoginPage(browser)
        with allure.step('打开url'):
            lp.open(base_url)
        with allure.step('等待首页页面显示'):
            lp.get_display(lp.login_element)
        with allure.step('进入登录页面'):
            lp.click(lp.login_element)
        with allure.step('等待登录页面显示'):
            lp.get_display(lp.login_title_element)
        with allure.step('输入用户名'):
            lp.send_value(lp.name_element, args['name'])
        with allure.step('输入用户密码'):
            lp.send_value(lp.password_element, args['password'])
        with allure.step('点击登录'):
            lp.click(lp.denglu_button)
        with allure.step('页面错误用户名或密码提示'):
            # 这里需要处理滑块验证（未完成）
            assert lp.get_display(lp.tips_error) is True


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_blog_2.py"])
