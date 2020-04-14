# 问题6
# 编写一个程序，根据给定的公式计算并打印值：Q = [（2 * C * D）/ H]的平方根
# 以下是C和H的固定值：C为50。H为30。D是变量，其值应以逗号分隔的顺序输入到程序中。
# 例
# 让我们假设以下逗号分隔的输入序列已赋予程序：100,150,180
# 该程序的输出应为：18,22,24

# 可以使用math的sqrt()函数
from math import sqrt


C = 50
H = 30
result = []
D_str = input('input your number string:')
D_list = D_str.split(',')
for i in D_list:
    i = float(i)
    res = (2*C*i)/H
    result.append(round(sqrt(res)))

for j in result:
    print(j,end=',')

    