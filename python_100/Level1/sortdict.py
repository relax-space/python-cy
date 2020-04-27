# 现有字典 d= {'a':24,'g':52,'i':12,'k':33}请按value值进行排序?

d= {'a':24,'g':52,'i':12,'k':33}
print(sorted(d.items(),key=lambda x:x[1]))

# 使用了sorted函数的key，使用匿名函数lambda
# x[0]代表用key进行排序；x[1]代表用value进行排序。

