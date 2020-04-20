# json字符串，dict，对象，之间的相互转换


# json和dict之间互相转化
import json
a = {'name':'zhangsan','age':12}

trans_json =json.dumps(a)
print(trans_json)
print(type(trans_json))

trans_dict = json.loads(trans_json)

print(type(trans_dict))
print(trans_dict)


# dict和对象相互转换


# json和对象互相转换
# class User(object):
#     def __init__(self):
#         self.name = ''
#         self.age = 0


# user = User()
# user.__dict__ = trans_dict
# print('name: '+ user.name,'age: '+ user.age)









