# 34.用一行代码生成[1,4,9,16,25,36,49,64,81,100]
res = [i*i for i in range(1,11)]
print(res)


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