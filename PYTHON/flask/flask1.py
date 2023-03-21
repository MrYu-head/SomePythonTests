from flask import Flask,redirect,url_for,request
import requests
app = Flask(__name__)

# 主页
@app.route('/')
def indexHtml():
    return '这里是主页。'

@app.route('/hello')
def hello():
    return 'Hello World!'

# @app.route('/hello/<name>')
# def hello1(name):
#     return 'Hello World:' + name


# @app.route('/admin/<adminv>')
# def hello_admin(adminv):
#     return 'Hello World Admin:' + adminv

# @app.route('/guest/<guestv>')
# def hello_guest(guestv):
#     return 'Hello World Guest::' + guestv

# @app.route('/user/<name>')
# def hello_user(name):
#     if name == 'admin':
#         return redirect(url_for('hello_admin',adminv = name))
#     else:
#         return redirect(url_for('hello_guest',guestv = name))


# 表单输入
# @app.route('/form',methods=['GET','POST'])
# def form():
#     print('请求方式：',request.method)
#     # 获取form中的所有参数,以列表形势存放
#     param = request.form
#     print('传过来的参数是', param)
#     print('text_name的值:', param.get('text_name'))
#     file = request.files['file_name']
#     print(file)
#     print(file.filename)
#     file.save(f'./{file.filename}')

#     file = request.files['file_name1']
#     print(file)
#     print(file.filename)
#     file.save(f'./{file.filename}')
#     return str('OK')


@app.route('/form')
def getForm():
    print('请求方式：',request.method)
    param = request.form
    print('请求到的参如下：',param)
    text = param['text_name']
    print('获取到的内容为：',text)
    text.save(f'./{text.filename}')
    return str('OK')





if __name__ == '__main__':
    app.run(host='127.0.0.10',port=1000,debug=False)


