# python高效编程技巧

# if n%2==0:取出是2的倍数，是的话就是true
# if n%2:取出n除以2是否有余数，有余数就为true

# 1.交换变量
a = 1
b = 2
a,b = b,a
print(a,b)


# 2.列表推导式、字典推导式、集合推导式
list1 = [1,2,3,4,5]
# res1 = [n+1 for n in list1 if n%2==0]
# print(res1)

list2 = [1,2,3,4,5,2,5,1,4,8]
# res = [n for n in list2 if n%2==0]
# print(res)
set = {n for n in list2 if n%2==0}
print(set)  #集合是不可变的,可以去重

dict = {x:x%2 == 0 for x in range(1,11)}
# 创建了一个不重复的1-10之间的整数，value是布尔类型
print(dict)

# 用简单方法创建一个集合：
set1 = {1,2,3,4,3,2,5}
print(set1)


# 3.计数时使用Counter计数对象
from collections import Counter
c = Counter('Hello World')
print(c)
# 查看最多的几个:
print(c.most_common(1))


# 4.打印JSON  indent参数
import json
data = [
    {"age": 27, "name": "Oz", "lactose_intolerant": "true"}, 
    {"age": 29, "name": "Joe", "lactose_intolerant": "false"}
    ]
print(json.dumps(data))
print('*'*20)
print(json.dumps(data,indent=2))


print('*'*40)
# 5.解决FizzBuzz:
'''
    写一个程序，打印数字1到100，
    3的倍数打印“Fizz”来替换这个数，5的倍数打印“Buzz”，
    对于既是3的倍数又是5的倍数的数字打印“FizzBuzz”
'''
for x in range(1,101):
    print("fizz"[x%3*len('fizz')::]+"buzz"[x%5*len('buzz')::] or x)

list = []
for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        list.append(str(i) + 'fizzbuzz')
    elif i%3 == 0:
        list.append(str(i) + 'fizz')
    elif i%5 == 0:
        list.append(str(i) + 'buzz')
    else:
        list.append(str(i))
print(list)


# 6.if语句在行内
print("Hello" if True else "World")


# 7.连接
nfc = ["Packers", "49ers"]
afc = ["Ravens", "Patriots"]
print(nfc + afc)

print(str(1) + "world")

# print(`1` + "world")

print(1,'world')

print(nfc,1)


# 8.数值比较
x = 2
if 3 < x < 1:
    print(x)
y = 2
if 1 < y > 0:
    print(y)


# 9.同时迭代两个列表  zip(list1,list2)
nfc = ["Packers", "49ers"]
afc = ["Ravens", "Patriots"]
for t1,t2 in zip(nfc,afc):
    print(t1 + ' vs ' + t2)



# 10.带索引的列表迭代
teams = ["Packers", "49ers", "Ravens", "Patriots"]
for index,team in enumerate(teams):
    print(index,team)


# 11.初始化列表的值
list3 = [0]*3
print(list3)


# 12.列表转换为字符串
teams = ["Packers", "49ers", "Ravens", "Patriots"]
print(','.join(teams))


# 13.从字典中获取元素
dict2 = {'name':'张三','age':18,'sex':'男'}
is_admin = dict2.get('admin',False)
print(is_admin)


# 14.获取列表的子集
list4 = [1,2,3,4,5,6]
print(list4[:3])  #前三个
print(list4[1:5])  #中间四个
print(list4[3:])  #最后三个
print(list4[::2])  #奇数项
print(list4[1::2])  #偶数项


# 15.迭代工具  itertools,可求出不同的组合方式
from itertools import combinations
teams = ["Packers", "49ers", "Ravens", "Patriots"]
for game in combinations(teams,2):
    print(game)


# 16.False == True
False == True
if False:
    print('Hello')
else:
    print('World')





