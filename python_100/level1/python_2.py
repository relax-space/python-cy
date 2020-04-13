# 问题2
# 使用给定的整数n，编写程序以生成包含（i，i * i）的字典，该字典为1到n之间的整数（都包括在内）。然后程序应打印字典。
# 假设将以下输入提供给程序：8
# 然后，输出应为：{1：1、2：4、3：9、4：16、5：25、6：36、7：49、8：64}



# 学习了，可以使用pow()函数


num = input('input your number:')
try:
    num = int(num)
    print(num)
    result = {}
    for i in range(1,num+1):
        result[i] = pow(i,2)
    print(result)
except ValueError:
    print('plz input int')
