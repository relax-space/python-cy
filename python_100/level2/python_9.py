# 问题9
# 编写一个程序，该程序接受由空格分隔的单词序列作为输入，
# 并在删除所有重复的单词并将其按字母数字顺序排序后打印这些单词。[大写]
# 假设将以下输入提供给程序：
# Hello world world Practice makes perfect
# Then, the output should be:
# HELLO WORLD PRACTICE MAKES PERFECT
# H M P W



# 可以使用python的集合概念，集合是不能有重复的，先用set(),然后改成列表

# input_str = input('input your string:')
input_str = 'Hello world world Practice makes perfect'
input_str = input_str.upper()
input_list = input_str.split(' ')
input_list = list(set(input_list))
input_list.sort()
print(input_list)



