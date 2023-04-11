from pyzw.内置命令 import *

# a = 取异步迭代器([2, 3, 5, 6])
# b = 取异步迭代器下一项数据(a, "完毕")

a = iter([2, 3, 5, 6])
for i in range(0, 9):
    b = next(a, 7)
    打印(b)

