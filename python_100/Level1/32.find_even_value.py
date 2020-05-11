# 32.请写出一个函数满足以下条件
# 该函数的输入是一个仅包含数字的list,输出一个新的list，其中每一个元素要满足以下条件：
#     1、该元素是偶数
#     2、该元素在原list中是在偶数的位置(index是偶数)
num = [0,1,2,3,4,5,6,7,8,9,10]

res = []
for i in num:
    if i %2 == 0 and num.index(i) %2 == 0:
        res.append(i)

print(res)
