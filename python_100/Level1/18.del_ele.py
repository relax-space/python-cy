# 18.Python-遍历列表时删除元素的正确做法

a = [1,2,3,4,5,6,7,8,9]
# 删除元素5和8

for i in (a[:]):
    if i == 5 or  i == 8:
        a.remove(i)

print(a)