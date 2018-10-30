# -*- encoding: utf-8 -*-

import pymysql
import mysql.connector

##连接数据库
# # 打开数据库连接
# db = pymysql.connect("localhost", "root", "zkyr1006", "Python")
#
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
#
# # 使用 execute()  方法执行 SQL 查询
# cursor.execute("SELECT VERSION()")
#
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
#
# print("Database version : %s " % data)
#
# # 关闭数据库连接
# db.close()

# 打开数据库连接
#conn=mysql.connector.connect(user='root',passwd='zkyr1006',database='python')

conn=pymysql.connect(host='localhost',
    port=3306,
    user='root',
    passwd='zkyr1006',
    db='python',
    charset='utf8'  )

#获取游标
cursor=conn.cursor()

# #插入数据到表中
# cursor.execute('''insert into people_data (name,hometown,birthday,age) values ('吴亦凡','内陆','1992-11-14',26)''')

#删除数据
# try:
#     cursor.execute('''delete from people_data where name='吴亦凡' ''')
#     conn.commit()
# except Exception as e:
#     print (e)
#     #事务回滚，即出现错误后，不会继续执行，而是回到程序未执行的状态，原先执行的也不算了
#     conn.rollback()

#数据库中查询
#a="select * from people_data"  #查询全部
#a="select name,age from people_data"  #查询指定列
# a='select distinct * from douban_books'  # 使用distinct可以消除重复的行
#a="select * from people_data where name !='钟汉良' and age<30"   #按条件查询
#a="select * from people_data where name like '钟%'"    #模糊查询
# a="select * from people_data where age between 20 and 30"  #范围查询
# a="select * from people_data where age is null "   #判空
#删除重复数据
a='''delete from douban_books where id in (select id from (select id from douban_books where id not in (select min(id) from douban_books group by title)) as temple);'''
cursor.execute(a)
conn.commit()
# 删除原有主键：
a='''ALTER  TABLE  `douban_books` DROP `id`;'''
cursor.execute(a)
conn.commit()
# 添加新主键字段：
a='''ALTER  TABLE  `douban_books` ADD `id` MEDIUMINT( 8 ) NOT NULL  FIRST;'''
cursor.execute(a)
conn.commit()
# 设置新主键：
a='''ALTER  TABLE  `douban_books` MODIFY COLUMN  `id` MEDIUMINT( 8 ) NOT NULL  AUTO_INCREMENT,ADD PRIMARY  KEY(id)'''
cursor.execute(a)
conn.commit()

# cursor.execute(a)
# print(cursor.rowcount)  #打印执行结果的条数
# rr=cursor.fetchall()
# for i in rr:
#     print(i)
#
# #修改数据
# #cursor.execute("UPDATE people_data SET age='38',birthday='1980-11-14' WHERE name='乔振宇'")
#
# #提交到数据库执行
# conn.commit()

# 关闭数据库连接，关闭游标
conn.close()
cursor.close()




