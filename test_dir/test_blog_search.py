#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : wp
# @Time : 2022/2/25 23:10
# @File : test_blog_search.py

import pytest
import allure
from page.search_page import SearchPage
from data.yaml_util import YamlUtil
from config import RunConfig
from logs.log import log


@allure.feature('博客园搜索功能测试')
class Test_Search_Blog:
    """博客园搜索页"""

    @allure.story('搜索测试')
    @pytest.mark.search
    @pytest.mark.parametrize('args', YamlUtil(RunConfig.data_path + '/search_file.yaml').read_yaml())
    def test_blog_login_case2(self, browser, args):
        """
        名称：博客园搜索测试
        步骤：
        1、打开博客园搜索页面
        2、输入搜索文本
        5、点击搜索按钮
        检查点：
        * 检查是否进行搜索。
        """
        sp = SearchPage(browser)
        with allure.step('进行搜索操作'):
            sp.search(args)
        with allure.step('检查搜索结果'):
            text = sp.get_text(sp.result_element)
            assert args["txt"] in text
            log().info('✅ 断言成功：成功搜索{}'.format(text))


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_blog_search.py"])
