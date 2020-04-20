# 问题7
# 编写一个程序，该程序将X，Y这两位数字作为输入并生成一个二维数组。数组的第i行和第j列中的元素值应为i * j。
# 注意：i = 0,1 ..，X-1; j = 0,1，¡Y-1。
# 例
# 假设将以下输入提供给程序：3,5
# 然后，程序的输出应为：[[0，0，0，0，0]，[0，1，2，3，4]，[0，2，4，6，8]] 

value_list = input('input your value:')
value_list = value_list.split(',')

result = []

for i in range(1,int(value_list[0])+1):
    res1 = []
    for j in range(1,int(value_list[1])+1):
        if (j == int(value_list[1])+1):
            break
        else:
            res1.append((i-1)*j)

    result.append(res1)

print(result)
