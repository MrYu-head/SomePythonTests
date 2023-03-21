import cx_Oracle

db_conn = cx_Oracle.connect('scott','111111','127.0.0.1:1521/orcl')
db_cursor = db_conn.cursor()
# db_cursor = db_conn.cursor()

# 单行查询
# sql_one = 'select * from sc'
# db_cursor.execute(sql_one)
# print(db_cursor.fetchone())


# 多行查询
# sql_more = 'select * from sc'
# db_cursor.execute(sql_more)
# print(db_cursor.fetchall())


# 带参查询
# sql_dc = 'select * from sc where sno =: abcd'
# sql_dc_sno = {'abcd' : 's002'}
# db_cursor.execute(sql_dc,sql_dc_sno)
# # print(db_cursor.fetchone())
# for i in db_cursor:
#     print(i)

# # 输入一个员工号，查询该员工得信息
# sql_emp ='select * from emp where empno =: eee'
# sql_eee = {'eee' : input('请输入员工号：')}
# db_cursor.execute(sql_emp,sql_eee)
# print(db_cursor.fetchone())



# DML操作
# # 插入一条数据：
# sql_ins_sc_one = 'insert into sc values(:sno,:cno,:score)'
# db_cursor.execute(sql_ins_sc_one,('s010','c010',100))

# 插入多条数据：
# sql_ins_sc_more = 'insert into sc values(:sno,:cno,:score)'
# db_cursor.executemany(sql_ins_sc_more,[('s010','c011',89),('s010','c012',69),('s011','c010',93)])

# db_conn.commit()



# 调用存储过程
# create or replace procedure p1(v1 in varchar2,v2 out varchar2)
# is
# begin
#   v2 := v1;
# end;
# str = 'abcd'
# msg = db_cursor.var(cx_Oracle.STRING)
# db_cursor.callproc('p1',[str,msg])
# db_conn.commit()
# print(msg)
# print(msg.getvalue())


# 调用函数
# create or replace procedure p1(v1 in varchar2,v2 out varchar2)
# is
# begin
#   v2 := v1;
# end;
str = db_cursor.callfunc('f1',cx_Oracle.STRING,['aaa','bbb'])
print(str)
db_conn.commit()







db_cursor.close()
db_conn.close()
