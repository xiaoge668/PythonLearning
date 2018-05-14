import codecs

# import chardet
from io import StringIO
from io import BytesIO
import os
import pickle
import json


"""
def open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True):

"""

#f = open('song1.txt', 'r')
#print(f) # <_io.TextIOWrapper name='song' mode='r' encoding='UTF-8'>



# f1 = open('song1.txt', 'r', encoding='gbk', errors='ignore')
# print(f1.read())

# print(f.read())
"""
sajgdjaafhkgfldskjfdjg
fgajg
kkk
ll
"""

# print(f.readline())
"""
sajgdjaafhkgfldskjfdjg
"""

# print(f.readlines()) # ['sajgdjaafhkgfldskjfdjg\n', 'fgajg\n', 'kkk\n', 'll\n']

# print(f.readlines(25)) # ['sajgdjaafhkgfldskjfdjg\n', 'fgajg\n']

# f.close()

"""
try:
    f = open('song1.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

"""
"""
saaf是否考虑sk浏览jfdjg
fgajg
kkk
ll
"""


"""
with open('song1.txt', 'r') as f:
    print(f.read())
    
"""
"""
saaf是否考虑sk浏览jfdjg
fgajg
kkk
ll
"""


"""
for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉


"""
"""
saaf是否考虑sk浏览jfdjg
fgajg
kkk
ll
"""

"""
f = open('song2', 'a')

num = f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
print(num)
f.close()
"""

"""
with open('song2', 'w') as f:
    f.write('Hello, world!')
"""


# print(f.tell())

"""
移动文件读取指针到指定位置。`offset`:开始的偏移量，需要向前或向后移动的字节数,正往结束方向移动，负往开始方向移动。
`whence`： 给`offset`参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头算起，1代表开始从当前位置开始算起，
2代表从文件末尾开始算起。当有换行时，会被换行截断。
saaf是否考虑sk浏览jfdjg
fgajg
kkk
ll

"""

"""
f = StringIO()
print(f.write('hello')) # 5
f.write(' ')
f.write('world!')
# getvalue()方法用于获得写入后的str。
print(f.getvalue()) # hello world!
"""

"""
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
    
"""
"""
Hello!
Hi!
Goodbye!
"""

"""
f = BytesIO()
f.write('中文'.encode('utf-8')) # 3
print(f.getvalue()) # b'\xe4\xb8\xad\xe6\x96\x87'



# 请注意，写入的不是str，而是经过UTF-8编码的bytes。和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：

f1 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f1.read()) # b'\xe4\xb8\xad\xe6\x96\x87'
"""

"""
# 操作系统类型(如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。)
print(os.name) # posix

# 要获取详细的系统信息，可以调用uname()函数(uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的)
print(os.uname())


# posix.uname_result(sysname='Darwin', nodename='yang.local', release='17.3.0', 
# version='Darwin Kernel Version 17.3.0: Thu Nov  9 18:09:22 PST 2017; 
# root:xnu-4570.31.3~1/RELEASE_X86_64', machine='x86_64')

"""


# print(os.environ)
"""
environ({'PATH': '/Users/yang/Desktop/Python/PythonLearning/venv/bin:/Users/yang/.rvm
/gems/ruby-2.4.1/bin:/Users/yang/.rvm/gems/ruby-2.4.1@global...

"""

# print(os.environ.get('PATH'))


# print(os.environ.get('x', 'default')) # default



# 查看当前目录的绝对路径:
# print(os.path.abspath('.')) # /Users/yang/Desktop/Python/PythonLearning/demo1

"""
把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
在Linux/Unix/Mac下，os.path.join()返回这样的字符串：part-1/part-2;而Windows下会返回这样的字符串：part-1\part-2
"""
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# print(os.path.join('/Users/yang/Desktop', 'testdir')) # /Users/yang/Desktop/testdir

# 然后创建一个目录:
#print(os.mkdir('/Users/yang/Desktop/testdir')) # None
# 删掉一个目录:
# print(os.rmdir('/Users/yang/Desktop/testdir')) # None


# print(os.path.split('/Users/yang/Desktop/file.txt')) # ('/Users/yang/Desktop', 'file.txt')

# print(os.path.splitext('/path/to/file.txt')) # ('/path/to/file', '.txt')




# 文件操作使用下面的函数。假定当前目录下有一个test.txt文件：
# 对文件重命名:
# os.rename('test.txt', 'test.py')
# 删掉文件:
# os.remove('test.py')



# 列出当前目录下的所有目录
# print([x for x in os.listdir('.') if os.path.isdir(x)])
# 要列出所有的.py文件
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
"""
['LYJudgeSentence.py', 'ly_IOProgram.py', '__init__.py', 'ly_variable.py', 'LYMethod.py', 
'ly_module.py', 'ly_string.py', 'ly_method.py', 'ly_judge_sentence.py', 'LYString.py', 
'ly_sum.py']
"""




d = dict(name='Bob', age=20, score=88)
# print(pickle.dumps(d))
"""
b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x03\x00\x00\x00Bobq\x02X\x03\x00\x00\x00
ageq\x03K\x14X\x05\x00\x00\x00scoreq\x04KXu.'
"""

# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()
# 直接把对象序列化后写入一个file-like Object：看看写入的dump.txt文件，一堆乱七八糟的内容，
# 这些都是Python保存的对象内部信息。

# f = open('song1.txt', 'wb')
# print(pickle.dump(d, f))
# f.close()



# f = open('song1.txt', 'rb')
# d = pickle.load(f)
# f.close()
# print(d) # {'name': 'Bob', 'age': 20, 'score': 88}




# d = dict(name='Bob', age=20, score=88)
# print(json.dumps(d)) # {"name": "Bob", "age": 20, "score": 88}




# json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# print(json.loads(json_str)) # {'age': 20, 'score': 88, 'name': 'Bob'}



"""
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
print(json.dumps(s))

"""


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

