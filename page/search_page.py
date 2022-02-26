#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : wp
# @Time : 2022/2/25 22:59
# @File : search_page.py

from selenium.webdriver.common.by import By
from base.base_page import BasePage
from config import RunConfig


class SearchPage(BasePage):

    # 页面url
    url = "https://zzk.cnblogs.com/"
    # 获取页面关联元素
    input_element = (By.ID, "w")
    search_button_element = (By.ID, "search_btn")
    result_element = (By.XPATH, '//*[@id="searchResult"]/div[2]/div[1]/h3/a')

    # 元素操作进行封装
    def search(self, args):
        # 进入搜索页面
        self.open(self.url)
        self.get_display(self.input_element)
        # '输入搜索文本内容'
        self.send_value(self.input_element, args['txt'])
        # '点击找一下按钮'
        self.click(self.search_button_element)
