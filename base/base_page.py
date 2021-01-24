# coding=utf-8
"""
此文件为selenium常用方法二次封装文件
"""
from selenium import webdriver
import os
from selenium.webdriver.common.action_chains import ActionChains  # 处理鼠标事件(高级操作)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait  # 隐式等待
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # 添加设置浏览器驱动的头部信息时候使用（代理Ip等等）
from selenium.common.exceptions import NoSuchElementException, TimeoutException  # 异常处理（捕获异常）
from selenium.webdriver.support.select import Select

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, base_path)


class BasePage(object):
    """
    selenium框架的主要类
    """
    # 初始化基础类
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def element_wait(self, by, value, secs=5):
        """
        等待元素显示，显示等待元素，消耗时间最短
        """
        try:
            if by == "id":
                WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.ID, value)))
            elif by == "name":
                WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.NAME, value)))
            elif by == "class":
                WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
            elif by == "link_text":
                WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.LINK_TEXT, value)))
            elif by == "xpath":
                WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.XPATH, value)))
            elif by == "css":
                WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
            else:
                raise NoSuchElementException(
                    "找不到元素，请检查语法或元素")
        except TimeoutException:
            print("查找元素超时请检查元素")

    def get_element(self, by, value):
        """
        判断元素定位方式，并返回元素
        """
        if by == "id":
            element = self.driver.find_element_by_id(value)
        elif by == "name":
            element = self.driver.find_element_by_name(value)
        elif by == "class_name":
            element = self.driver.find_element_by_class_name(value)
        elif by == "link_text":
            element = self.driver.find_element_by_link_text(value)
        elif by == "partial_link_text":
            element = self.driver.find_element_by_partial_link_text(value)
        elif by == "xpath":
            element = self.driver.find_element_by_xpath(value)
        elif by == "css_selector":
            element = self.driver.find_element_by_css_selector(value)
        else:
            raise NameError(
                "Please enter the correct targeting elements,"
                "'id','name','class_name','link_text','partial_link_text','xpath','css_selector'.")
        return element

    def open(self):
        """
        打开url.
        用法:
        driver.open()
        """
        self.driver.get(self.url)

    def max_window(self):
        """
        设置浏览器最大化.
        用法:
        driver.max_window()
        """
        self.driver.maximize_window()

    def set_window(self, wide, high):
        """
        设置浏览器窗口宽和高.
        用法:
        driver.set_window(wide,high)
        """
        self.driver.set_window_size(wide, high)

    def send_value(self, by, value, text):
        """
        操作输入框.
        用法:
        driver.type(by, value,"selenium")
        """
        el = self.get_element(by, value)
        el.send_keys(text)

    def clear(self, by, value):
        """
        清除输入框的内容.
        用法:
        driver.clear(by, value)
        """
        el = self.get_element(by, value)
        el.clear()

    def click(self, by, value):
        """
        它可以点击任何文本/图像
        连接，复选框，单选按钮，甚至下拉框等等..
        用法:
        driver.click(by, value)
        """
        el = self.get_element(by, value)
        el.click()

    def right_click(self, by, value):
        """
        右键单击元素.
        用法:
        driver.right_click(by, value)
        """
        el = self.get_element(by, value)
        ActionChains(self.driver).context_click(el).perform()

    def move_to_element(self, by, value):
        """
        鼠标移到元素（悬停）.
        用法:
        driver.move_to_element(by, value)
        """
        el = self.get_element(by, value)
        ActionChains(self.driver).move_to_element(el).perform()

    def double_click(self, by, value):
        """
        双击元素.
        用法:
        driver.double_click(by, value)
        """
        el = self.get_element(by, value)
        ActionChains(self.driver).double_click(el).perform()

    def drag_and_drop(self, el_by, el_value, ta_by, ta_value):
        """
        把一个元素拖到一定的距离，然后把它放下.
        用法:
        driver.drag_and_drop(el_by, el_value, ta_by, ta_value)
        """
        element = self.get_element(el_by, el_value)
        target = self.get_element(ta_by, ta_value)
        ActionChains(self.driver).drag_and_drop(element, target).perform()

    def click_text(self, text):
        """
        单击链接文本中的元素
        用法:
        driver.click_text("新闻")
        """
        self.driver.find_element_by_partial_link_text(text).click()

    def close(self):
        """
        模拟用户在弹出框的标题栏中点击“关闭”按钮窗口或选项卡.
        Usage:
        driver.close()
        """
        self.driver.close()

    def quit(self):
        """
        关闭使用的所有窗口.
        用法:
        driver.quit()
        """
        self.driver.quit()

    def submit(self, by, value):
        """
        提交指定的表单
        用法:
        driver.submit(by, value)
        """
        el = self.get_element(by, value)
        el.submit()

    def F5(self):
        """
        刷新当前页面.
        用法:
        driver.F5()
        """
        self.driver.refresh()

    def js(self, script):
        """
        执行JavaScript脚本.
        用法:
        driver.js("window.scrollTo(200,1000);")
        """
        self.driver.execute_script(script)

    def get_attribute(self, by, value, attribute):
        """
        获取元素属性的值.
        用法:
        driver.get_attribute(by, value,"type")
        """
        el = self.get_element(by, value)
        return el.get_attribute(attribute)

    def get_text(self, by, value):
        """
        获得元素文本信息
        用法:
        driver.get_text(by, value)
        """
        el = self.get_element(by, value)
        return el.text

    def get_display(self, by, value):
        """
        获取元素来显示，返回结果为真或假.
        用法:
        driver.get_display(by, value)
        """
        el = self.get_element(by, value)
        return el.is_displayed()

    def get_title(self):
        """
        得到窗口标题.
        用法:
        driver.get_title()
        """
        return self.driver.title

    def get_url(self):
        """
        获取当前页面的URL地址.
        用法:
        driver.get_url()
        """
        return self.driver.current_url

    def get_alert_text(self):
        """
        得到警报的文本.
        用法:
        driver.get_alert_text()
        """
        return self.driver.switch_to.alert.text

    def wait(self, secs=10):
        """
        隐式等，页面上的所有元素.
        用法:
        driver.wait(10)
        """
        self.driver.implicitly_wait(secs)

    def accept_alert(self):
        """
        接受警告框.
        用法:
        driver.accept_alert()
        """
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        """
        Dismisses the alert available.
        用法:
        driver.dismiss_alert()
        """
        self.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, by, value):
        """
        切换到指定的frame.
        用法:
        driver.switch_to_frame(by, value)
        """
        iframe_el = self.get_element(by, value)
        self.driver.switch_to.frame(iframe_el)

    def switch_to_frame_out(self):
        """
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.
        Usage:
        driver.switch_to_frame_out()
        """
        self.driver.switch_to.default_content()

    def open_new_window(self, by, value):
        """
        打开新窗口并切换到新打开的窗口.
        用法:
        传入一个点击后会跳转的元素
        driver.open_new_window("link_text=>注册")
        """
        original_window = self.driver.current_window_handle
        el = self.get_element(by, value)
        el.click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != original_window:
                self.driver.switch_to.window(handle)

    def get_screen_shot(self, file_path):
        """将当前窗口的屏幕截图保存到PNG图像文件中.
        用法:
        driver.get_screen_shot('/Screenshots/foo.png')
        """
        self.driver.get_screenshot_as_file(file_path)

    def select_value(self, by, value, value1):
        """
        构造函数。对给定的元素进行了检查，确实是一个SELECT标记。如果不是,
        然后抛出一个意料之外的tag name exception.
        :Args:
         - css - element SELECT element to wrap
         - value - The value to match against
        Usage:
            <select name="NR" id="nr">
                <option value="10" selected="">每页显示10条</option>
                <option value="20">每页显示20条</option>
                <option value="50">每页显示50条</option>
            </select>
            driver.select("css", "#nr", '20')
            driver.select("xpath", "//[@name='NR']", '20')
        """
        el = self.get_element(by, value)
        Select(el).select_by_value(value1)

    def select_index(self, by, value, index):
        """
        构造函数。对给定的元素进行了检查，确实是一个SELECT标记。如果不是,
        然后抛出一个意料之外的tag name exception.
        :Args:
         - css - element SELECT element to wrap
         - value - The value to match against
        Usage:
            <select name="NR" id="nr">
                <option value="10" selected="">每页显示10条</option>
                <option value="20">每页显示20条</option>
                <option value="50">每页显示50条</option>
            </select>
            driver.select("css", "#nr", '20')
            driver.select("xpath", "//[@name='NR']", '20')
        """
        el = self.get_element(by, value)
        Select(el).select_by_index(index)

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


if __name__ == '__main__':
    driver = webdriver.Chrome()
    page = BasePage(driver, 'https://www.baidu.com')
    page.open()
    page.quit()
