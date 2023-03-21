import pymysql
from flask import Flask,request
import json
from flask_cors import CORS
# import scores

# 1.1创建app应用程序
app = Flask(__name__)
# 1.2跨域设置
CORS(app = app)
# 1.3开启debug模式
app.debug = True

db = pymysql.connect(host='localhost',user='root',password='111111',database='pythontest')
cursor = db.cursor()

# 1.4设置路由
@app.route('/addUser',methods=['POST'])  #设置请求头和请求方式
@app.route('/delUser',methods=['POST'])
# @app.route('/modify',methods=['POST'])
# @app.route('/view',methods=['POST'])

def addUser():
    # 2.1 获取data数据
    req_data = request.get_data()
    # 2.2 将获取的前端的数据转换为json格式
    data = json.loads(req_data)
    print('这是获取到的数据',data)
    try:
        # 2.3 将json中的数据作为插入的数据传递到sql语句中
        sql_add_data = (data['username'],data['password'],int(data['age']))
        add_sql = 'insert into user_info(username,password,age) values(%s,%s,%s)'
        # 2.4 游标执行
        cursor.execute(add_sql,sql_add_data)
        db.commit()
        # 2.5 向前端发送状态信息
        print('*'*100)
        return {'code':200,'msg':'添加用户成功！'}
    except Exception as e:
        db.rollback()
        return {'code':000,'msg':'用户添加失败！'}


# url传参方式删除数据
def delUser():
    delete_username = request.args.get('username')
    delete_password = request.args.get('password')
    print('这是用户名：',delete_username)
    print('这是密码：',delete_password)
    print('%'*100)
    del_sql = f'delete from `user_info` where username = "{delete_username}" and password = "{delete_password}"'
    try:
        print('%'*100)
        cursor.execute(del_sql)
        db.commit()
        return {'code':200,'msg':'删除用户成功！s'}
    except Exception as e:
        db.rollback()
        return {'code':000,'msg':'删除用户失败！'}
        



# json格式删除数据：
# def delUser():
#     # 获取data数据
#     req_data = request.get_data()
#     # 加载为json格式
#     data = json.loads(req_data)
#     try:
#         sql_del_data = (data['username'],data['password'])
#         del_sql = 'delete from user_info where username = %s and password = %s'
#         cursor.execute(del_sql,sql_del_data)
#         print('*'*60)
#         db.commit()
#         return {'code':200,'msg':'删除用户成功！'}
#     except Exception as e:
#         db.rollback()
#         return {'code':000,'msg':'删除用户失败！'}

        



if __name__ == '__main__':
    app.run(host='localhost',port='8090')
    # 关闭游标和数据库连接
    cursor.close()
    db.close()












# # 添加
# def add():
#     # 插入多条数据
#     # 每次调用函数建议先测试一下数据库和游标是否在打开状态:
#     db = pymysql.connect(host='localhost',user='root',password='111111',database='pythontest')
#     # 创建游标对象
#     cursor = db.cursor()
#     add_sql = 'insert into user_info(username,password,age) values(%s,%s,%s)'
#     username = input('输入username：')
#     password = input('输入password：')
#     age = int(input('请输入年龄：'))
    
#     array = [
#         # 多组数据需要列表包含元组的形式传递
#         (username,password,age),
#         # ('章鱼哥',13,'语文系','卓球'),
#         # ('蟹老板',13,'英文系','羽毛球')
#     ]
#     try:
#         cursor.executemany(add_sql,array)
#     except Exception as e:
#         db.rollback()
#         print(add_sql,e)
#     # 提交事务
#     db.commit()
#     # 每次函数尾部关闭游标
#     cursor.close()
#     print('添加用户成功!')
#     pyMysql()

# # 删除
# def delete():
#     db = pymysql.connect(host='localhost',user='root',password='111111',database='pythontest')
#     cursor = db.cursor()
#     del_sql = 'delete from user_info where username = %s'
#     del_name = input('请输入要删除的用户的姓名')
#     del_name_array = [(del_name)]
#     try:
#         cursor.execute(del_sql,del_name_array)
#     except Exception as e:
#         db.rollback()
#         print(del_sql,e)
#     db.commit()
#     cursor.close()
#     print('删除用户成功!')
#     pyMysql()

# # 修改
# def modify():
#     db = pymysql.connect(host='localhost',user='root',password='111111',database='pythontest')
#     cursor = db.cursor()
#     midify_sql = 'update user_info set username = %s where username = %s '
#     old_name = input('请输入要修改的用户的姓名：')
#     mod_name = input('请输入修改后的姓名：')
#     mod_name_array = [
#         (mod_name),
#         (old_name)
#     ]
#     try:
#         cursor.execute(midify_sql,mod_name_array)
#     except Exception as e:
#         db.rollback()
#         print(midify_sql,e)
#     db.commit()
#     cursor.close()
#     print('修改用户信息成功!')

#     pyMysql()

# # 查看 select
# def view():
#     db = pymysql.connect(host='localhost',user='root',password='111111',database='pythontest')
#     cursor = db.cursor()
#     view_sql = 'select * from user_info where username = %s'
#     view_name = input('请输入要查看信息的用户名:')
#     view_name_array = [(view_name)]
#     try:
#         cursor.execute(view_sql,view_name_array)
#         for i in cursor:
#             print('用户信息如下：',i)
#     except Exception as e:
#         db.rollback()
#         cursor.close()
#         pyMysql()
        

# # 获取自增的id
# # print(cursor.lastrowid)
# # cursor.close()
# # db.close()

# def pyMysql():
#     print('*' * 20)
#     print('可进行如下操作：\n'
#          + '  1----添加用户\n'
#          + '  2----删除用户\n'
#          + '  3----修改用户信息\n'
#          + '  4----查看用户信息\n'
#          + '  5----退出系统')
#     print('*' * 20)
#     tab = int(input('请输入要进行的操作：'))
#     if tab == 1:
#         add()
#     elif tab == 2:
#         delete()
#     elif tab == 3:
#         modify()
#     elif tab == 4:
#         view()
#     elif tab == 5:
#         exit()
#     else:
#         print('输入的指令不正确，请重试')
#         pyMysql()
# 
# pyMysql()
#