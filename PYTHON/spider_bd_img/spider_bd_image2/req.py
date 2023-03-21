import requests
import getProxyIp

# 设置请求头
header = {}
header['User_Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'

# 避免反爬机制，使用ip代理进行访问
ip = getProxyIp.getProxyIp()
if ip['status'] == 0:
    print('获取代理ip失败。')
    exit()
print('*'*30)
ip = ip['ip']
proxies = {"http":f"http://{ip}"}
url = 'https://www.vmall.com/index.html'
r = requests.get(headers=header,proxies=proxies,url=url)

status = r.status_code
r.encoding = 'utf-8'
print('状态码：',status)
print(r.url)

print(r.text)
with open('./hwsc.txt','w',encoding='utf-8') as f:
    f.write(r.text)
try:
    print(r.json())
except Exception as e:
    print(e)
print(r.headers)
print(status)
print(r.encoding)
if status == 200:
    pass
else:
    print('状态码异常，请求失败.',status)





