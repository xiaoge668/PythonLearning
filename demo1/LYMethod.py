
#  1.无参数的函数
def hello():
    print('hello')
hello()  # 调用函数hello(),输出结果：hello

#  2.函数中带上参数变量
def area(width, height):
    return width * height
print(area(20,8))  #  调用函数area(),输出结果：160

#  3.


sum = lambda  arg1, arg2: arg1 + arg2
print ("相加后的值为 : ", sum( 10, 20))

