# 8.请按alist中元素的age由大到小排序
# alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]

alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]

a = sorted(alist,key = lambda x: x['age'],reverse=True)
print(a)

# 和题目4差不多,多考察了一下reverse