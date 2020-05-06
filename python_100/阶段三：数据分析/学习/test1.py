import pandas as pd 
import numpy  as np 
# s = pd.Series([1,3,'str',np.nan,44,1])



# s = pd.Series([1,3,'str'],index=['name','age','sex'])

# print(s)
# print(s.index)
# print(s.values)

# print(s['age'])
# s['age'] = 12
# print(s['age'])
# print(s)

sd = {'name':'xiaohua','age':12,'sex':'female'}
s = pd.Series(sd)
# print(s)
s = pd.Series(sd,index=['name','height','sex'])
# print(s.isnull())
s.index = ['名字','身高','性别']
# print(s)

data = {'name':['google','baidu','yahoo'],'marks':[100,200,300],'price':[1,2,3]}
f1 = pd.DataFrame(data,columns=['price','marks','name'],index=['a','b','c'])
# print(f1)
data = {'name':{'one':'xiaohong','two':'xiaohua'},'grade':{'one':100,'two':98}}
f2 = pd.DataFrame(data)
# print(f2)
data = {'username':{'first':'wangxin','second':'dalao'},'age':{'first':24,'second':25}}
f3 = pd.DataFrame(data,columns=['username','age','sex'])
print(f3)
f3['sex'] = 'female'
print(f3)

# dates = pd.date_range('20200101',periods=6)
# print(dates)

# df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])

# print(df)