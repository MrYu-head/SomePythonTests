# import web

# # urls中第一个参数是router路由，第二个参数是该路由对应的类
# # urls = ('/(.*)', 'hello')
# urls = ('/login','Login')
# app = web.application(urls, globals())

# # 登陆类  对应login
# class Login():
#     def GET(self):
#         return 111

# if __name__ == "__main__":
#     app.run()
#     # 默认是127.0.0.1:8080



import web
import client

urls = (
    '/server','server',
    '/.*','notfound'
)

# 重载web.application类，防止端口冲突
class MyApplication(web.application):
    def run(self,port=8080,*middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func,('0.0.0.0',port))

class server:
    def __init__(self):
        self.return_msg = {'errorCode':0,'msg':'系统正常。'}
    
    def POST(self):
        content = web.input()
        print('收到消息，',content.key1,content.key2,content.key3)
        return str(self.return_msg).replace('\'','\"')

class notfound:
    # def GET(self):
    #     print('notfound')
    #     return '404 not found'
    def POST(self):
        print('notfound')
        return '404 not found'
        
if __name__ == '__main__':
    app = MyApplication(urls,globals())
    app.run(port=3300)




