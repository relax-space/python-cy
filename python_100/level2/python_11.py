# 问题11
# 编写一个程序，以给定的数字作为a的值来计算a + aa + aaa + aaaa的值。
# 假设将以下输入提供给程序：
# 9
# 然后，输出应为：
# 11106

num = input('input your num:')
# num = 9

try:
    num = int(num)
    num_1 = num * 10 + num
    num_2 = num_1 * 10 + num
    num_3 = num_2 * 10 + num
    result = num + num_1 + num_2 + num_3
    print(result)
except :
    print('plz input int')