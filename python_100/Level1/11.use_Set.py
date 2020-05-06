# 11.给定两个列表，怎么找出他们相同的元素和不同的元素？
a = [1,2,3,5]
b = [2,3,4,6]


c = []
d = []

for j in b :
    if j in a:
        c.append(j)
    else:
        d.append(j)

for i in a:
    if i not in b:
        d.append(i)

print(c,d)


# 这里可以使用set集合的概念：set是一组key的集合，不存储value。无序不重复元素组成的集合
# c = set(a) & set(b)
# print(c)

# d = set(a) ^ set(b)
# print(d)
