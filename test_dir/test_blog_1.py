# coding=utf-8
import pytest
import allure
from page.blog_page import BlogPage


@allure.feature('博客园首页')
class Test_Blogs_Page:
    '''博客园首页'''

    @allure.story('首页页面')
    def test_blog_page_case(self, browser, base_url):
        """
        名称：博客园首页页面测试
        步骤：
        1、打开博客园页面
        2、检查首页页面
        检查点：
        * 检查首页页面是否包含关键字。
        """
        bp = BlogPage(browser)
        bp.open(base_url)
        bp.get_display(bp.regist_element)
        assert browser.title == "博客园 - 开发者的网上家园"


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_blog_1.py"])
