# coding=utf-8
import pytest
import allure
from page.login_page import LoginPage
from test_dir.yaml_util import YamlUtil
import os
from selenium.webdriver.common.by import By


@allure.feature('博客园登录页')
class Test_Login_Blog:
    '''博客园登录页'''

    @allure.story('登录测试1')
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
        lp.open(base_url)
        lp.get_display(lp.login_element)
        # 进入登录页
        lp.click(lp.login_element)
        lp.get_display(lp.login_title_element)
        assert browser.title == "用户登录 - 博客园"

    @allure.story('登录测试2')
    def test_blog_login_case2(self, browser, base_url):
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
        lp.open(base_url)
        lp.get_display(lp.login_element)
        # 进入登录页
        lp.click(lp.login_element)
        lp.get_display(lp.login_title_element)
        assert browser.title == "用户登录 - 博客园1"

    @allure.story('登录测试3')
    @pytest.mark.parametrize('args', YamlUtil(os.getcwd() + '/data/data_file.yaml').read_yaml())
    def test_blog_login_case3(self, browser, base_url, args):
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
        lp.open(base_url)
        lp.get_display(lp.login_element)
        # 进入登录页
        lp.click(lp.login_element)
        lp.get_display(lp.login_title_element)
        # 进行登录
        lp.send_value(lp.name_element, args['name'])
        lp.send_value(lp.password_element, args['password'])
        lp.click(lp.denglu_button)
        error_element = lp.get_element((By.XPATH, '//*[text()="用户名或密码错误"]'))

        assert lp.get_display(error_element) is True


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_blog_2.py"])
