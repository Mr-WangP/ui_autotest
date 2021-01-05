# coding=utf-8
import sys
from time import sleep
import pytest
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.blog_page import BlogPage


class TestBlogs:
    '''博客园首页'''

    def test_blog_login_case(self, browser, base_url):
        """
        名称：博客园登陆测试
        步骤：
        1、打开博客园页面
        2、点击登录
        3、输入用户名、密码登录
        检查点：
        * 检查页面标题是否包含关键字。
        """
        page = BlogPage(browser)
        page.get(base_url)
        page.regist_element.is_displayed()
        page.login_element.click()
        # page.search_button.click()
        sleep(2)
        assert browser.title == "用户登录 - 博客园1"


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_blogs.py"])
