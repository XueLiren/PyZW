from pyzw.内置命令 import *

x = compile('print(78)', 'test', 'eval')
print(x)
# exec(x)

x = compile('print(89)\nprint(88)', 'test', 'exec')
exec(x)
