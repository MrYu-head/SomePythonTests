from flask import *
import cx_Oracle
import json

'''
 flask是为了设置不同的路由，以此来实现静态路由访问
 cx_Oracle是为了和oracle'数据库进行交互
首先在前端输入，然后提交按钮ajax发送请求和json格式的数据到服务器，服务器调用对应的
路由方法解析数据，将数据和数据库中比对
'''

app = Flask(__name__)

# 设置数据库服务：
db_conn = cx_Oracle.connect('scott','111111','127.0.0.1:1521/orcl')
db_cur = db_conn.cursor()


# 根路由：login:/login
@app.route('/login',method=['POST'])
def login():
    # 获取前端的jsondata
    data = request.get_data()
    print('这是data:',data)
    json_data = json.loads(data)
    print(json_data)
    # if request.method == 'POST':
    #     # 表单发送的请求数据
    #     unm = request.form['username']
    #     pwd = request.form['password']
    #     print('这是username：',unm)
    #     print('这是password：',pwd)
    #     return redirect(url_for('success',username = unm,password = pwd))
    # else:
    #     print('失败')

# # view(展示) :/view
# @app.route('/view')
# def view():
#     print('hhh')
# # register :/register
# @app.route('/register')
# def register():
#     print('hhh')


if __name__ == '__main__':
    app.run()
