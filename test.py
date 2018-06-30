import mysql.connector

# conn=mysql.connector.connect(user='root',passwd='wxy456456')
# cursor=conn.cursor()
#
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# cursor.execute('insert into user (id, name) values (%s, %s)', ('1', 'Michael'))
# conn.commit()
# cursor.close()
#
# # 运行查询:
# cursor = conn.cursor()
# cursor.execute('select * from user where id = %s', ('1',))
# values = cursor.fetchall()
# print(values)
# # 关闭Cursor和Connection:
# cursor.close()
# conn.close()


# import time
#
# try:
#     # 连接数据库
#     con = mysql.connector.connect(host='localhost', port=3306, user='root',
#                                   password='wxy456456', database='mldn', charset='utf8')
#     print(con.connection_id)
#     time.sleep(5)
#     # 断开
#     con.close()
# except mysql.connector.Error as e:
#     print(format(e))
conn = mysql.connector.connect(user='root', password='wxy456456', database='mldn')

cursor = conn.cursor()
# 创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ('1', 'Michael'))
print('rowcount =', cursor.rowcount)
# 提交事务:
conn.commit()
cursor.close()

# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
# 关闭Cursor和Connection:
cursor.close()
conn.close()