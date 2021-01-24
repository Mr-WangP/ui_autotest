# coding=utf-8
import os
import pytest
import logging
import time
from py.xml import html
from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as CH_Options
from selenium.webdriver.firefox.options import Options as FF_Options
from config import RunConfig

# 项目目录配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = os.path.join(BASE_DIR, "test_report", "")
LOG_DIR = os.path.join(BASE_DIR, "test_log", "")


# 定义基本测试环境
@pytest.fixture(scope='function')
def base_url():
    return RunConfig.url


# 设置用例描述表头
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.insert(3, html.th('Time', class_='sortable time', col='time'))
    cells.pop()


# 设置用例描述表格
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.insert(3, html.td(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), class_='col-time'))
    cells.pop()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    用于向测试用例报告中添加用例的开始时间、内部注释，和失败截图等.
    :param item:测试用例对象
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    report.description = description_html(item.function.__doc__)
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            case_path = report.nodeid.replace("::", "_") + ".png"
            if "[" in case_path:
                case_name = case_path.split("-")[0] + "].png"
            else:
                case_name = case_path
            capture_screenshots(case_name)
            img_path = "image/" + case_name.split("/")[-1]
            if img_path:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % img_path
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def description_html(desc):
    """
    将用例中的描述转成HTML对象
    :param desc: 描述
    :return:
    """
    if desc is None:
        return "No case description"
    desc_ = ""
    for i in range(len(desc)):
        if i == 0:
            pass
        elif desc[i] == '\n':
            desc_ = desc_ + ";"
        else:
            desc_ = desc_ + desc[i]

    desc_lines = desc_.split(";")
    desc_html = html.html(
        html.head(
            html.meta(name="Content-Type", value="text/html; charset=latin1")),
        html.body(
            [html.p(line) for line in desc_lines]))
    return desc_html


def capture_screenshots(case_name):
    """
    配置用例失败截图路径
    :param case_name: 用例名
    :return:
    """
    global driver
    file_name = case_name.split("/")[-1]
    if RunConfig.NEW_REPORT is None:
        raise NameError('没有初始化测试报告目录')
    else:
        image_dir = os.path.join(RunConfig.NEW_REPORT, "image", file_name)
        RunConfig.driver.save_screenshot(image_dir)


# 启动浏览器
@pytest.fixture(scope='session', autouse=True)
def browser():
    """
    全局定义浏览器驱动
    :return:
    """
    global driver

    if RunConfig.driver_type == "chrome":
        # 本地chrome浏览器
        driver = webdriver.Chrome()
        driver.maximize_window()

    elif RunConfig.driver_type == "firefox":
        # 本地firefox浏览器
        driver = webdriver.Firefox()
        driver.maximize_window()

    elif RunConfig.driver_type == "chrome-headless":
        # chrome headless模式
        chrome_options = CH_Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(options=chrome_options)

    elif RunConfig.driver_type == "firefox-headless":
        # firefox headless模式
        firefox_options = FF_Options()
        firefox_options.headless = True
        driver = webdriver.Firefox(firefox_options=firefox_options)

    elif RunConfig.driver_type == "grid":
        # 通过远程节点运行
        driver = Remote(command_executor='http://localhost:4444/wd/hub',
                        desired_capabilities={
                            "browserName": "chrome",
                        })
        driver.set_window_size(1920, 1080)

    else:
        raise NameError("driver驱动类型定义错误！")

    RunConfig.driver = driver

    return driver


# 关闭浏览器
@pytest.fixture(scope="session", autouse=True)
def browser_close():
    yield driver
    driver.quit()
    print("test end!")


def log():
    # 创建一个日志器
    logger = logging.getLogger('logger')
    # 设置日志输出最低等级，低于当前等级就会忽略
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        # 创建处理器
        sh = logging.StreamHandler()
        fh = logging.FileHandler(filename='{}\\{}_log'.format(
            LOG_DIR, time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())), encoding='utf-8')
        # 创建一个格式器
        formator = logging.Formatter(fmt='%(asctime)s %(filename)s %(levelname)s %(message)s',
                                     datefmt='%Y/%m/%d/%X')
        sh.setFormatter(formator)
        fh.setFormatter(formator)
        logger.addHandler(sh)
        logger.addHandler(fh)

    return logger


if __name__ == "__main__":
    capture_screenshots("test_dir/test_baidu_search.png")
