# 模块
import random
# from..import  从模块中导入一个指定的部分到当前空间
# from modname import name
# 起别名：import...as

# 导入text.py模块中的add()方法
# import test
# # from test import add
# result = test.add(1,2)
# print(result)

# from Test import test
# print(test.info1(1,5))
# print(test.info2())




################
# 常用模块
# import random
# # 随机生成0-1之间的浮点数
# print(random.random())
# # 用于生成一个指定范围内的整数，a是下限，b是上限
# print(random.randint(1,3))
#
# import math
# print(math.pi)
# # 返回一个大于等于参数的最小整数
# print(math.ceil(5.3))
# # 取小于等于茶树的最大整数
# print(math.floor(7.2))
# # 返回x的y次方
# print(math.pow(3,2))
# # 求x的平方根  开根号
# print(math.sqrt(9))


# time  datetime  calender模块可以处理日期和时间
# import time
# t = time.time()
# print('当前时间戳为：',t)
# # print(time.strftime('%Y-%m-% %H:%M:%S'))
# # 获取当前时间，将时间戳传递给函数
# localtime = time.localtime(time.time())
# print('本地时间为：',localtime)
# # 获取格式化的时间
# ltime = time.asctime(time.localtime(time.time()))
# print(ltime)
# # 格式化日期
# print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
# print(time.strftime("%a %b %d %H %S %Y",time.localtime()))
# # 将格式字符串转换为时间戳
# a = "Sat Mar 28 22:24:24 2022"
# print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))

#
# from datetime import datetime
# # 获取当前日期
# now = datetime.now()
# print(now)
# print(type(now))














