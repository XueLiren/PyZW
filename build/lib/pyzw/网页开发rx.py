import reflex as rx


def 文本(文本内容="", *, 字体尺寸="", 字体颜色="", 元素标签="", 最大行数="", 最大宽度=""):
    """
    详细用法请阅读中文文档(https://pyzw.org.cn)
    :param 文本内容:
    :param 字体尺寸:
    :param 字体颜色:
    :param 元素标签:
    :param 最大行数:
    :param 最大宽度:
    :return:
    """
    return rx.text(文本内容, font_size=字体尺寸, color=字体颜色, as_=元素标签, noOfLines=最大行数, maxWidth=最大宽度)


def 标题(文本内容="", *, 组件尺寸="", 字体尺寸="", 字体颜色="", 元素标签="", 最大行数="", 最大宽度="", 最大高度=""):
    """
    详细用法请阅读中文文档(https://pyzw.org.cn)
    :param 文本内容:
    :param 组件尺寸:
    :param 字体尺寸:
    :param 字体颜色:
    :param 元素标签:
    :param 最大行数:
    :param 最大宽度:
    :param 最大高度:
    :return:
    """
    return rx.heading(文本内容, size=组件尺寸, font_size=字体尺寸, color=字体颜色, as_=元素标签, noOfLines=最大行数, maxWidth=最大宽度, lineHeight=最大高度)


def 高亮文本(文本内容="", *, 高亮内容: list = None, 高亮样式: dict = None):
    """
    详细用法请阅读中文文档(https://pyzw.org.cn)
    :param 文本内容:
    :param 高亮内容:
    :param 高亮样式:
    :return:
    """
    return rx.highlight(文本内容, query=高亮内容, styles=高亮样式)


def 标记文本(标记内容="", *, 字体颜色="", 字体粗细="", 元素标签=""):
    """
    详细用法请阅读中文文档(https://pyzw.org.cn)
    :param 标记内容:
    :param 字体颜色:
    :param 字体粗细:
    :param 元素标签:
    :return:
    """
    return rx.span(标记内容, color=字体颜色, font_weight=字体粗细, as_=元素标签)


def MK(markdown语句=""):
    """
    详细用法请阅读中文文档(https://pyzw.org.cn)
    :param markdown语句:
    :return:
    """
    return rx.markdown(markdown语句)
