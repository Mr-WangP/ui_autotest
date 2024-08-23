# ui_autotest
python + selenium + pytest + allure

### 特点

* 全局配置浏览器启动/关闭。
* 测试用例运行失败自动截图。
* 测试用例运行失败可以重跑。
* 测试数据参数化。

### 安装

```shell
$ pip install -r requirements.txt
```

### 配置

在 `config.py` 文件配置

```python
class RunConfig:
    """
    运行测试配置
    """
    # 项目路径
    root_path = Path(__file__).resolve().parent

    # 项目运行url
    conf_path = Path(root_path, "common", "conf_env.ini")
    uri = ConfigUtil(conf_path).read_config('DEFAULTS', 'url')

    # 运行测试用例的目录或文件
    cases_path = Path(root_path, "test_dir")

    # 配置浏览器驱动类型(Chrome/Edge/Remote)。
    driver_type = "Chrome"

    # 数据文件目录
    data_path = Path(root_path, "data")

    util_path = Path(root_path, "utils")
    # 日志文件目录
    log_path = Path(root_path, "logs")

    # 报告文件目录
    report_path = Path(root_path, "report")

    # cookie保存文件
    cookies_path = Path(root_path, "cookies")

    # 上传、下载文件保存目录
    download_path = Path(root_path, "files")
    upload_path = Path(root_path, "files")
    # 失败重跑次数
    rerun = "1"

    # 当达到最大失败数，停止执行
    max_fail = "3"

    # 浏览器驱动（不需要修改）
    driver = None
```

### 运行

```shell
$ python run_tests.py
```
