from flask import *  #为了省事，直接导*
import cx_Oracle
import os  #操作系统包，包含普遍的操作系统功能
# 导入数据库扩招，配置文件，转到2.3
from flask_sqlalchemy import SQLAlchemy


# 1 连接oracle数据库
db_conn = cx_Oracle.connect('scott','111111','127.0.0.1:1521/orcl')
# 对应参数为：用户名、密码、数据库地址实例
# 2 创建游标  每次单独执行路由函数的时候打开游标，这样不会导致游标混乱
db_cur = db_conn.cursor()
# 3 根据不同路由创建不同的函数进行增删改查操作
# 3.1 登陆验证
def loginCheck():
    # 3.1.1 每个路由函数调用的时候最好检查一遍数据库连接是否断开
    db_conn = cx_Oracle.connect('scott','111111','127.0.0.1:1521/orcl')
    db_cur = db_conn.cursor()
    # 3.1.2 写sql语句,其中name和pwd是从前端ajax发送来的输入的用户名和密码
    sql_login_check = 'select * from user_infor_table where username := name and password := pwd'
    web_data = {'name':'web_username','pwd':'web_password'}
    # 3.1.3 游标执行sql语句
    try:
        # 此处放在异常捕获中是为了判断情况
        db_cur.execute(sql_login_check,web_data)
    except Exception as e:
        print('验证失败，请重试。')
    




# 2.1 创建app应用
app = Flask(__name__)

# 2.2 创建路由，路由指的是访问路径，不同路由指向不同的页面
@app.route('/login')
def login():
    return 'successful'

# 2.3 工程配置信息
class Config(object):
    """工程配置信息"""
    debug = True
    # 数据库配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
app.config.from_object(Config)


# 2.# 跑服务器
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=3300,debug=True)

# db_conn.close()
