#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wp
# @Time: 2021/6/26 18:24
# @File: login_page.py
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from config import RunConfig


class LoginPage(BasePage):

    # 页面url
    url = "https://account.cnblogs.com/"
    # 获取关联元素
    login_title_element = (By.XPATH, "//app-sign-in-up-page-title/h1")
    name_element = (By.XPATH, "//*[@id='mat-input-0']")
    password_element = (By.XPATH, "//*[@id='mat-input-1']")
    denglu_button = (By.XPATH, "//*[@fxlayout='column']/button")
    tips_error = (By.XPATH, '//*[text()="用户名或密码错误"]')

    # 元素操作进行封装
    def login(self, args):
        # 进入登录页面
        self.open(self.url)
        self.get_display(self.login_title_element)
        # '输入用户名'
        self.send_value(self.name_element, args['name'])
        # '输入用户密码'
        self.send_value(self.password_element, args['password'])
        # '点击登录'
        self.click(self.denglu_button)
