import pymysql

conn = pymysql.connect(host='***',user='root',password='**',database='***')



# 查询
query_row = conn.query('select * from orders limit 1')
print(query_row) #1

cursor = conn.cursor()

query_data = cursor.execute('select * from orders limit 1 ')
print(query_data) #2878

data = cursor.fetchone()

print(data)

query_data_2 = cursor.execute('select channel_code from channel')

data_2 =cursor.fetchmany(size=2)
print(data_2)


#插入，修改,删除
sql = 'update distribute_brand set grab_type = "A" where brand_code = "NC" and tenant_code = "pangpang"'

try :
    cursor.execute(sql)
    conn.commit()
except:
    conn.rollback()