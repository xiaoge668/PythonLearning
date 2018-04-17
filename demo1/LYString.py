

#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import base64


s = 'hello world !'


#  1.把字符串的第一个字符大写
print('s.capitalize():',s.capitalize())
#  2.返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
print('s.center(20):',s.center(20))
print('s.center(20,\'*\'):',s.center(20,'*'))
#  3.返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
"""
参数1：搜索的子字符串；
参数2：字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0；
参数3：字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。

"""
print('s.count(\'l\',0,-1):',s.count('l',0,-1))
#  4.以 encoding 指定的编码格式解码 string，如果出错默认报一个 ValueError 的异常,除非 errors 指定的是 'ignore' 或者'replace'
"""
python3不太一样：因为3.x中字符都为unicode编码，而b64encode函数的参数为byte类型，所以必须先转码。
"""
encodestr = base64.b64encode('abcr34r344r'.encode('utf-8'))
"""
encodestr: b'YWJjcjM0cjM0NHI='  结果和我们预想的有点区别，我们只想要获得YWJjcjM0cjM0NHI=，而字符串被b''包围了。
b 表示 byte的意思，我们只要再将byte转换回去就好了
"""
print('encodestr:',encodestr)

encodestr1 = str(encodestr,'utf-8', errors='strict')
print('encodestr1:',encodestr1) #  encodestr1: YWJjcjM0cjM0NHI=

decodestr = base64.b64decode(encodestr1.encode('utf-8'))
print('decodestr:',decodestr)  #  b'abcr34r344r'
print(str(decodestr,'utf-8', errors='strict'))  #  abcr34r344r
#  5.检查字符串是否以 obj 结束，如果beg或者end指定则检查指定的范围(长度)内是否以obj结束,如果是,返回 True,否则返回 False.
print('\'test\'.endswith(\'t\',4):','test'.endswith('t',0,4))
#  6.把字符串中的 tab 符号('\t')转为空格，tab 符号('\t')默认的空格数是 8。
print('this is\tstring example....wow!!!'.expandtabs(15))  #  this is        string example....wow!!!
#  7.检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
"""
str -- 指定检索的字符串
beg -- 开始索引，默认为0。
end -- 结束索引，默认为字符串的长度。
注意：检测到一个就会停止
"""
print(s.find('l',0,10))
#  8.跟find()方法一样，只不过如果str不在 string中会报一个异常
print('\'good\'.index(\'0\',0,4):','good'.index('o',0,4))
#  9.如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False(检测字符串是否由字母和数字组成)
print("'678'.isalnum():",'678'.isalnum())
print("'6a78'.isalnum():",'6a78'.isalnum())
print("'-he66'.isalnum():",'-he66'.isalnum())

#  10.如果 string 至少有一个字符并且所有字符都是字母则返回 True,否则返回 False(检测字符串是否只由字母组成)
print("'678'.isalpha():",'678'.isalpha())
print("'6a78'.isalpha():",'6a78'.isalpha())
print("'gegge'.isalpha():",'gegge'.isalpha())
#  11.如果 string 只包含十进制数字则返回 True 否则返回 False)
#     注意:定义一个十进制字符串，只需要在字符串前添加 'u' 前缀即可。
print("'678'.isdecimal():",'678'.isdecimal())
print("'678a'.isdecimal():",'678a'.isdecimal())
print("'0x124ad'.isdecimal():",'0x124ad'.isdecimal())
#  12.如果 string 只包含数字则返回 True 否则返回 False.
print("'678'.isdigit():",'678'.isdigit())
print("'678t'.isdigit():",'678t'.isdigit())
#  13.如果 string 中只包含数字字符，则返回 True，否则返回 False
print("'678'.isnumeric():",'678'.isnumeric())
print("'678t'.isnumeric():",'678t'.isnumeric())
#  14.如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，
# 则返回 True，否则返回 False(检测字符串是否由小写字母组成)
print("'test'.islower():",'test'.islower())
print("'Test'.islower():",'Test'.islower())
#  15.如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
print("'test'.isupper():",'test'.isupper())
print("'TEST'.isupper():",'TEST'.isupper())
#  16.如果 string 中只包含空格，则返回 True，否则返回 False
print("'       '.isspace():",'       '.isspace())
print("'This is string example....wow!!!'.isspace():",'This is string example....wow!!!'.isspace())
#  17.如果 string 是标题化的(见 title())则返回 True，否则返回 False
print("'This Is A Test'.istitle():",'This Is A Test'.istitle())
print("'This is a test'.istitle():",'This is a test'.istitle())
#  18.

'''

string.join(seq)

以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串

string.ljust(width)

返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串

string.lower()

转换 string 中所有大写字符为小写.

string.lstrip()

截掉 string 左边的空格

string.maketrans(intab, outtab])

maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。

max(str)

返回字符串 str 中最大的字母。

min(str)

返回字符串 str 中最小的字母。

string.partition(str)

有点像 find()和 split()的结合体,从 str 出现的第一个位置起,把 字 符 串 string 分 成 一 个 3 元 素 的 元 组 (string_pre_str,str,string_post_str),如果 string 中不包含str 则 string_pre_str == string.

string.replace(str1, str2,  num=string.count(str1))

把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次.

string.rfind(str, beg=0,end=len(string) )

类似于 find()函数，不过是从右边开始查找.

string.rindex( str, beg=0,end=len(string))

类似于 index()，不过是从右边开始.

string.rjust(width)

返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串

string.rpartition(str)

类似于 partition()函数,不过是从右边开始查找.

string.rstrip()

删除 string 字符串末尾的空格.

string.split(str="", num=string.count(str))

以 str 为分隔符切片 string，如果 num有指定值，则仅分隔 num 个子字符串

string.splitlines([keepends])

按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。

string.startswith(obj, beg=0,end=len(string))

检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查.

string.strip([obj])

在 string 上执行 lstrip()和 rstrip()

string.swapcase()

翻转 string 中的大小写

string.title()

返回"标题化"的 string,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())

string.translate(str, del="")

根据 str 给出的表(包含 256 个字符)转换 string 的字符,

要过滤掉的字符放到 del 参数中

string.upper()

转换 string 中的小写字母为大写

string.zfill(width)

返回长度为 width 的字符串，原字符串 string 右对齐，前面填充0

string.isdecimal()

isdecimal()方法检查字符串是否只包含十进制字符。这种方法只存在于unicode对象。

'''