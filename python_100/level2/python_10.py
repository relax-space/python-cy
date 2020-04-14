# 问题10
# 编写一个接受句子并计算字母和数字数量的程序。
# 假设将以下输入提供给程序：
# hello world! 123
# Then, the output should be:
# 字母10
# 数字3

# 用isdigit函数判断是否数字
#用isalpha判断是否字母
#isalnum判断是否数字和字母的组合


input_str = input('input your str:')
# input_str = 'hello world! 123'
count_num = 0
count_word = 0
for i in input_str:

    try:
        i = int(i)
        if i in list(range(0,10)):
            # print(i)
            count_num = count_num + 1 
    except :
        if i.isalpha():
            count_word = count_word + 1


print('数字:',count_num)
print('字母:',count_word)


