# 7.将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}
a = "k:1 |k1:2|k2:3|k3:4"
a_list = a.split('|')
a_dict = {}
for i in a_list:
    b = i.split(':')
    a_dict[b[0]] = int(b[1])
    
print(a_dict)


# d = {k:int(v) for t in a.split('|') for k,v in (t.split(":"), )}
# 要习惯这种写法