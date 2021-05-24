# coding=utf-8
"""
此文件为selenium常用方法二次封装文件
"""
import os
from selenium.webdriver.common.action_chains import ActionChains  # 处理鼠标事件(高级操作)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait  # 隐式等待
from selenium.webdriver.support.select import Select

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, base_path)


class BasePage(object):
    """
    selenium框架的主要类
    """
    # 初始化基础类
    def __init__(self, driver, url=None):
        self.driver = driver
        self.root_uri = url if url else getattr(self.driver, 'url', None)

    def open(self, uri):
        """
        打开url.
        用法:
        driver.open()
        """
        root_uri = self.root_uri or ''
        self.driver.get(root_uri + uri)
        self.driver.implicitly_wait(5)

    def get_element(self, loc):
        """
        判断元素定位方式，并返回元素
        """
        return self.driver.find_element(*loc)

    def element_wait(self, loc, secs=5):
        """
        等待元素显示，显示等待元素，消耗时间最短
        """
        WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located(self.get_element(loc)))

    def max_window(self):
        """
        设置浏览器最大化.
        """
        self.driver.maximize_window()

    def set_window(self, wide, high):
        """
        设置浏览器窗口宽和高.
        """
        self.driver.set_window_size(wide, high)

    def send_value(self, loc, text):
        """
        操作输入框.
        """
        el = self.get_element(loc)
        el.send_keys(text)

    def clear(self, loc):
        """
        清除输入框的内容.
        """
        el = self.get_element(loc)
        el.clear()

    def click(self, loc):
        """
        可以点击任何文本/图像
        连接，复选框，单选按钮，甚至下拉框等等..
        """
        el = self.get_element(loc)
        el.click()

    def right_click(self, loc):
        """
        右键单击元素.
        """
        el = self.get_element(loc)
        ActionChains(self.driver).context_click(el).perform()

    def move_to_element(self, loc):
        """
        鼠标移到元素（悬停）
        """
        el = self.get_element(loc)
        ActionChains(self.driver).move_to_element(el).perform()

    def double_click(self, loc):
        """
        双击元素
        """
        el = self.get_element(loc)
        ActionChains(self.driver).double_click(el).perform()

    def drag_and_drop(self, start_loc, target_loc):
        """
        把一个元素拖到一定的距离，然后把它放下
        """
        start = self.get_element(start_loc)
        target = self.get_element(target_loc)
        ActionChains(self.driver).drag_and_drop(start, target).perform()

    def click_text(self, text):
        """
        单击链接文本中的元素
        """
        self.driver.find_element_by_partial_link_text(text).click()

    def close(self):
        """
        模拟用户在弹出框的标题栏中点击“关闭”按钮窗口或选项卡.
        """
        self.driver.close()

    def quit(self):
        """
        关闭使用的所有窗口.
        """
        self.driver.quit()

    def submit(self, loc):
        """
        提交指定的表单
        """
        el = self.get_element(loc)
        el.submit()

    def F5(self):
        """
        刷新当前页面.
        """
        self.driver.refresh()

    def js(self, script):
        """
        执行JavaScript脚本.
        用法: driver.js("window.scrollTo(200,1000);")
        """
        self.driver.execute_script(script)

    def get_attribute(self, loc, attribute):
        """
        获取元素属性的值
        """
        el = self.get_element(loc)
        return el.get_attribute(attribute)

    def get_text(self, loc):
        """
        获得元素文本信息
        """
        el = self.get_element(loc)
        return el.text

    def get_display(self, loc):
        """
        获取元素来显示，返回结果为真或假
        """
        el = self.get_element(loc)
        return el.is_displayed()

    def get_title(self):
        """
        得到窗口标题.
        """
        return self.driver.title

    def get_url(self):
        """
        获取当前页面的URL地址.
        """
        return self.driver.current_url

    def get_alert_text(self):
        """
        得到弹框的文本.
        """
        return self.driver.switch_to.alert.text

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

    def dismiss_alert(self):
        """
        忽略弹框
        """
        self.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, loc):
        """
        切换到指定的frame.
        """
        iframe_el = self.get_element(loc)
        self.driver.switch_to.frame(iframe_el)

    def switch_to_frame_out(self):
        """
        返回默认frame
        """
        self.driver.switch_to.default_content()

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

    def get_screen_shot(self, file_path):
        """
        将当前窗口的屏幕截图保存到PNG图像文件中.
        """
        self.driver.get_screenshot_as_file(file_path)

    def select_value(self, loc, value):
        """
        通过value值选择
        """
        el = self.get_element(loc)
        Select(el).select_by_value(value)

    def select_index(self, loc, index):
        """
        通过index值选择
        """
        el = self.get_element(loc)
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