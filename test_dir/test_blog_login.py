#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wp
# @Time: 2021/5/26 18:24
# @File: test_blog_login.py

import pytest
import allure
from page.login_page import LoginPage
from data.yaml_util import YamlUtil
from config import RunConfig
from logs.log import log


@allure.feature('博客园登录功能测试')
class Test_Login_Blog:
    """博客园登录页"""

    @allure.story('错误用户登录测试')
    @pytest.mark.login
    @pytest.mark.parametrize('args', YamlUtil(RunConfig.data_path + '/login_file.yaml').read_yaml())
    def test_blog_login_case2(self, browser, args):
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
        with allure.step('进行登录操作'):
            lp.login(args)
        with allure.step('页面错误用户名或密码提示'):
            # 这里需要处理滑块验证
            txt = lp.get_display(lp.tips_error)
            assert txt is True
            log().info('✅ 断言成功：页面显示错误用户名或密码提示')


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_blog_login.py"])
