import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()  # 谷歌浏览器的对象
# # driver.get('https://taobao.com/')
# # btn = driver.find_element(By.XPATH, value='/html/body/div[3]/div[2]/div[2]/div[2]/div[5]/div/div[2]/div[1]/a[1]')
# # btn.click()


# 百度图片
driver = webdriver.Chrome()
url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=detail&fr=&hs=0&xthttps=111110&sf=1&fmq=1673416762751_R&pv=&ic=0&nc=1&z=&se=&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E8%A1%A8%E6%83%85%E5%8C%85&oq=%E8%A1%A8%E6%83%85%E5%8C%85&rsp=-1'


driver.get(url) 
input('1111')
# 调用js下滑页面
print('--------------------------------------')
js = "var d = document.documentElement.scrollTop=3000"
driver.execute_script(js)

input()
print('--------------------------------------')
btn = driver.find_elements(By.CLASS_NAME,value='main_img')
# print('+++++++++++++++',btn[0])

print('这是长度*************************************************',len(btn))
for i in range(0,len(btn)):
    url1 = btn[i].get_attribute('src')
    print(url1)
    # 如果获取到的不是图片，则抛出异常跳过
    try:
        r = requests.get(url1)
        content = r.content
        with open(f'./img/{i}.jpg','wb') as f:
            f.write(content)
    except Exception as e:
        print(e)
        pass










