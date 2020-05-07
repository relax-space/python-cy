# 28.字符串 "123" 转换成 123，不使用内置api，例如 int()
a = '123'
from functools import reduce

print(reduce(lambda x,y: x*10+ord(y)-ord('0'),a,0))


# 这里之前想到了reduce，但是并不知道如何处理str，
# ord():以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值

