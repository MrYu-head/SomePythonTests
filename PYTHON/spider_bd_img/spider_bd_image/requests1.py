# 从百度获取image类型的图片
import requests
import getIp

# 设置请求头
heaser = {}
heaser['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'

# 设置ip代理池
ip = getIp.getIp()
if ip['status'] == 0:
    print('获取ip代理池失败。')
    exit()
ip = ip['ip']
proxies = {"http":f"http://{ip}"}
url = 'https://www.baidu.com'
r = requests.get(headers=heaser,proxies=proxies,url=url)

# 查看状态吗
status = r.status_code
r.encoding = 'utf-8'
print(status)
status = r.status_code
print(r.url)

# 返回cookie
print(r.text)
with open('./baidu1.html','w',encoding='utf-8') as f:
    f.write(r.text)
try:
    print(r.json())
except Exception as e:
    print(e)
print(r.headers)
print(r.encoding)
if status == 200:
    pass
else:
    print('状态码异常，请求失败',status)
    












