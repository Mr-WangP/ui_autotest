#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wp
# @Time: 2021/5/26 18:24
# @File: base_page.py

"""
此文件为selenium常用方法二次封装文件
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from logs.log import log


class BasePage(object):
    """
    selenium框架的主要类
    """

    # 初始化基础类
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def open(self, url):
        """
        打开url
        :param url:
        :return:
        """
        try:
            self.driver.get(url)
            log().info("✅ 打开url：{}".format(url))
        except Exception as e:
            log().error("❌ 打开url：{}失败".format(url))
            return e

    def get_url(self):
        """
        获取当前页面的URL地址.
        :return:
        """
        try:
            current_url = self.driver.current_url
            log().info("✅ 获取当前页面url为：{}".format(self.driver.current_url))
            return current_url
        except Exception as e:
            log().error("❌ 获取当前页面url失败")
            return e

    def get_element(self, loc, timeout=10):
        """
        显示等待，并判断元素定位方式，并返回元素对象
        :param loc: 元素定位
        :param timeout: 超时时间
        :return:
        """
        try:
            el = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_element(*loc))
            log().info("✅ 查找到元素：{by}={value} ".format(by=loc[0], value=loc[1]))
            return el
        except Exception as e:
            error_msg = "❌ 查找不到元素: {by}={value} ".format(by=loc[0], value=loc[1])
            log().error(error_msg)
            return e

    def max_window(self):
        """
        设置浏览器最大化.
        """
        self.driver.maximize_window()
        log().info("✅ 最大化浏览器")

    def set_window(self, wide, high):
        """
        设置浏览器窗口宽和高.
        """
        self.driver.set_window_size(wide, high)
        log().info("✅ 设置浏览器宽高为：{}×{} ".format(wide, high))

    def clear(self, loc):
        """
        清除输入框的内容.
        :param loc: 输入框元素定位
        :return:
        """
        el = self.get_element(loc)
        el.clear()
        log().info("✅ 清除输入框的内容 ")

    def send_value(self, loc, text):
        """
        操作输入框.
        :param loc: 输入框元素定位
        :param text: 输入文本
        :return:
        """
        try:
            el = self.get_element(loc)
            el.clear()
            log().info("✅ 清除输入框的内容 ")
            el.send_keys(text)
            log().info("✅ 输入框输入的内容为：{}".format(text))
        except Exception as e:
            error_msg = "❌ 未能正确向输入框输入文本: {} ".format(text)
            log().error(error_msg)
            return e

    def get_text(self, loc):
        """
        获取元素文本
        :return:
        """
        el = self.get_element(loc).text
        log().info("✅ 获取元素的文本为：{}".format(el))
        return el

    def click(self, loc):
        """
        可以点击任何文本/图像，包括链接，复选框，单选按钮，甚至下拉框等等..
        :param loc: 元素定位
        :return:
        """
        el = self.get_element(loc)
        el.click()
        log().info("✅ 点击元素：{by}={value} ".format(by=loc[0], value=loc[1]))

    def right_click(self, loc):
        """
        右键单击元素.
        :param loc: 元素定位
        :return:
        """
        el = self.get_element(loc)
        ActionChains(self.driver).context_click(el).perform()
        log().info("✅ 右键单击元素：{by}={value} ".format(by=loc[0], value=loc[1]))

    def move_to_element(self, loc):
        """
        鼠标移到元素（悬停）
        :param loc: 元素定位
        :return:
        """
        el = self.get_element(loc)
        ActionChains(self.driver).move_to_element(el).perform()
        log().info("✅ 鼠标移到元素（悬停）：{by}={value} ".format(by=loc[0], value=loc[1]))

    def double_click(self, loc):
        """
        双击元素
        :param loc:
        :return:
        """
        el = self.get_element(loc)
        ActionChains(self.driver).double_click(el).perform()
        log().info("✅ 双击元素：{by}={value} ".format(by=loc[0], value=loc[1]))

    def drag_and_drop(self, start_loc, target_loc):
        """
        把一个元素拖到一定的距离，然后把它放下
        :param start_loc: 元素起始位置
        :param target_loc: 元素停止位置
        :return:
        """
        start = self.get_element(start_loc)
        target = self.get_element(target_loc)
        ActionChains(self.driver).drag_and_drop(start, target).perform()
        log().info("✅ 把元素从{by1}={value1}拖拽到{by2}={value2}放下 ".format(
            by1=start_loc[0], value1=start_loc[1], by2=target_loc[0], value2=target_loc[1]))

    def close(self):
        """
        模拟用户在弹出框的标题栏中点击“关闭”按钮窗口
        """
        self.driver.close()
        log().info("✅ 关闭浏览器当前窗口")

    def quit(self):
        """
        退出使用的所有窗口.
        """
        self.driver.quit()
        log().info("✅ 关闭浏览器所有窗口")

    def submit(self, loc):
        """
        提交指定的表单
        """
        el = self.get_element(loc)
        el.submit()
        log().info("✅ 提交指定的表单：{by}={value} ".format(by=loc[0], value=loc[1]))

    def refresh(self):
        """
        刷新当前页面.
        """
        self.driver.refresh()
        log().info("✅ 刷新当前页面 ")

    def js(self, script):
        """
        执行JavaScript脚本.
        用法: driver.js("window.scrollTo(200,1000);")
        :param script: JavaScript脚本
        :return:
        """
        try:
            self.driver.execute_script(script)
            log().info("✅ 执行js脚本：{} ".format(script))
        except Exception as e:
            error_msg = "❌ 未能正确执行js脚本：{} ".format(script)
            log().error(error_msg)
            return e

    def get_attribute(self, loc, attribute):
        """
        获取元素属性的值
        :param loc: 元素定位
        :param attribute: 元素属性
        :return:
        """
        el = self.get_element(loc)
        el_attribute = el.get_attribute(attribute)
        log().info("✅ 获取元素{value1}属性的值：{value2} ".format(value1=attribute, value2=el_attribute))
        return el_attribute

    def get_display(self, loc):
        """
        获取元素是否显示，返回结果为真或假
        """
        try:
            el = self.get_element(loc)
            el_play = el.is_displayed()
            log().info("✅ 元素已显示：{by}={value} ".format(by=loc[0], value=loc[1]))
            return el_play
        except Exception as e:
            error_msg = "❌ 元素未显示：{by}={value} ".format(by=loc[0], value=loc[1])
            log().error(error_msg)
            return e

    def get_title(self):
        """
        得到窗口标题.
        """
        title = self.driver.title
        log().info("✅ 当前窗口标题为：{} ".format(title))
        return title

    def get_alert_text(self):
        """
        得到弹框的文本.
        """
        text = self.driver.switch_to.alert.text
        log().info("✅ 弹框的文本为：{} ".format(text))
        return text

    def wait(self, secs=10):
        """
        隐式等待，页面上的所有元素
        """
        self.driver.implicitly_wait(secs)

    def accept_alert(self):
        """
        接受警告框
        """
        self.driver.switch_to.alert.accept()
        log().info("✅ 确认弹框 ")

    def dismiss_alert(self):
        """
        忽略弹框
        """
        self.driver.switch_to.alert.dismiss()
        log().info("✅ 取消弹框 ")

    def switch_to_frame(self, loc):
        """
        切换到指定的iframe.
        """
        iframe_el = self.get_element(loc)
        self.driver.switch_to.frame(iframe_el)
        log().info("✅ 切换到指定的iframe：{by}={value} ".format(by=loc[0], value=loc[1]))

    def switch_to_frame_out(self):
        """
        返回默认iframe
        """
        self.driver.switch_to.default_content()
        log().info("✅ 返回默认iframe ")

    def open_new_window(self, loc):
        """
        打开新窗口并切换到新打开的窗口.
        """
        original_window = self.driver.current_window_handle
        el = self.get_element(loc)
        el.click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != original_window:
                self.driver.switch_to.window(handle)
        log().info("✅ 打开新窗口并切换到指定的窗口：{by}={value} ".format(by=loc[0], value=loc[1]))

    def get_screen_shot(self, file_path):
        """
        将当前窗口的屏幕截图保存到图像文件中.
        """
        self.driver.get_screenshot_as_file(file_path)
        log().info("✅ 将当前窗口的屏幕截图保存到图像文件中：{} ".format(file_path))

    def select_value(self, loc, value):
        """
        多选框，通过value值选择
        """
        el = self.get_element(loc)
        Select(el).select_by_value(value)
        log().info("✅ 通过value值选择多选框：{} ".format(value))

    def select_index(self, loc, index):
        """
        多选框，通过index值选择
        """
        el = self.get_element(loc)
        Select(el).select_by_index(index)
        log().info("✅ 通过index值选择多选框：{} ".format(index))

    def select_text(self, loc, text):
        """
        多选框，通过text文本值选择
        """
        el = self.get_element(loc)
        Select(el).select_by_visible_text(text)
        log().info("✅ 通过text文本值选择多选框：{} ".format(text))

    def window_scroll_to(self, left='0', top='0'):
        """
        控制浏览器滚动条的位置
        :param left: 水平的左边距
        :param top: 垂直的上边距
        Usage:
            window_scroll_to(100, 0)  #右滑
            execute_script("window.scrollTo(document.body.scrollWidth, 0)");
            window_scroll_to(0, 100)  #下滑
            execute_script("window.scrollTo(0, document.body.scrollHeight)");
        """
        scroll = "window.scrollTo(%s, %s);" % (left, top)
        self.js(scroll)
        log().info("✅ 控制浏览器向右滑动{}，向下滑动{} ".format(left, top))
