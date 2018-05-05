#!/usr/bin/python3
# -*- coding: UTF-8 -*-
count = 0
while count < 5:
    print(count, '小于5')
    count += 1
else:
    print(count, '大于或等于5')


for i in range(5):
    print(i)  #  0 1 2 3 4

#  1.使用range指定区间的值
for i in range(3,5):
    print(i)  #  3 4

#  2.使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长')
for i in range(0,10,3):
    print(i)  #  0 3 6 9

#  3.结合range()和len()函数以遍历一个序列的索引
a = ['Google', 'Baidu', 'Runoob', 'Taobao']
for i in range(len(a)):
    print(i, a[i])  #  0 Google  1 Baidu  2 Runoob 3 Taobao

#  4.使用range()函数来创建一个列表
print(list(range(3)))  #  [0, 1, 2]

b = 6
if b > 1:
    pass #如果没有内容，可以先写pass，但是如果不写pass，就会语法错误



sequence = [12, 34, 34, 23]
for i, j in enumerate(sequence):
    print(i, j)
"""
0 12
1 34
2 34
3 23
"""

for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行 pass 块')
    print('当前字母 :', letter)



var = 10
while var > 0:
    print ('当期变量值为 :', var)
    var = var -1
    if var == 5:
        break


var1 = 5
while var1 > 0:
    var1 = var1 -1
    if var1 == 2:   # 变量为 2 时跳过输出
        continue
    print ('当前变量值 :', var1)



