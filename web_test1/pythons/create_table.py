import cx_Oracle

db_conn = cx_Oracle.connect('scott','111111','127.0.0.1:1521/orcl')

db_cur = db_conn.cursor()

sql = 'create table user_infor_table (id int,username varchar2(20),password varchar2(30))'

db_cur.execute(sql)

db_cur.close()
db_conn.close()


