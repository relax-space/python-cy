# 问题18
# 网站要求用户输入用户名和密码进行注册。编写程序以检查用户输入的密码的有效性。
# 以下是检查密码的标准：
# 1. [a-z]之间至少1个字母
# 2. [0-9]之间至少1个数字
# 1. [A-Z]之间至少1个字母
# 3. [$＃@]中的至少1个字符
# 4.最小交易密码长度：6
# 5.交易密码的最大长度：12
# 您的程序应接受逗号分隔的密码序列，并将根据上述条件进行检查。符合条件的密码将被打印，每个密码之间用逗号分隔。
# 例
# 如果输入以下密码作为程序输入：
# ABd1234@1，a F1＃，2w3E*，2We3345
# 然后，程序的输出应为：
# ABd1234@1

# 是一个python使用正则的题目
import re
input_str = input('input your pwd:')
# input_str = 'ABd1234@1，a F1＃，2w3E*，2We3345'
input_list = input_str.split('，')

rgx_1 = r'[a-z]'
rgx_2 = r'[0-9]'
rgx_3 = r'[A-Z]'
rgx_4 = r'[$＃@]'
for i in input_list:
    if len(i)>=6 and len(i) <= 12 :
        if re.search(rgx_1,i) and re.search(rgx_2,i) and re.search(rgx_3,i) and re.search(rgx_4,i):
            print(i,end=',')
