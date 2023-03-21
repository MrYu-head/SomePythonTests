import requests
def getIp():
    res = {}
    # 获取ip代理，以json格式展示
    r = requests.get('https://bz.nulls.cn/getIpProxy')
    if r.status_code == 200:
        # 转换成json格式
        jso = r.json()
        print(jso['data']['proxy'])
        res['status'] = 1
        # 将请求的ip替换成代理ip
        res['ip'] = jso['data']['proxy']
    else:
        print('状态码异常，请求失败',r.status_code)
        res['status'] = 0
    return res


# {'data':
#      {
#          'anonymous': '', 'check_count': 286, 'fail_count': 0, 'https': True, 'last_status': True,
#         'last_time': '2023-01-08 07:30:45',
#          'proxy': '204.155.95.87:8080', 'region': '', 'source': 'freeProxy02'
#      },
#  }