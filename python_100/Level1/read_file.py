# -*- coding: UTF-8 -*-
def read_file(filepath):

    with open(filepath,'rb') as file:
        # yield (file.readlines())
        for i in file:
            yield i


a = read_file(r'D:\pythontest/test\python_100/2/base.txt')
print(next(a))




