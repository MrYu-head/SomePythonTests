import requests
import getIp
import time

def clTitle(title):
    bhf = ['\\','/',':','*','?','"','<','>','|']
    for i in bhf:
        # 替换特殊字符
        title = title.replace(i,'')
    return title

def chuliImage(data):
    for i in data:
        try:
            print(i['replaceUrl'])
            imgUrl = i['replaceUrl'][0]['objUrl']
            title = clTitle(i['fromPageTtile'])
            try:
                r = requests.get(url=imgUrl,headers={})
                if r.status_code == 200:
                    content = r.content
                    with open(f'./img/{title}.jpg','wb') as f:
                        f.write(content)
                else:
                    print('图片请求失败',r.status_code)
            except Exception as e:
                print('图片请求超时，跳过',e)
        except KeyError as k:
            print('replaceUrl不存在，跳过',k)            
        except Exception as e:
            print('其他错误，跳过',e)

# url头  设置查询的结果
urlHead = 'https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&dyTabStr=MCwzLDYsMSw1LDQsNyw4LDIsOQ%3D%3D&word='
# url尾  设置页数
urlTail = 'cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&expermode=&nojc=&isAsync=&pn='

all = {
    '表情包': ['杰尼龟', '蘑菇头', '沙雕'],
    '壁纸': ['清新', '女生', '']
}
# 设置ip代理池
ip = getIp.getIp()['ip']
proxy = {'http':f'http://{ip}'}
header = {}
header['Cookie'] = 'BDqhfp=%E6%9D%B0%E5%B0%BC%E9%BE%9F%26%26NaN-1undefined%26%260%26%261; BIDUPSID=9405D8DBEF0A8C235D157B9861586C31; PSTM=1657527142; BAIDUID=5DBC9F55E3A06CB880D1B20812E80DA6:FG=1; MCITY=-%3A; indexPageSugList=%5B%22%E9%93%A0%E7%94%B2%E5%8B%87%E5%A3%AB%22%2C%22%E5%88%91%E5%A4%A9%E9%93%A0%E7%94%B2%E5%8D%87%E7%BA%A7%22%2C%22%E5%88%91%E5%A4%A9%E9%93%A0%E7%94%B2%22%2C%22%E5%B8%9D%E7%9A%87%E9%93%A0%E7%94%B2%22%2C%22%E4%BF%AE%E7%BD%97%E9%93%A0%E7%94%B2%22%5D; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_PS_PSSID=26350; delPer=0; PSINO=1; BAIDUID_BFESS=5DBC9F55E3A06CB880D1B20812E80DA6:FG=1; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=www.baidu.com; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; ab_sr=1.0.1_YWYzNDgwN2VjYjhiMWZhMGE1NTdiZDc5NjVhZmMwMDBjYjU1YWJiYmNlNTczNzgzZWRhZTQ1NGY1ZmQwNGU1ZGJmY2Q3N2VhNWM2OWEyYTBlNjcyY2NiNDk3YTI4M2Q3ZDFjODY5MTMzY2E1ZDExNDFlZDg0YTNmNWM5YTJiMzJlNDVkZjk4NjMzMDc3MzJiNTA5ZDVmNjBhNTM2NTAzNw==; BDRCVFR[89NjedbPcJ6]=mk3SLVN4HKm; BA_HECTOR=25a08h0lah8k810h802ha5pu1hrs46k1l; ZFY=xNUJvW:As:AWu:BhSYEBwo4rDb8UjoLiFchmthishmcJ8g:C'
# 设置要抓取的页数
pages = range(30,200,30)
for k,v in all.items():
    big = k
    for small in v:
        for page in pages:
            imgClass = big + ' ' + small
            # 拼接完整地址
            url = urlHead + imgClass + urlTail + str(page)
            r = requests.get(url=url,headers=header,proxies=proxy)
            r.encoding = 'utf-8'
            print(r.status_code)
            data = r.json()['data']
            chuliImage(data)
            time.sleep(1)








