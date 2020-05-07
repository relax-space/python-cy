# 16.设计实现遍历目录与子目录，抓取.pyc文件

import os

file_dict = {}
res = []
def go_through(file_path):
    file = os.listdir(file_path)
    file_dict[file_path] = file
    for f in file:
        f_path = file_path + '\\' + f
        if os.path.isdir(f_path):
            go_through(f_path)
        else:
            if os.path.splitext(f)[1] == '.pyc':
                res.append(f)
                
    return res


a = go_through('D:\\pythontest\\test\\python_100')
# print(a)



#可以使用os.walk()不需要自己进行递归，可以直接得到要遍历的目录,有三个元组，dirpath, dirnames, filenames
# print(os.walk('D:\\pythontest\\test\\python_100')) generator
for dirpath, dirnames, filenames in os.walk('D:\\pythontest\\test\\python_100'):
    # print(dirpath, dirnames,filenames)
    for f in filenames:
        if os.path.splitext(f)[1] == '.pyc':
            print(f)