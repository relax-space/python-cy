import pymongo

conn = pymongo.mongo_client.MongoClient(host='***')

# print(conn)

# 验证身份users authenticated
user_db = conn['admin']
user_db.authenticate('**','****')
# print(conn.list_database_names())

# 选一个数据库
db = conn['order-service']
# print(db)

# 查询
result = db.orders.find({"uid":{"$regex":"^db3a5b3b.*"}})
# print(result) <pymongo.cursor.Cursor object at 0x027FDFF0>
# for res in result:
#     print(res)

result = db.orders.find_one({"uid":{"$regex":"^db3a5b3b.*"}})
# print(result)

# 插入
# result = db.orders.insert({"uid":"123"})
# print(result)

# 删除
# result = db.orders.delete_one({"uid":"123"})
# print(result)


# 修改
# result['customer']['name'] = '木棉花'
# update_res = db.orders.update({"uid":{"$regex":"^db3a5b3b.*"}},result)
# print(update_res)










conn.close()


