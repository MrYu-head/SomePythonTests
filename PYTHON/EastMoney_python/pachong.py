# 导入requests
import requests

url = 'https://t.bilibili.com/'
strhtml = requests.get(url)
print(strhtml.text)



# post
# import json
# def get_translate_data(word = None):
#     url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

#     From_data = {'i': word, 'from': 'zh-CHS', 'to': 'en', 'smartresult': 'dict', 'client': 'fanyideskweb',
#                  'salt': '15477056211258', 'sign': 'b3589f32c38bc9e3876a570b8a992604', 'ts': '1547705621125',
#                  'bv': 'b33a2f3f9d09bde064c9275bcb33d94e', 'doctype': 'json', 'version': '2.1', 'keyfrom': 'fanyi.web',
#                  'action': 'FY_BY_REALTIME', 'typoResult': 'false'}
#     #请求表单数据
#     response = requests.post(url,data = From_data)
#     #将json格式字符串转换为字典
#     content = json.loads(response.text)
#     print(content)

#     if __name__ == '__main__':
#         get_translate_data('我爱中国')














