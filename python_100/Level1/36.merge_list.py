# 36.两个有序列表，l1,l2，对这两个列表进行合并不可使用extend

# extend() 函数用于在列表末尾一次性追加另一个序列中的多个值
# a.extend(b)


# 还可以用set，首先找出两个列表不同的数值，然后找到相同的，然后合并

# 这里比较注意原列表是有序的，最好合并之后还能够是有序列表（虽然题目好像没说）
# 思路就是先看列表的长度，如果都是有值，判断哪个值小，先放进新列表，然后删除这个小的数值，再进行比较
# 缺点是这样会将原列表改变了，列表是可变的，最后会将原列表都清空了
a = [1,2,3,4,5]
b = [2,4,6,7,8,10]

res = []

while len(a)>0 and len(b) > 0:
    if a[0] < b[0]:
        res.append(a[0])
        del a[0]
    elif a[0] == b[0]:
        res.append(a[0])
        del a[0]
        del b[0]
    else:
        res.append(b[0])
        del b[0]
while len(a) > 0:
    res.append(a[0])
    del a[0]
while len(b) > 0:
    res.append(b[0])
    del b[0]

print(res)