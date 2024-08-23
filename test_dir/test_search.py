#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : wp
# @Time : 2022/2/25 23:10
# @File : test_search.py

from pathlib import Path
import pytest
import allure
from page.search_page import SearchPage
from config import RunConfig
from utils.logUtils.logControl import log
from utils.readFilesUtils.yaml_util import YamlUtil


@allure.feature('百度搜索功能测试')
class Test_Search_Blog:
    """百度搜索"""

    @allure.story('搜索测试')
    @pytest.mark.search
    @pytest.mark.parametrize('args', YamlUtil(Path(RunConfig.data_path, "search_file.yaml")).read_yaml())
    def test_search(self, browser, args):
        """
        名称：百度搜索测试
        步骤：
        1、打开百度搜索页面
        2、输入搜索文本
        5、点击搜索按钮
        检查点：
        * 检查是否进行搜索。
        """
        sp = SearchPage(browser)
        with allure.step('进行搜索操作'):
            sp.search(args)
        with allure.step('检查搜索结果'):
            sp.wait(2)
            assert sp.get_title() == args["txt"] + "_百度搜索"
            log().info('✅ 断言成功：成功搜索{}'.format(args["txt"]))


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_search.py"])
