#!/usr/bin/python3
# -*- coding: UTF-8 -*-


' a test module '  # 表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释

__author__ = 'yang' # 使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；

# from LYFibonacci import module1, module2
from collections import *  # 这提供了一个简单的方法来导入一个模块中的所有项目。然而这种声明不该被过多地使用。
# import ly_sum
# from ly_sum import sum123,sum1234
from ly_sum import *  # 需要注意的是在实践中往往不鼓励从一个模块或包中使用 * 导入所有，因为这样会让代码变得很难读
import LYFibonacci.ly_fibo
import sys
import datetime


print(isinstance('abc', Iterator))


LYFibonacci.ly_fibo.fib(1000)
print(LYFibonacci.ly_fibo.fib2(100))
print(LYFibonacci.ly_fibo.__name__)
# print(ly_sum.sum123(90, 60))
print(sum123(90, 60))
print(sum1234(10, 10, 10))

print('--------------sys----------------')
print('命令行参数如下:')
for i in sys.argv:
    print(i)

print('Python 路径为：', sys.path)

print(datetime.date.today())
print(datetime.datetime.today())

print(sys)
print(LYFibonacci.ly_fibo)