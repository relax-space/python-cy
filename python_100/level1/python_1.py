# 问题1
# 编写一个程序，查找所有可以被7整除但不是5的倍数的数字。在2000到3200之间（均包括在内）。所获得的数字应以逗号分隔的顺序打印在一行上。

for i in range(2000,3200):
    if i % 7 == 0 and i % 5 != 0:
        print(i,end=',')