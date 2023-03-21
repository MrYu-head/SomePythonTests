import cx_Oracle
db_conn = cx_Oracle.connect('scott','111111','127.0.0.1:1521/orcl')

db_cur = db_conn.cursor()
# 1.1查询单条
sql_cmd_one = 'select * from emp where empno := eno'
# 1.2查询所有
# sql_cmd_all = 'select * from emp'
# eno为前端input输入的整数类型的eno

# sql_data = {'eno' : }
# 将查询语句选项放进列表进行选择
# sql_cmd_list = [sql_cmd_one,sqqingl_cmd_all]
# 前端发送来的请求指令

# db_cur.execute(sql_cmd_list[i])

# 2.1返回单条数据
sel_one_data = db_cur.execute(sql_cmd_one)

# 2.2返回多条数据
# sel_all_data = db_cur.fetchall()

db_cur.close()
db_conn.close()



