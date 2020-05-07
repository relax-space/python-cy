# 26.用一行python代码写出1+2+3+10248

a = sum([1,2,3,1024])
print(a)

from functools import reduce
a = reduce(lambda x,y: x+y ,[1,2,3,1024])
print(a)