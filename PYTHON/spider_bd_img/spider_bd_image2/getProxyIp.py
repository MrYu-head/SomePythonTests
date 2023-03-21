import requests
def getProxyIp():
    # 声明一个结果集，用于存放从ip池获取到的状态和ip
    res = {}
    r = requests.get('https://bz.nulls.cn/getIpProxy')
    if r.status_code == 200:
        # 请求成功，将结果集存储为json格式，并添加到res结果集中
        json = r.json()
        print(json['data']['proxy'])
        # 如果获取代理池ip成功，则添加一个状态码进行识别
        res['status'] = 1
        res['ip'] = json['data']['proxy']
    else:
        print('状态码错误，请求失败。',r.status_code)
        res['status'] = 0
    return res