import cx_Oracle
db_conn = cx_Oracle.connect('scott','111111','127.0.0.1:1521/orcl')
db_cursor = db_conn.cursor()
# 游标查询学生表信息
# 当学生表不存在时执行建表语句
# 新建学生表
sql_create = 'create table stuList(' \
                 'sno varchar2(10),' \
                 'sname varchar2(20),' \
                 'age number(4),' \
                 'sex varchar2(4))'
db_cursor.execute(sql_create)

db_cursor.close()
db_conn.close()