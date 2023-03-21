
# python转换为json

import json
# data = {
#     'no' : 1,
#     'name' : 'runoob',
#     'url' : 'http://www.runoob.com'
# }
# # 将数据编码为json格式
# json_str = json.dumps(data)
# print('python原始数据：',repr(data))
# print('json对象:',json_str)




# json格式转换为python格式
# data1 = {
#     'no' : 1,
#     'name' : 'Runoob',
#     'url' : 'http://www.runoob.com'
# }
# json_str1 = json.dumps(data1)
# print('python原始数据:',repr(data1))
# print('json对象:',json_str1)

# # 将json对象转换为python字典
# data2 = json.loads(json_str1)
# print("data2['name']:",data2['name'])
# print("data2['url']",data2['url'])





# -*- coding:utf-8 -*-
import requests
import bs4
 
 
def get_web(url):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.59"}
    res = requests.get(url, headers=header, timeout=5)
    # print(res.encoding)
    content = res.text.encode('ISO-8859-1')
    return content
 
 
def parse_content(content):
    soup = bs4.BeautifulSoup(content, 'lxml')
 
    '''
    存放天气情况
    '''
    list_weather = []
    weather_list = soup.find_all('p', class_='wea')
    for i in weather_list:
        list_weather.append(i.text)
 
    '''
    存放日期
    '''
    list_day = []
    i = 0
    day_list = soup.find_all('h1')
    for each in day_list:
        if i <= 6:
            list_day.append(each.text.strip())
            i += 1
    # print(list_day)
 
    '''
    存放温度：最高温度和最低温度
    '''
    tem_list = soup.find_all('p', class_='tem')
    i = 0
    list_tem = []
    for each in tem_list:
        if i == 0:
            list_tem.append(each.i.text)
            i += 1
        elif i > 0:
            list_tem.append([each.span.text, each.i.text])
            i += 1
    # print(list_tem)
 
    '''
    存放风力
    '''
    list_wind = []
    wind_list = soup.find_all('p', class_='win')
    for each in wind_list:
        list_wind.append(each.i.text.strip())
    # print(list_wind)
    return list_day, list_weather, list_tem, list_wind
 
 
def get_content(url):
    content = get_web(url)
    day, weather, tem, wind = parse_content(content)
    item = 0
    for i in range(0, 7):
        if item == 0:
            print(day[i]+':\t')
            print(weather[i]+'\t')
            print("今日气温："+tem[i]+'\t')
            print("风力："+wind[i]+'\t')
            print('\n')
            item += 1
        elif item > 0:
            print(day[i]+':\t')
            print(weather[i] + '\t')
            print("最高气温："+tem[i][0]+'\t')
            print("最低气温："+tem[i][1] + '\t')
            print("风力："+wind[i]+'\t')
            print('\n')
 
 