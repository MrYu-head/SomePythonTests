# 客户端

import requests
# import app

def client_post(url,data):
    rep = requests.post(url,data = data)
    return rep.text

if __name__ == '__main__':
    url1 = 'http://127.0.0.1:3300/server'
    url2 = 'http://127.0.0.1:3300/'
    data = {'key1':'张三','key2':'李四','key3':'王五'}
    res1 = client_post(url1,data)
    res2 = client_post(url2,data)

    print('127.0.0.1:3300/server:',res1)
    print('127.0.0.1:3300/:',res2)
