from pyzw.内置命令 import *


x = 1


def test():
    x = 2
    expression = 'x + 1'
    result0 = eval执行(expression)
    result1 = eval执行(expression, globals())
    result2 = eval执行(expression, globals(), locals())
    print(f"result1: {result0}")
    print(f"result1: {result1}")
    print(f"result2: {result2}")


test()
