
# 37.给定一个任意长度数组，实现一个函数：让所有奇数都在偶数前面，而且奇数升序排列，偶数降序排序，如字符串'1982376455',变成'1355798642'

# 我的想法比较复杂，是将奇数和偶数分别拿出来放到列表中，分别排序后进行列表相加，这样需要三个列表才能完成

# 示例的处理办法是先将原列表进行排序，倒序之后，从前到后筛选奇数，先筛选出来的放到后面，没筛选到的偶数就是在最后还是倒序的排列。
# 使用了insert(),pop()函数
# insert()：将元素放置在列表的指定位置 list.insert(位置，值)
# pop():用于移除列表中的一个元素，并且返回该元素的值  list.pop()

def sort_list(str):
    l = list(str)
    a = []
    b = []
    res = []
    while len(l) > 0:
        if int(l[0]) % 2 != 0:
            a.append(l[0])
        else:
            b.append(l[0])
            
        l.remove(l[0])
    a.sort()
    b.sort(reverse=True)
    res = a+b
    print(''.join(i for i in res))

def func1(l):
    if isinstance(l, str):
        l = [int(i) for i in l]
    l.sort(reverse=True)
    for i in range(len(l)):
        if l[i] % 2 > 0:
            l.insert(0, l.pop(i))
    print(''.join(str(e) for e in l))
            


a = '1982376455'

sort_list(a)
func1(a)