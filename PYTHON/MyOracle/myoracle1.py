import cx_Oracle
from datetime import date
db_conn = cx_Oracle.connect('scott','111111','127.0.0.1:1521/orcl')

# 简单查询
# db_cursor = db_conn.cursor()
# sql_cmd = 'select * from emp'
# db_cursor.execute(sql_cmd)
# for row in db_cursor:
#     print(row)
#
# db_cursor.close()
# db_conn.close()

# db_cursor = db_conn.cursor()
# sql_cmd = 'select * from emp'
# db_cursor.execute(sql_cmd)
# for r in db_cursor:
#     print(r)
# db_cursor.close()
# db_conn.close()


# 带参数查询
# db_cursor = db_conn.cursor()
# sql_cmd = 'select * from emp where empno =: a'
# sql_p_empno = {'a' : 7499}
# db_cursor.execute(sql_cmd,sql_p_empno)
# for row in db_cursor:
#     print(row)
# db_cursor.close()
# db_conn.close()


# 获取单行数据可以使用fetchone()函数  获取多条记录使用fetchall()函数
# 1.获取单行  fetchone()
# db_cursor = db_conn.cursor()
# sql_cmd = 'select * from student'
# db_cursor.execute(sql_cmd)
# print(db_cursor.fetchone())
# db_cursor.close()
# db_conn.close()

# 2.获取全部
# db_cursor = db_conn.cursor()
# sql_cmd = 'select * from student'
# db_cursor.execute(sql_cmd)
# print(db_cursor.fetchall())
# db_cursor.close()
# db_conn.close()


# oracle的DML  update、delete、insert
from datetime import datetime
db_cursor = db_conn.cursor()
# # insert
# 1.
# sql = "insert into emp(hiredate) values(to_date(:hire,'yyyy/MM/dd')) where empno : eno"
# hired = input('请输入日期：')
# eno1 = int(input('请输入员工号:'))
# db_cursor.execute(sql,(hired,eno1))
sql = "insert into emp(hiredate) values(to_date(':a','yyyy/MM/dd')) where empno = 1111"
a = '20221117'
db_cursor.execute(sql)

# t = int(input('请输入：'))
# t = datetime.t
# # now = datetime.now()
# print(t.strftime("%y/%m/%d"))
#
# t = input('请输入：')
# print(datetime.strftime(t,'%y/%m/%d'))


db_conn.commit()
db_cursor.close()
db_conn.close()


# 调用存储过程和函数
# 调用存储过程
''' PLSQL代码：
    create or replace procedure p_demo(v1 in varchar2,v2 out varchar2)
    is
    begin
        v2 := v1;
    end;
'''
# db_cursor = db_conn.cursor()
# str = 'abcd'
# msg = db_cursor.var(cx_Oracle.STRING)
# db_cursor.callproc('p_demo',[str,msg])
# db_conn.commit()
# print(msg)
# print(msg.getvalue())
# db_cursor.close()
# db_conn.close()

# 调用存储过程查询指定员工编号的员工信息
# db_cursor = db_conn.cursor()
# eno = int(input('请输入一个员工编号:'))
# msg = db_cursor.var(cx_Oracle.DB_TYPE_)
# db_cursor.callproc('p_test',[eno,msg])
# db_conn.commit()
# # print(msg)
# print(msg.getvalue())
# db_cursor.close()
# db_conn.close()



# 函数
# db_cursor = db_conn.cursor()
# str = db_cursor.callfunc('f_test',cx_Oracle.STRING,['abc','def'])
# print(str)
# db_conn.commit()
# db_cursor.close()
# db_conn.close()


















