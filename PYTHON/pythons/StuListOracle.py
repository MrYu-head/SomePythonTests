'''
   编写程序，设计“学生管理系统”项目（使用oracle数据库）
   需要完成的基本功能：
   添加学生(包括学号，姓名，年龄，性别,生日)
   删除学生
   修改学生
   查询学生
   退出系统
   程序运行后，除非选择退出系统，否则重复执行功能
'''
# 函数实现功能，替换为execute实现

# 当学生表不存在时执行建表语句
# 新建学生表
# def createTable():
#     sql_create = 'create table stuList(' \
#                      'sno varchar2(10),' \
#                      'sname varchar2(20),' \
#                      'age number(4),' \
#                      'sex varchar2(4),' \
#                     'birthday date)'
#     db_cursor.execute(sql_create)
#     # 遍历学生表
#     for row in db_cursor:
#         print(row)
# def selectStu():
#     db_cursor.execute(sql_select)
#     for result in db_cursor:
#         if result == None:
#             print('学生表不存在。')
#         else:
#             print('学生表存在。')
#             print(result)
# 添加学生
def addStu():
    import cx_Oracle
    db_conn = cx_Oracle.connect('scott', '111111', '127.0.0.1:1521/orcl')
    db_cursor = db_conn.cursor()
    print('======现在进行添加学生操作。')
    sql_add = 'insert into stuList values(:sno,:sname,:age,:sex)'
    newsno = input('请输入学号：')
    newname = input('请输入姓名：')
    newage = int(input('请输入年龄：'))
    newsex = input('请输入性别：')
    db_cursor.execute(sql_add,{'sno':newsno,'sname':newname,'age':newage,'sex':newsex})

    # 判断学生表是否存在，保存在，判断学生是否存在
    sql_selectAll = 'select * from stuList'
    db_cursor.execute(sql_selectAll)
    result = db_cursor.fetchall
    db_conn.commit()
    print('添加成功。')
    db_cursor.close()
    db_conn.close()
def deleteStu():
    import cx_Oracle
    db_conn = cx_Oracle.connect('scott', '111111', '127.0.0.1:1521/orcl')
    db_cursor = db_conn.cursor()
    sno = input('请输入要删除的学生学号：')
    sql_del = 'delete from stuList where sno =: sno'
    db_cursor.execute(sql_del,{'sno' : sno})
    db_conn.commit()
    print('删除成功。')
    db_cursor.close()
    db_conn.close()

def modifyStu():
    import cx_Oracle
    db_conn = cx_Oracle.connect('scott', '111111', '127.0.0.1:1521/orcl')
    db_cursor = db_conn.cursor()
    sno = input('请输入要修改的学生的学号：')
    sql_update = 'update stuList set sname =: sname,age =: age,sex =: sex where sno =: sno'
    sname = input('请输入修改后的姓名：')
    age = input('请输入修改后的年龄：')
    sex = input('请输入修改后的性别：')
    db_cursor.execute(sql_update,{'sno' : sno,'sname' : sname,'age' : age,'sex' : sex})
    db_conn.commit()
    print('修改成功。')
    db_cursor.close()
    db_conn.close()
def checkStu():
    import cx_Oracle
    db_conn = cx_Oracle.connect('scott', '111111', '127.0.0.1:1521/orcl')
    db_cursor = db_conn.cursor()
    sno = input('请输入要查询的学生的学号：')
    sql_select = 'select * from stuList where sno =: sno'
    db_cursor.execute(sql_select,{'sno' : sno})
    result = db_cursor.fetchall()
    for res in result:
        print(res)

    db_cursor.close()
    db_conn.close()
# # 删除学生
# def deleteStu():
#     print('现在进行删除学生的操作.')
#     dno = input('删除学生。请输入要删除的学生的学号:')
#
# # 修改学生
# def modifyStu():
#     print('现在进行修改学生的操作.')
#     btn = input('请输入要修改信息的学生的学号：')  # 根据学号修改学生字典信息，查出userList对应的k,v,然后根据k修改
#     # 修改之前先判断名片字典是否存在
#
# # 查询学生
# def checkStu():
#     check = int(input('1-----查看指定学号学生信息\n2-----查看所有学生信息\n'))
#     # for row in db_cursor:
#     #     # for v_emp in cur:
#     #     if len(row) <= 0:
#     #         print('信息不存在。')
#     #     else:
#     #         print('学生表存在信息。')
#     #         print(row)
#     # else:
#     #     print('学生表不存在。')
#     if check == 1:
#         db_cursor.execute(sql_select)
#         print(db_cursor.fetchall())
#     #     userBtn = input('请输入要查询信息的学生的学号：')   #str
#     #     if len(result) <= 0:
#     #         print('学生表不存在，请先创建表。')
#     #     else:
#     #         sql_selOne = 'select * from stuList where sno =:userBtn'
#     #         # 声明一个变量保存查询的结果
#     #         result2 = db_cursor.execute(sql_selOne,{'userBtn' : userBtn})
#     #         if result2:
#     #             print('查询到该学生的信息：')
#     #             print(result2)
#     #         else:
#     #             print('该学生不存在。')
#     # elif check == 2:
#     #     if len(result) <= 0:
#     #         print('学生表不存在，请先创建表。')
#     #     else:
#     #         # sql_select = 'select * from stuList'
#     #         db_cursor.execute(sql_select)
#     #         print(db_cursor.fetchall())
#     else:
#         print('请输入正确的指令。\n')
while True:
    print('==========学生管理系统==========')
    print('======可进行的操作如下所示：')
    print('1------添加学生')
    print('2------删除学生')
    print('3------修改学生信息')
    print('4------查询学生信息')
    print('5------退出系统\n')
    tab = int(input('======请输入要进行的操作:'))
    if tab == 1:
        addStu()
    if tab == 2:
        deleteStu()
    if tab == 3:
        modifyStu()
    if tab == 4:
        checkStu()
    if tab == 5:
        print('退出系统')
        break




