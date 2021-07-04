# coding=utf-8
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class LoginPage(BasePage):

    # 获取关联元素
    login_element = (By.XPATH, "//*[@id='navbar_login_status']/a[5]")

    login_title_element = (By.XPATH, "//div[text()='博客园用户登录']")

    name_element = (By.XPATH, "//*[@id='mat-input-0']")
    password_element = (By.XPATH, "//*[@id='mat-input-1']")

    denglu_button = (By.XPATH, "//*[@fxlayout='column']/button")

    tips_error = (By.XPATH, '//*[text()="用户名或密码错误"]')

    # 元素操作进行封装
