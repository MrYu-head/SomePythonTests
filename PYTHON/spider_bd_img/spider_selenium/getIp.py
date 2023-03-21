import requests
def getIp():
    res = {}
    # 获取ip连接池，以json格式展示
    r = requests.get('https://bz.nulls.cn/getIpProxy')
    if r.status_code == 200:
        # 把ip连接池以json格式输出
        json = r.json()
        print(json['data']['proxy'])
        res['status'] = 1
        # 将请求的ip替换成代理ip
        res['ip'] = json['data']['proxy']
    else:
        print('状态码异常，请求失败',r.status_code)
        res['status'] = 0
    return res


