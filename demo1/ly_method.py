#!/usr/bin/python3
# -*- coding: UTF-8 -*-


from collections import Iterator


print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))


# 1.无参数的函数

def hello():
    print('hello')


hello()  # 调用函数hello(),输出结果：hello

#  2.函数中带上参数变量


def area(width, height):
    return width * height


print(area(20, 8))  # 调用函数area(),输出结果：160

#  3.

sum1 = lambda arg1, arg2: arg1 + arg2
print("相加后的值为 : ", sum1(10, 20))


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)


o = odd()
next(o)
next(o)
next(o)

print('------------------------------')


