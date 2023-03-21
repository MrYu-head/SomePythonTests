
# import requests

# req = requests.get('http://www.runoob.com')
# print(req.text)
# # 返回页面编码方式
# print(req.apparent_encoding)
# print(req.apparent_encoding)
# # 获取http状态码
# print(req.status_code)
# print(req.status_code)
# # 返回响应头，以字典格式返回
# print(req.headers)
# # 查看相应是否被重定向  是返回true，否返回false
# print(req.is_redirect)
# # 返回结果的json对象  以json格式编写
# # print(req.json())
# # 返回此相应的请求对象
# print('------------------------------')
# print(req.request)
# # 返回响应的url
# print(req.url)



# # 请求json数据文件，返回json内容
# req_json = requests.get('https://www.runoob.com/try/ajax/json_demo.json')
# # 返回json数据
# print('---------------------')
# print(req.json())



import requests
import getIp
# 设置一下请求头
header = {}
header['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'

# 从连接池获取ip
ip = getIp.getIp()
if ip['status'] == 0:
    print('获取代理池ip失败')
    exit()
ip = ip['ip']
proxies = {"http" : f"http://{ip}"}

r = requests.get(headers=header,proxies=proxies,url='http://www.baidu.com')
# 查看状态码
status = r.status_code
r.encoding = 'utf-8'
print(status)
status = r.status_code
# 请求的url地址
print(r.url)

# 返回cookie信息
print(r.text)
with open('./baidu1.html','w',encoding='utf-8')as f:
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
























