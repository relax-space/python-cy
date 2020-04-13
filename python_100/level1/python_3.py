# 问题3
# 编写一个程序，该程序从控制台接受一个逗号分隔的数字序列，并生成一个列表和一个包含每个数字的元组。
# 假设将以下输入提供给程序：34,67,55,33,12,98
# 然后，输出应为：
# ['34'，'67'，'55'，'33'，'12'，'98']
# （“ 34”，“ 67”，“ 55”，“ 33”，“ 12”，“ 98”）

# 字符串转化成列表可以使用函数split()
# 列表转化成字符串可以使用.join()
# 列表转化成元组可以用tuple()


input_str = input('input your number str:')
input_list = input_str.split(',')
input_tuple = tuple(input_list)
input_str = ','.join(input_list)

print('列表格式：',input_list)
print('元组格式：',input_tuple)
print('字符串格式：',input_str)