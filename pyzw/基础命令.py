import time


def 延时(时长: float):
    """
    详细用法请阅读中文文档(https://pyzw.org.cn)
    :param 时长: 必选参数, 单位: 秒
    :return: None
    """
    time.sleep(时长)


def 打印(*输出内容, 分隔符=' ', 后缀='\n', 文件=None, 刷新=False):
    """
    详细用法请阅读中文文档(https://pyzw.org.cn)
    :param 输出内容: 可以填入一个或多个输出内容, 以逗号隔开即可
    :param 分隔符: 当有多个输出内容时, 以指定符号进行分隔, 默认为空格
    :param 后缀: 输出内容的结尾, 默认为换行符
    :param 文件: 当填入文件路径时, 可以将输出内容写入到该文件
    :param 刷新:
    :return:
    """
    return print(*输出内容, sep=分隔符, end=后缀, file=文件, flush=刷新)


def 调试输出(*任意数据, 分隔符=' ', 后缀='\n', 文件=None, 刷新=False):
    """
    详细用法请阅读中文文档(https://pyzw.org.cn)
    :param 任意数据:
    :param 分隔符:
    :param 后缀:
    :param 文件:
    :param 刷新:
    :return:
    """
    return print(*任意数据, sep=分隔符, end=后缀, file=文件, flush=刷新)
