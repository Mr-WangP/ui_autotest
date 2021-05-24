# coding=utf-8
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class BlogPage(BasePage):

    # 获取关联元素
    login_element = (By.XPATH, "//*[@id='navbar_login_status']/a[5]")
    regist_element = (By.XPATH, "//*[@id='navbar_login_status']/a[4]")
    home_element = (By.XPATH, "//*[@id='nav_left']/li[2]/a")
    news_element = (By.XPATH, "//*[@id='nav_left']/li[3]/a")
    # ...
    # find_element = (By.XPATH, "//*[@id='nav_left']/li[9]/div[1]/a")
    yuanzi_element = (By.XPATH, "//*[@id='nav_left']/li[9]/div[2]/a[1]")
    shoucang_element = (By.XPATH, "//*[@id='nav_left']/li[9]/div[2]/a[3]")
    # ...
    jinghua_element = (By.XPATH, "//*[@id='sidenav_pick']/a/span")
    dingyue_element = (By.XPATH, "//*[@id='sidenav_subscription']/a/span")
    more_element = (By.XPATH, "//*[@id='sidenav_more']/div[1]/a/span")
    all_blogs_element = (By.XPATH, "//*[@id='sidenav_more']/div[2]/a[1]")

    # 元素操作进行封装
