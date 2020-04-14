# 问题8

# 编写一个程序，该程序接受以逗号分隔的单词序列作为输入，并在按字母顺序对单词进行排序后以逗号分隔的顺序打印这些单词。
# 假设将以下输入提供给程序：没有，你好，袋，世界
# 然后，输出应为：袋，你好，没有，世界

import pypinyin

# a = '没有，你好，袋，世界'
# b = pypinyin.pinyin(a,style=pypinyin.Style.FIRST_LETTER)
# c = pypinyin.slug(a)

a = input('input your chinese word:')

input_str = a.split('，')
result = {}
for i in input_str:
    key = pypinyin.pinyin(i,style=pypinyin.Style.FIRST_LETTER)[0][0]
    result[key] = i

# print(result)
res = sorted(result.items())
# print(res)
for i in res :
    print(i[1],end=',')




