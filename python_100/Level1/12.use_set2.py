# 12.请写出一段python代码实现删除list里面的重复元素？

a = [1,2,3,4,5,4,3,2,1,0]

b = list(set(a))
print(b)
# 还可以加一个，排序显示方式为根据原始的index进行排序
# b = list(set(a))
# b.sort(key=a.index)
# print(b)