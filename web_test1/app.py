from flask import request
import web

urls = (
    # '/(.*)', 'hello',
    '/login','LoginCheck'
)
app = web.application(urls, globals())

class hello:
    def GET(self,name):
        if not name:
            name = 'World'
        return 'Hello'

class LoginCheck:
    def login(self):
        req = request.get_json()
        print('data:',req)

if __name__ == "__main__":
    app.run()