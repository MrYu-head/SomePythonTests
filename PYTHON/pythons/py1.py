'''
  name = '张三'
  age = 19
  print(name,age)
  print(name + '\n今年' + str(age) + '岁了。')
'''

# 1.编写程序，完成以下要求：
# 提示用户进行输入数据-input
# 获取用户的数据数据（需要获取2个）
# 对获取的两个数字进行求和运行，并输出相应的结果

'''
a = int(input('输入第一个数:'))
b = int(input('输入第二个数:'))
print(a + b)
'''

'''
2.编写程序，完成以下要求：
提示用户进行输入数据
获取用户的数据数据（需要获取3个）
按照从小到大输出
'''
'''
a = int(input('输入第一个数:'))
b = int(input('输入第二个数:'))
c = int(input('输入第三个数:'))
if a > b > c:
    print(c,b,a)
elif a > c > b:
    print(b,c,a)
elif b >a >c:
    print(c,a,b)
elif b >c >a:
    print(a,c,b)
elif c >a >b:
    print(b,a,c)
elif c >b >a:
    print(a,b,c)
'''

'''
3. 编写程序，从键盘获取一个人的信息，然后按照下面格式显示
   ==================================
    姓名: 李四
    QQ:xxxxxxx
    手机号:131xxxxxx
    公司地址:北京市xxxx
    ==================================
'''
'''
name = input('输入姓名:')
QQ = input('输入QQ号:')
phone = input('输入手机号:')
address = input('输入地址:')
print('姓名:' + name + '\nQQ:' + QQ + '\n手机号:' + phone + '\n公司地址:' + address)
'''

'''
4.从键盘获取用户名、密码
如果用户名和密码都正确（预先设定一个用户名和密码），
那么就显示“欢迎进入xxx的世界”，否则提示密码或者用户名错误
'''
'''
usnm = '张三'
paw = 111111
username = input('输入用户名:')
password = int(input('输入密码:'))
if (username == usnm) and (password == paw):
    print('欢迎进入傻逼的世界！')
else:
    print('进入傻逼世界失败，你不是傻逼。')
'''

'''
5.设计猜拳
随机数代码如下:
import random
print(random.randint(1,3))  可以随机产生1或2或3
'''
'''
import random
ra = random.randint(1,3);
print(type(ra))
a = int(input('我出1:剪刀，2：石头，3：布:'))
if (a == 1 and ra == 2) or (a == 1 and ra == 3) or (a == 3 and ra == 1):
    print('我出:' + str(a) + '机器出:' + str(ra) + ',机器胜。')
elif a == ra:
    print('我出:' + str(a) + '机器出:' + str(ra) + ',平局。')
else:
    print('我出:' + str(a) + '机器出:' + str(ra) + ',我胜。')
'''

'''
6.编写程序，完成以下要求:
提示用户进行输入数据
获取用户的数据数据（需要是3位数）
判断是否是水仙花数。水仙花数是指一个 3 位数，
它的每个位上的数字的 3次幂之和等于它本身（例如153：1^3 + 5^3+ 3^3 = 153）
'''

# n = int(input('请输入一个三位数:'))
# a = int(n/100)
# b = int(n/10%10)
# c = int(n%10)
# print(a,b,c)
# if (a**3 + b**3 + c**3 == n):
#     print(str(n) + '是水仙花数。')
# else:
#     print(str(n) + '不是水仙花数。')


#####################################################################
#####################################################################
#####################################################################
#####################################################################
#####################################################################

# 1. 计算1~100的和（包含1和100）
# sum = 0
# for i in range(1,101):
#     sum += int(i)
# print(sum)

# 2. 计算1~6的乘积（包含1和6）
# sum = 1
# for i in range(1,7):
#     sum *= i;
# print(sum)

# 3. 计算1~100之间偶数的和（包含1和100）
# sum = 0;
# for i in range(2,101,2):
#     sum += i
# print(sum)

# 4. 计算1~100之间可以被3又能被5整数的数的个数（包含1和100）
# sum = 0
# for i in range(1,101):
#     if (i%3 == 0 and i%5 == 0):
#         sum += 1
# print(sum)

# 5.使用循环，完成以下图形的输出
# *
# * *
# * * *
# * * * *
# * * * * *
# for i in range(1,6):
#     for j in range(1,i+1):
#         print('*',end="")
#     print()

# 6.使用循环九九乘法表
# sum = 0;
# for i in range(1,10):
#     for j in range(1,i+1):
#         sum = i * j
#         print(str(i) + '*' + str(j) + '=' + str(sum) + '   ',end="")
#     print()

# 7.判断一个是是否是质数(质数就是除了1和本身，没有其他的公约数)
# a = int(input('输入一个数:'))
# for i in range(2,a):
#     if a%i == 0:
#         print(str(a) + '不是质数')
#         break
# else:
#     print(str(a) + '是质数')

# 8.求2-100000的质数的个数
# sum = 0
# for i in range(2,1001):
#     for j in range(2,i):
#         if i%j == 0:
#             break
#     else:
#         sum += 1
# print(sum)


# sum = 0
# i = int(input('输入一个数：'))
# if i == 2:
#     sum = 1
# else:
#     for i in range(2,1001):
#         for j in range(2,i):
#             if i%j == 0:
#                 break
#         else:
#             sum += 1
#     print(sum)


#####################################################################
#####################################################################
#####################################################################
#####################################################################
#####################################################################
# 列表(List):[] 可以存储多个值，通过下标访问，下标从0开始，可以为负数，表示从后面往前
# 集合(set):{}  是一个无序不重复元素的序列。创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
# 元组:[] 与列表类似，不同之处在于元组的元素不能修改。元组使用小括号，列表使用方括号。【】


# a = 'abcdefghi'
# print(a[1:-2])
# print(a[0:-3])

# 数组
# name = 'abcdefg'
# print(name[0] + name[4])
# print(name[0:4])  # 取出一部分,不包括最后一个
# print(name[3:4])
# print(name[2:])  #从开始位置截取
# print(name[1:-1])  #下标1开始到最后倒数第二个之间的
# print(name[:3])  #取前三个
# print(name[:2])  #取前两个
# print(name[::2])  #每次加两个字符
# print(name[::-2])  #倒序输出每次增加两个字符
# print('------')
# print(name[5:1:2])  #
# print(name[5:1:-2])  #倒序每次输出两个
# print(name[1:5:2])
#
# print('--------------------')
# print('--------------------')
# #字符串操作
# a = 'abcdefghijklmnabcd'
# #find  查找位置
# print(a.find('f',0,10))
# #index
# print(a.index('f',0,9))
# #count  计算出现的次数
# print(a.count('c',0,len(a)))
# #replace  替换
# print(a.replace('g','G',2))
# #split  分割
# print(a.split('c',2))
# #capitalize  第一个字符串大写
# print(a.capitalize())
# #title  把字符串每个单词首字母大写
# abc = 'Nihao Wojiao Zhangsan'
# print(abc.title())
# #stsrtswith  检查字符串是否是以obj 开头
# print(abc.startswith('n'))
# #endswith  检查字符串是否以obj结尾
# print(abc.endswith('n'))
# #lower  将字符串所有大写字符转为小写
# print(abc.lower())
# #upper  将字符串所有小写字符转为大写
# print(abc.upper())
# #ljust  返回一个字符串左对齐
# print(abc.ljust(40))
# #rjust  字符串右对齐
# print(abc.rjust(40))
# #center  字符串居中并填充
# print(abc.center(40))
# #lstrip  删除字符串左边的空白字符
# print(abc.lstrip())
# #strip   删除字符串右边的空白字符
# print(abc.strip())
# #rfind  从右边开始查找
# print(a.rfind('f',0,20))
# #rindex  类似于index()，从右边开始查找
# print(a.rindex('f',0,20))
# #partition  分割字符串
# print(a.partition('f'))
# #rpartition  从右边开始分割
# print(a.rpartition('f'))
# #splitlines  按照行分割
# a='''asdfghjkl
# fs
# fsa
# dkyat
# ajr
# k
# '''
# print(a.splitlines())
# #isalpha  如果字符串中都是字母，则返回true，否则返回false
# print(a.isalpha())
# #isalnum  如果所有字符串都是字母或者数字则返回true，否则返回false
# print(a.isalnum)
# #isspace  如果字符串包含空格，则返回true，否则返回false
# print(a.isspace())
# #join  将序列中的元素按照指定字符连接生成一个新的字符串
# str = ['1','2','3']
# b = '-'
# print(b.join(str))


###########################################################################

# 列表:可以存储多个值，通过下标访问，下标从0开始，可以为负数，表示从后面往前
# nameList = ['张三','李四','王五']
# print(nameList)
# print(nameList[0])

# 列表的循环遍历
# #1.使用for循环
# nameList = ['张三','李四','王五']
# for name in nameList:
#     print(name)
#
# #2.使用while循环
# length = len(nameList)
# i = 0
# while i < length:
#     print(nameList[i])
#     i += 1


###添加元素:append  extend  insert
# append:
# nameList = ['张三','李四','王五']
# print("-----添加之前，列表nameList的数据-----")
# for tempName in nameList:
#     print(tempName)
# temp = input('请输入要添加的元素:')
# nameList.append(temp)
# print("-----添加之后，列表nameList的数据-----")
# for tempName in nameList:
#     print(tempName)


# extend:extend可以将一个集合中的元素逐一添加到列表中
# a = ['1','3','5','7']
# b = ['2','4','6','8']
# a.append(b)
# print(a)

# c = ['1','3','5','7']
# d= ['2','4','6','8']
# c.extend(d)
# print(c)

# #insert  insert(index,object):再指定位置index前插入元素object
# e = ['1','3','5','7']
# f = ['2','4','6','8']
# e.insert(1,3)
# print(e)


####修改元素
# nameList = ['张三','李四','王五']
# for tempName in nameList:
#     print(tempName)
# #修改元素
# nameList[0] = 'zhangsan'
# for tempName in nameList:
#     print(tempName)


###查找元素  in / not in / index / count
# nameList = ['张三','李四','王五']
# print(nameList)
# findName = input('请输入要查找的名字:')
# if findName in nameList:
#     print('找到名字。')
# else:
#     print('没有找到。')

# list1 = ['1','2','3','4','5']
# list1.index('3',1,5)


###删除元素  del / pop / remove
# del:根据下标进行删除
# pop:删除最后一个元素
# remove:根据元素的值删除

# nameList = ['张三','李四','王五','赵六','陈七']
# for tempName in nameList:
#     print(tempName,end='')
# print()
# del
# del nameList[3]
# for tempName in nameList:
#     print(tempName,end='')

# ##pop
# nameList.pop()
# for tempName in nameList:
#     print(tempName,end='')


# ##remove
# nameList.remove('赵六')
# for tempName in nameList:
#     print(tempName,end='')


######排序  sort / reverse
##sotr重新排列list，默认从小到大  reverse = true课改为倒序，即有大到小

# a = [1,2,3,4,5]
# a.sort()  #正序
# a.reverse()  #倒序
# print(a)


#########列表的嵌套
# a = [['1','2'],'3','4',['5',['6','7']]]
# print(a)


################
# 集合  set{}  创建一个空集合：set()  创建一个空字典：set{}
# name = {'张三','李四','张三','王五','赵六','陈七'}
# print(name)

# set可以进行集合运算
# a = set('abcdefghijklmn')
# b = set('abcdopqrstuvwmn')
# print(a - b)  #差集,第一个减去两个相交的
# print(a | b)  #并集，两个集合所有的
# print(a & b)  #交集，两个集合相交
# print(a ^ b)  #两个集合不同时存在的元素


##############################################
# 元组  元组的元素不能修改
# tuple = ('hello','1','张三',20)
# print(tuple)
# print(tuple[3])
# 修改元组  元组中的元素值不允许修改，但是可以进行连接组合
# tup1 = (10,11,12)
# tup2 = ('abc','xyz')
# print(tup1)
# print(tup2)
# tup3 = tup1 + tup2
# print(tup3)
##删除元组  元组中的元素值不允许修改  可以使用del语句删除整个元组
# tup1 = ('faef','fasfa',123124,5232)
# del tup1
# print(tup1)


##############################################
##############################################
##############################################

# 字典
# info = {'name' : '张三','age' : 20,'sex' : '男','address' : '青岛'}
# print(info)
# print(info['name'])
#
# #get()  可以获取值
# age = info.get('age',19)
# print(age)


# info = {'name' : '张三','age' : 20,'sex' : '男','address' : '青岛'}
###修改元素
# newage = int(input('请输入年龄:'))
# info['age'] = newage
# print(info)

###添加元素
# 如果在使用 变量名['键'] = 数据 时，这个“键”在字典中，不存在，那么就会新增这个元素
# newscore = int(input('请输入一个成绩:'))
# info['score'] = newscore
# print(info)
# print('添加之后的成绩为:%d'%info['score'])


###删除元素
#  del || clear()
# del:删除指定元素
# info = {'name' : '张三','age' : 20,'sex' : '男','address' : '青岛','score' : 99}
# print('删除前：%d'%info['score'])
# del info['score']
# print('删除后:%d'%info['score'])

# del 删除整个字典
# del info
# print(info)

# clear清空整个字典
# info.clear()
# print(info)

#
# info = {'name' : '张三','age' : 20,'sex' : '男','address' : '青岛','score' : 99}
# #字典操作：
# #len()  返回字典中键值对的个数
# print(info.len())


# str = 'abcdabcabcabcc'
# print(str.split('a'))
# print(str.split('a',))
# print(str.split('a',1))
# print(str.split('a',2))
# print(str.split('b',3))
# print(str.split('b'))


# 1.一个学校，有3个办公室，现在有8位老师等待工位的分配，请编写程序，
# 完成随机的分配
# #列表
# import random
# bgs = [[],[],[]]
# teacher = ['T01','T02','T03','T04','T05','T06','T07','T08',]
# for t in teacher:
#     # 随机分配办公室
#     id = random.randint(0,2)
#     bgs[id].append(t)
# print(bgs)
# i = 1
# for n in bgs:
#     print('办公室' + str(i) + '中有' + str(len(n)) + '位老师。')
#     i += 1
#     print('老师如下：',end='')
#     for t1 in n:
#         print(t1,end='  ')
#     print()


# 2.编写程序，完成“名片管理器”项目
# 需要完成的基本功能：
# 添加名片
# 删除名片
# 修改名片
# 查询名片
# 退出系统
# 程序运行后，除非选择退出系统，否则重复执行功能
#
# userList = []
# i = 0  #i为用户标识符，标记是哪个用户
# while True:
#     print('名片管理器')
#     #选择选项进行功能调用
#     print('======可进行的操作如下所示：')
#     print('1------添加名片')
#     print('2------删除名片')
#     print('3------修改名片')
#     print('4------查询名片')
#     print('5------退出系统')
#     tab = int(input('======请输入要进行的操作'))
#     #添加名片
#     if tab == 1:
#         print('======现在进行添加名片操作。')
#         newname = input('请输入姓名：')
#         newsex = input('请输入性别：')
#         newage = (input('请输入年龄：'))
#         newaddress = input('请输入地址：')
#     #每次增加名片，下标增加1
#     i += 1
#     userInfo = {}
#     userInfo['id'] = i
#     userInfo['name'] = newname
#     userInfo['sex'] = newsex
#     userInfo['age'] = newage
#     userInfo['address'] = newaddress
#     userList.append(userInfo)
#     print('用户添加成功！')
# #删除名片,删除下标对应的元素的所有数据，但是下标还存在
# if tab == 2:
#     d = int(input('======请输入要删除的名片的下标:'))
#     if len(userList) > 0:
#         if len(userList[d]) > 0:
#             userList[d].clear()
#         else:
#             print('该用户名片不存在，请重试')
#     else:
#         print('名片列表不存在。')
# #修改名片
# if tab == 3:
#     btn = int(input('请输入要修改的元素的下标：'))  # 要修改的元素的下标 userList[btn]
#     #修改之前先判断名片字典是否存在
#     if userList[btn]:
#         choice = int(input('======可进行的修改操作如下:\n1-修改部分数据\t2-修改全部数据\n请输入要进行的修改操作：'))
#         if choice == 1:
#             print('======部分修改。可进行的修改操作如下:\n\t1------修改姓名\n\t2------修改性别\n\t3------修改年龄\n\t4------修改地址')
#             update = int(input('请输入要进行修改的内容标号:'))
#             if update == 1:
#                 updateName = input('请输入修改后的姓名：')
#                 userInfo['name'] = updateName
#                 print('修改姓名成功。')
#             elif update == 2:
#                 updateSex = input('请输入修改后的性别：')
#                 userInfo['sex'] = updateSex
#                 print('修改性别成功。')
#             elif update == 3:
#                 updateAge = input('请输入修改后的年龄：')
#                 userInfo['age'] = updateAge
#                 print('修改年龄成功。')
#             elif update == 4:
#                 updateAddress = input('请输入修改后的地址：')
#                 userInfo['address'] = updateAddress
#                 print('修改地址成功。')
#         #修改多条数据，包括所有数据
#         if choice == 2:
#             print('======修改全部数据。')
#             updateName = input('请输入修改后的姓名：')
#             userInfo['name'] = updateName
#             updateSex = input('请输入修改后的性别：')
#             userInfo['sex'] = updateSex
#             updateAge = input('请输入修改后的年龄：')
#             userInfo['age'] = updateAge
#             updateAddress = input('请输入修改后的地址：')
#             userInfo['address'] = updateAddress
#             print('用户所有信息修改成功！')
#     else:
#         print('用户字典不存在，请重试。')
#
# #查询名片
# if tab == 4:
#     # for k,v in enumerate(userList):
#     #     print(k,v)
#     userBtn = int(input('请输入要查询名片的用户的下标：'))
#     if userList:
#         if userList[userBtn]:
#             print(userList[userBtn])
#         else:
#             print('用户字典不存在。')
#     else:
#         print('名片列表不存在,请先创建。')
#     #print(userList)
# if tab == 5:
#     print('退出系统。')
#     break


#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
'''练习4  学生管理系统
  编写程序，设计“学生管理系统”项目
  需要完成的基本功能：
  添加学生(包括学号，姓名，年龄，性别)
  删除学生
  修改修改
  查询查询
  退出系统
  程序运行后，除非选择退出系统，否则重复执行功能
'''
'''
userList = []
#i为用户标识符，标记是哪个用户
id = 0
while True:
    print('==========学生管理系统==========')
    #选择选项进行功能调用
    print('======可进行的操作如下所示：')
    print('1------添加学生')
    print('2------删除学生')
    print('3------修改学生信息')
    print('4------查询学生信息')
    print('5------退出系统\n')
    tab = int(input('======请输入要进行的操作:'))
    #1---添加名片
    if tab == 1:
        print('======现在进行添加学生操作。')
        newsno = input('请输入学号：')
        newname = input('请输入姓名：')
        newsex = input('请输入性别：')
        newage = input('请输入年龄：')

        # 添加学生之前需要进行判断，判断要添加的学生是否已经存在了，判定条件是按照学号去判定
        for i in userList:
            if i['sno'] == newsno:
                print('存在学号为%s的学生，不能重复添加。'%newsno)
                break
        else:
            #每次增加名片，学生的id增加1
            id += 1
            userInfo = {}
            userInfo['id'] = id
            userInfo['sno'] = newsno
            userInfo['name'] = newname
            userInfo['sex'] = newsex
            userInfo['age'] = newage
            userList.append(userInfo)
            print('学生添加成功！\n')

    #2---删除学生,根据学号清空对应的学生字典的数据，但是字典还是存在的
    if tab == 2:
        print('现在进行删除学生的操作.')
        dno = input('删除学生。请输入要删除的学生的学号:')
        if len(userList) > 0:
            for i in userList:
                if i['sno'] == dno:
                    # 查找到要删除的学生对应的列表的下标
                    for k,v in enumerate(userList):
                        # 当下标对应的字典与要删除的学生字典匹配成功，则删除该字典
                        if i == v:
                            del userList[k]
                            print('删除成功，删除了学号为%s的学生\n'%dno)
                            break
        else:
            print('学生字典不存在，请重试。\n')

    #3---修改学生
    if tab == 3:
        print('现在进行修改学生的操作.')
        btn = input('请输入要修改信息的学生的学号：')  #根据学号修改学生字典信息，查出userList对应的k,v,然后根据k修改
        #修改之前先判断名片字典是否存在
        if len(userList) > 0:
            # 遍历列表，查找学号对应的字典
            for i in userList:
                if i['sno'] == btn:
                    # 查找到学生字典,可以进行修改操作
                    print('++++++++找到了该学号对应的学生字典如下：++++++++')
                    print(i)
                    for k,v in enumerate(userList):
                        # 当进行修改操作的学生学号查找到了对应的字典，则可以进行修改操作
                        if v['sno'] == i['sno']:
                            choice = int(input('======可进行的修改操作如下:\n1-修改部分信息\t2-修改全部信息\n请输入要进行的修改操作：'))
                            if choice == 1:
                                print('======部分修改。可进行的修改操作如下:\n\t1------修改学号\n\t2------修改姓名\n\t3------修改性别\n\t4------修改年龄')
                                update = int(input('请输入要进行修改的内容标号:'))
                                if update == 1:
                                    updateSno = input('请输入修改后的学号：')
                                    userList[k]['sno'] = updateSno
                                    # userInfo['sno'] = updateSno
                                    print('修改学号成功。\n')
                                elif update == 2:
                                    updateName = input('请输入修改后的姓名：')
                                    userList[k]['name'] = updateName
                                    print('修改姓名成功。\n')
                                elif update == 3:
                                    updateSex = input('请输入修改后的性别：')
                                    userList[k]['sex'] = updateSex
                                    print('修改性别成功。\n')
                                elif update == 4:
                                    updateAge = input('请输入修改后的年龄：')
                                    userList[k]['age'] = updateAge
                                    print('修改年龄成功。\n')
                            #修改多条数据，包括所有数据
                            if choice == 2:
                                print('======修改全部数据。')
                                updateSno = input('请输入修改后的学号：')
                                userList[k]['sno'] = updateSno
                                updateName = input('请输入修改后的姓名：')
                                userList[k]['name'] = updateName
                                updateSex = input('请输入修改后的性别：')
                                userList[k]['sex'] = updateSex
                                updateAge = input('请输入修改后的年龄：')
                                userList[k]['age'] = updateAge
                                print('学生所有信息修改成功！\n')
        else:
            print('学生字典不存在，请重试。')

    #4---查询名片
    if tab == 4:
        check = int(input('1-----查看指定学号学生信息\n2-----查看所有学生信息\n'))
        if check == 1:
            userBtn = input('请输入要查询信息的学生的学号：')
            if len(userList) > 0:
                print('学生列表存在数据。')
                for i in userList:
                    # 遍历列表查找与学号对应的学生的字典
                    if i['sno'] == userBtn:
                        print('找到该学生的字典。')
                        print(i)
                        break
                # 当要查找的学生学号不存在于学生列表的时候提示不存在。
                else:
                    print('学生字典不存在。\n')
            else:
                print('学生列表不存在,请先创建。')
        elif check == 2:
            if userList:
                print(userList)
            else:
                print('学生列表不存在。\n')
        else:
            print('请输入正确的指令。\n')

    # 5---退出系统
    if tab == 5:
        print('退出系统。')
        break

'''


#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################

###面向对象

##类和对象
# 定义类：
# class A:
#     def f(self):
#         print('hello')
#
# # 创建对象：  对象名=类名()
# myObj = A()
# # # 调用方法：
# myObj.f()
# # # 添加属性:
# myObj.j = 12

# 定义一个猫狗类
# class Dog:
#     def func1(self):
#         print('我是Dog.')
#
# class Cat:
#     def func2(self):
#         print('我是Cat.')
#
# def objFunc():
#     dogObj = Dog()
#     catObj = Cat()
#     dogObj.func1()
#     catObj.func2()
#
# objFunc()

# 定义一个人类
# class People:
#     def __init__(self, name, age, sex):
#         self.name = name
#         # 设置私有属性
#         self.__age = age
#         self.sex = sex
#         print(self.name, self.__age, self.sex)
#         print('__init__构造方法被调用.')
#
#     # set方法给私有属性变量赋值
#     def setAge(self, age):
#         if age > 0 and age < 100:
#             self.__age = str(age)
#         else:
#             print('输入的年龄不符合规范。')
#
#     # get方法获取到set中赋值的年龄
#     def getAge(self):
#         return self.__age
#
#     def eat(self):
#         print(self.name + '今年' + self.getAge() + '岁了。')
#
# # 创建对象
# p = People('张三','0','男')
# p.setAge(19)
# p.eat()





#########################################################################################
#########################################################################################
'''1.该程序中有类：Lader、Circle具体要求如下：
   Lader类具有上底、下底、高、面积属性，具有返回面积的功能，构造方法对上底、下底、高进行初始化。
   Circle类具半径、周长和面积属性，具有返回周长、面积的功能，构造方法对半径进行初始化'''
# class Lader:
#     def __init__(self,sd,xd,h,s1):
#         self.sd = str(sd)
#         self.xd = str(xd)
#         self.h = str(h)
#         self.s1 = str(s1)
#         print(self.sd,self.xd,self.h,self.s1)
#         print('__init__构造函数成功调用。')
#     def jisuan(self):
#         print('Lader上底为:' + self.sd + ',下底为：' + self.xd + ',高为:' + self.h + ',面积为：' + self.s1)
#
# # 创建一个函数，执行函数的时候键盘输入上底、下底、高，然后创建对象去计算面积
# def countSquare():
#     sd = int(input('请输入上底:'))
#     xd = int(input('请输入下底:'))
#     h = int(input('请输入高:'))
#     s1 = ((sd + xd) * h) / 2
#     # 创建对象
#     l = Lader(sd,xd,h,s1)
#     l.jisuan()
# # 调用函数
# countSquare()
#
# class Circle:
#     def __init__(self,r,c,s2):
#         self.r = str(r)
#         self.c = str(c)
#         self.s2 = str(s2)
#         print(self.r,self.c,self.s2)
#         print('__init__构造函数成功调用。')
#     def countSquaer2(self):
#         print('半径为:' + self.r + ',周长为:' + self.c + '面积为:' + self.s2)
#
# def circleFunc():
#     r = int(input('请输入一个半径:'))
#     c = 2 * 3.14 * r
#     s = 3.14 * r**2
#     s2 = Circle(r,c,s)
# circleFunc()

'''
 2.按要求编写程序。
（1）建立一个名叫Cat的类：
 属性：姓名、毛色、年龄
 行为：显示姓名、喊叫
 （2）创建一个对象猫，姓名为“妮妮”，毛色为“灰色”，年龄为2岁，在屏幕上输
 出该对象的毛色和年龄，让该对象调用显示姓名和喊叫两个方法。'''

# class Cat:
#     def __init__(self,name,color,age):
#         self.name = name
#         self.color = color
#         self.age = str(age)
#         print('小猫叫' + self.name + ',毛色是' + self.color + ',年龄为' + self.age + '岁。')
#     def viewName(self):
#         print('小猫的姓名为：' + self.name)
#     def speak(self):
#         print('喵喵！你好，我叫' + self.name + '，很高兴认识你')
#
# c = Cat('妮妮','灰色',2)
# c.viewName()
# c.speak()

'''
3．按要求编程序。
（1）创建一个叫做People的类：
 属性：姓名、年龄、性别、身高
 行为：说话、计算加法、改名
 编写能为所有属性赋值的构造方法；
（2）创建一个对象：名叫“张三”，性别“男”，年龄18岁，身高1.80；
 让该对象调用成员方法：
 说出“你好！”
 计算23+45的值
 将名字改为“李四”'''

# class People:
#     def __init__(self,name,age,sex,tall,a,b):
#         self.name = name
#         self.age = str(age)
#         self.sex = sex
#         self.tall = str(tall)
#         self.a = a
#         self.b = b
#     def say(self):
#         print('你好！我叫' + self.name + '，性别' + self.sex + '，我今年' + self.age + '岁了，身高为' + self.tall + 'cm。')
#     def count(self):
#         print('a+b=' + str(self.a + self.b))
#
# p = People('张三',18,'男',178,23,45)
# p.say()
# p.count()
# p.name = '李四'
# p.say()
'''
4．编写应用程序。首先，定义描述学生的类——Student，包括学号、
姓名、年龄等属性；outPut()用于输出学生信息。
创建多个Student类的对象，使用这些对象来测试Student类的功能。'''

# class Student:
#     def __init__(self,sno,name,age,sex):
#         self.sno = sno
#         self.name = name
#         self.age = age
#         self.sex = sex
#         print(self.sno,self.name,self.age,self.sex)
#     def outPut(self):
#         print('你好，我叫' + self.name + '，我的学号是' + str(self.sno) + '，我' + str(self.age) + '岁了，性别是' + self.sex)
#
# a = Student(1,'张三',18,'男')
# a.outPut()
# b = Student(2,'李四',19,'男')
# b.outPut()
# c = Student(3,'王五',21,'男')
# c.outPut()


'''
5.创建一个Point类，有属性x，y，方法getX(),setX()，还有一个构造方
法初始化x和y。创建对象测试它。'''
# (x,y) 坐标值
# class Point:
#     def __init__(self):
#         self.__x = ''
#         self.__y = ''
#     def getX(self):
#         return self.__x
#     def setX(self,x):
#         if x > 0:
#              self.__x = x
#         else:
#             print('输入的数值不符合规范。')
#     def getY(self):
#         return self.__y
#     def setY(self,y):
#         if y > 0:
#             self.__y = y
#         else:
#             print('输入的数值不符合规范。')
#     def printXy(self):
#         print('X为:' + str(self.getX()) + ',Y为:' + str(self.getY()))
#
# p = Point()
# p.setX(-1)
# p.setY(9)
# p.printXy()





#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################

### 继承  描述的是事物之间的所属关系
#字类继承时，小括号中为父类的名字，父类的属性、方法会继承给字类
# class Animal:
#     def eat(self):
#         print('吃饭。')
#     def drink(self):
#         print('喝水。')
#     def run(self):
#         print('跑。')
#     def sleep(self):
#         print('睡觉。')
#
# # 定义一个Dog字类，调用父类Animal的方法
# class Dog(Animal):
#     def goujiao(self):
#         print('--叫--')
# # 定义一个Cat字类，调用父类Animal的方法
# class Cat(Animal):
#     def zhualaoshu(self):
#         print('--抓老鼠--')
# # 创建一个Dog对象
# wangcai = Dog()
# wangcai.eat()
# wangcai.goujiao()
# # 创建一个Cat对象
# mimi = Cat()
# mimi.eat()
#
# a = Animal()
# a.eat()



# 多继承，即字类有多个父类
# 定义一个父类1
# 当多个父类有同名的方法时，字类调用的时候按照创建对象是的先后顺序来
# class Parent1:
#     def printParent1(self):
#         print('--这是Parent1--')
# # 定义一个父类2
# class Parent2:
#     def printParent2(self):
#         print('--这是Parent2--')
# # 定义一个字类继承父类1和2
# class Child(Parent1,Parent2):
#     def printChild(self):
#         print('--Child--')
# # 创建一个字类对象
# obj = Child()
# obj.printParent1()
# obj.printParent2()


#############################################################
# 方法重写  子类中有一个方法和父类中的方法重名，那么子类中的方法会覆盖掉父类中的同名方法
# 定义一个Cat父类
# class Cat(object):
#     def sayHello(self):
#         print('这是父类中的方法。')
# # 定义一个Bosi字类
# class Bosi(Cat):
#     def sayHello(self):
#         print('这是字类中的方法。')
# bosi = Bosi()
# bosi.sayHello()


# 调用父类的方法：
# 父类类名.父类方法(self)
# super(字类类名,self).方法名()
# super().父类的方法名()
# class Cat(object):
#     def __init__(self,name):
#         print(name)
# class Bosi(Cat):
#     def __init__(self,name):
#         #调用父类在的__init__方法1
#         Cat.__init__(self,name)
#         #调用父类的__init__方法2
#         super(Bosi,self).__init__(name)
#         #调用父类的__init__方法3
#         super().__init__(name)
#         super().__init__(name)
# bosi = Bosi(Cat)
# bosi.__init__('咪咪')

##########1:
# 父类Animal
# class Animal(object):
#     def eat(self):
#         print('---吃---')
#     def drink(self):
#         print('---喝---')
#     def run(self):
#         print('---跑---')
#     def bark(self):
#         print('---汪汪汪---')
# # Dog字类
# class Dog(Animal):
#     #字类继承父类所有的方法和属性
#     def bark(self):
#         print('汪汪叫。')
# # 具体字类，继承Dog
# class Wangcai(Dog):
#     def swim(self):
#         print('我会游泳。')
#     def bark(self):
#         print('汪汪汪')
# d = Wangcai()
# d.bark()
# d.eat()
# d2 = Dog()
# d2.bark()

########2:字类扩展
# class Animal(object):
#     def eat(self):
#         print('---吃---')
#     def drink(self):
#         print('---喝---')
#     def run(self):
#         print('---跑---')
#     def bark(self):
#         print('---汪汪汪---')
# # Dog字类
# class Dog(Animal):
#     #字类继承父类所有的方法和属性
#     def bark(self):
#         print('汪汪叫。')
# # 具体字类，继承Dog
# class Wangcai(Dog):
#     def swim(self):
#         print('我会游泳。')
#     def bark(self):
#         print('汪汪汪')
# d = Wangcai()
# d.bark()
# d.eat()
# d2 = Dog()
# d2.bark()



#############################################################
#多态 ：定义时的类型和运行时的类型不一样，称为多态
#python--鸭子类型
# class F1(object):
#     def show(self):
#         print('F1 show!')
# class S1(F1):
#     def show(self):
#         print('S1 show!')
# class S2(F1):
#     def show(self):
#         print('S2 show!')
# # s1 = S1()
# # s1.show()
# # s2 = S2()
# # s2.show()
# # s = F1()
# # s.show()
# # 多态  定义时的类型和执行时的类型是不同的
# def func(obj):
#     obj.show()
# s = S1()
# func(s)


##################################################
# 类属性、实例属性
# 类属性就是类的属性，实例属性就是在实例中定义的属性
# 类属性需要通过类需调用，实例属性需要通过实例对象去调用
# 类属性
# class People(object):
#     name = '张三'  #类属性
#     def __init__(self):
#         self.name = '李四'  #实例属性
#         self.age = 20      #实例属性
#
# p = People()  #创建实例对象
# print(p.name)  #这里输出的是实例属性
# #通过实例对象修改实例属性，会创建一个同名的实例属性,相当于把实例属性给覆盖了，这种方式修改的是实例属性，类属性不会被修改
# p.name = '张三1'
# print(p.name)  #这里输出的是实例属性
#
# # del方法删除实例属性
# del p.name      #删除重复的实例属性后，原先存在的实例属性相当于被清空了，不存在了
# print(p.name)   #实例属性不存在了，所以只能找到类属性
# # 再通过实例对象去修改实例属性
# p.name = '汤姆'
# print('1111' + p.name)
# p.name = '杰瑞'
# print('2222' + p.name)
# del p.name
# print('---' + p.name)
# # 通过类对象修改类属性
# People.name = '王五'
# print(People.name)
# print(p.name)


#####################################################
# 类方法和静态方法
# 类方法时类对象拥有的，修饰器：@classmethod来标时其为类方法,第一个参数必须是类对象
# class People(object):
#     country = 'China'  #类属性
#     # 类方法,创建了类方法，属性就是类属性了
#     @classmethod
#     def getCountry(cls):
#         return cls.country
# p = People()
# print('这是通过实例对象调用：' + p.getCountry())  #通过实例对象调用
# print('这是通过类对象调用' + People.getCountry())   #通过类对象调用
# p.country = '中国'  #通过实例对象修改实例属性，此时相当于创建了一个实例属性
# print(p.country)
# print(People.country)  #创建了一个实例属性，但是类属性没有被修改
#
# # 删除实例属性
# del p.country
# print(p.country)

# 类属性和实例属性
# 类属性在类中定义，实例属性在方法中定义
# 类属性：
# class Parent:
#     name = '张三'  #类属性
#     def __init__(self):
#         self.age = 12  #实例属性
#         self.sex = '男'  #实例属性
# # 创建一个实例对象
# p = Parent()
# print('这是类属性：' + Parent.name)
# print('这是实例属性：' + str(p.age),p.sex)
# # 通过实例对象修改实例属性，此时会创建一个和实例对象同名的属性
# p.name = '李四'
# p.age = 20
# print('实例修改的属性：' + p.name,str(p.age),p.sex)
# print('--------' + Parent.name)
# # del方法删除实例对象修改的实例属性
# del p.name
# print(p.name,str(p.age),p.sex)
# print(Parent.name)


########################################
# 类方法和静态方法
# 类方法：是类对象拥有的方法 修饰器@classmethod,可以通过类对象和实例对象访问
# class Parent:
#     name = '张三'
#     @classmethod
#     def getname(cls):
#         return cls.name
# p = Parent()
# print(p.getname())
# print(Parent.getname())

# 静态方法  修饰器@staticmethod  不需要定义参数
# class Parent:
#     name = '张三'
#     @staticmethod
#     def getname():
#         return Parent.name
# p = Parent()
# print(p.getname())
# print(Parent.getname())
#
# 使用类方法计算矩形面积
# class Parent:
#     l = 3
#     w = 10
#     @classmethod
#     def mianji(cls):
#         return cls.l * cls.w
# p = Parent()
# print(p.mianji())


#静态方法  修饰器：@staticmethod,静态方法不需要定义参数
# class People(object):
#     country = 'China'  #类属性
#     @staticmethod
#     def getCountry():
#         return People.country
# p = People()  #创建一个实例对象
# print('这是实例属性：' + p.country)
# p.country = '中国'   #通过实例对象修改实例属性，此时创建了一个实例属性
# print(p.country)
# print(p.getCountry())
# People.country = '中华人民共和国'  #通过类对象修改类属性
# print(p.getCountry())
# print(People.getCountry())


#__new__方法
# class Dog(object):
#     def __init__(self):
#         print('构造函数执行成功。')
#     def __new__(cls):
#         print('--new--方法')
#         # 可以return父类__new__出来的实例  即object.__new__()
#         return object.__new__(cls)
# a = Dog()
# print(a.__new__())


#############################
#单例模式  确保一个类只有一个实例，自行实例化
# class Dog(object):
#     __instance = None
#     def __new__(cls):  #cls为要实例化的类
#         if cls.__instance == None:
#             # 如果当前类的实例不存在，或者为空，那么就把父类对象的实例赋值给他
#             # Dog就是单例类
#             cls.__instance = object.__new__(cls)
#             return cls.__instance
#         else:
#             return cls.__instance
# a = Dog()
# print(id(a))
# b = Dog()
# print(id(b))

# 监管报送
# east校验  查找出脏数据(异常的数据)，进行数据清洗
#贷款业务五级分类：正常、关注、次级、可疑、损失
# ename = null
# select ename from emp
#   where ename is null
#   or length(replace(trim(ename),' ','')) = 0
#   or ename = 'null'


'''1．编写一个类A，该类创建的对象可以调用方法f输出小写的英文字母表。然
后再编写一个A类的子类B，子类B创建的对象不仅可以调用方法f输出小写的英文字母表，
而且可以调用子类新增的方法g输出大写的英文字母表。测试类A与类B。'''
#ord('a') => 97  chr(97) => a
# print(chr(91))
# print(ord('A'))
# print(ord('Z'))

# class A():
#     def f(self):
#         for i in range(ord('a'),ord('{')):
#             self.i = chr(i)
#             print(self.i,end=' ')
# class B(A):
#     def f(self):
#         for i in range(ord('a'),ord('{')):
#             self.i = chr(i)
#             print(self.i,end=' ')
#     def g(self):
#         for i in range(ord('A'),ord('[')):
#             self.i = chr(i)
#             print(self.i,end=' ')
# # 创建一个实例对象b
# b = B()
# b.f()

# b.g()

'''2．按要求编写一个应用程序：
（1）定义一个类，描述一个矩形，包含有长、宽两种属性，和计算面积方法。
（2）编写一个类，继承自矩形类，同时该类描述长方体，具有长、宽、高属性，
和计算体积的方法。
（3）创建一个长方体，定义其长、宽、高，输出其面积和体积。'''

# 重写方法：
# class Juxing:
#     def __init__(self,l,w):
#         self.l = l
#         self.w = w
#     def s(self):
#         self.s = self.l * self.w
#         print('面积为%d'%self.s)
# 字类
# class Child(Juxing):
#     def __init__(self,l,w,h):
#         self.h = h
#         # 重写父类方法
#         super().__init__(l,w)
#         print('子类重写方法',self.l,self.w,self.h)
#     def v(self):
#         self.v = self.l * self.w * self.h
#         print('体积为：%d'%self.v)
# c = Child(1,2,3)
# c.s()
# c.v()


# class juxing:
#     def mianji(self,chang = 0,kuan = 0):
#         self.mianji = chang * kuan
#         print(self.chang,self.kuan)
#         print('面积为：%d'%self.mianji)
# # 字类：
# class child(juxing):
#     def mianji(self,chang,kuan,gao = 0):
#         self.mianji1 = chang * kuan
#         self.mianji2 = chang * gao
#         self.mianji3 = kuan * gao
#         print('面积为：%d' %(self.mianji1*2 + self.mianji2*2 + self.mianji3*2))
#     def tiji(self,chang,kuan,gao):
#         self.tiji = chang * kuan * gao
#         print(chang,kuan)
#         print('长方体体积为：%d'%self.tiji)
# c = child()
# c.mianji(10,20,10)
# c.tiji(10,10,10)

'''3.要求编写一个应用程序：
定义类Circle(圆)，属性有半径，构造方法可以为属性初始化，返回圆的面积
定义类Cylinder(圆柱),属性有半径，高;返回圆柱的体积'''

# class Circle:
#     def __init__(self,r):
#         self.r = r
#     def mianji(self):
#         self.mianji = self.r**2 * 3.14
#         return self.mianji
# class Cylinder:
#     def __init__(self,r,h):
#         self.r = r
#         self.h = h
#     def tiji(self):
#         self.v = self.r**2 * 3.14 * self.h
#         return self.v
# # 创建一个实例对象s
# c = Circle(3)
# print(c.mianji())
# l = Cylinder(2,4)
# print(l.tiji())

'''4.从键盘上接收2个数，完成2个数相除功能；考虑发生的异常并处理(处理方式给出提示即可)'''

# class Number:
#     def __init__(self):
#         self.__a = 0
#         self.__b = 0
#     def setA(self,a):
#         self.a = a
#     def getA(self):
#         return self.a
#     def setB(self,b):
#         # if b == 0:
#         #     print('除数不能为0')
#         # else:
#         #     self.b = b
#         self.b = b
#     def getB(self):
#          return self.b
#     def chufa(self):
#         self.result = self.getA() / self.getB()
#         print('%f / %f = %f'%(self.getA(),self.getB(),self.result))
# def jisuan():
#     a = float(input('请输入第一个数：'))
#     b = float(input('请输入第二个数：'))
#     # n = Number()
#     # n.setA(a)
#     # n.setB(b)
#     if b == 0:
#         print('除数不能为0')
#     else:
#         n = Number()
#         n.setA(a)
#         n.setB(b)
#         n.chufa()
#
# jisuan()


'''
列表：[]，通过下标访问元素，下标从0开始
集合：{}，无序不重复的序列，创建一个空集合：set()
元组：[]，与列表类似，但是其中的元素不能修改，只能删除整个元素
字典：{},key,value 键值存储数据，通过下标访问
'''
# name = 'abcdefghijklmn'
# print(name[1:7:2])
# print(name[7:1:-2])
# print(name[::-2])
# 列表的训话
# nameList = ['张三','李四','王五']
# for i in nameList:
#     print(i)
# append  添加元素
# info['name'] = '张三'
# userList.append(info)
# a = [1,2]
# b = [3,4]
# a.append(b)
# a.append(b)
# print(a)
# 删除对象：
# del：根据下标删除
# pop：删除最后一个元素
# remove：根据元素的值进行删除


# ###########################
# 异常处理
# try:
#     open('a.txt','r')
# except:
#     print('异常。')

# try:
#     print(num)
# except (IOError,NameError,Exception) as result:
#     print(result)

# try:
#     num = 100
#     print(num)
# except NameError as errorMsg:
#     print('产生了错误：%s'%errorMsg)
# else:
#     print('没有异常')

# try:
#     num = 100
#     print(num1)
# except NameError as errorMsg:
#     print('产生异常：%s'%errorMsg)
# else:
#     print('没有异常。')
# finally:
#     print('finaly执行。')

# 抛出异常  raise
# try:
#     raise Exception('抛出异常')
# except:
#     print('异常')
#     raise
# print('结束')

# 嵌套异常
# try:
#     try:
#         try:
#             print(num)
#         except (FileNotFoundError) as e:
#             print(e)
#     except (IOError) as e:
#         print(e)
# except (NameError) as e:
#     print(e)

# 自定义异常
# class ShortInputException(Exception):
#     "自定义异常类"
#     def __init__(self,length,atleast):
#         super().__init__()
#         self.length = length
#         self.atleast = atleast
# def main():
#     try:
#         s = input('请输入：')
#         if len(s) < 3:
#             raise ShortInputException(len(s),3)
#     except ShortInputException as result:
#         print('ShortInputException的长度是：%d,长度至少应该是%d'%(result.length,result.atleast))
#     else:
#         print('没有异常')
# main()


# 自定义异常  是Error或者Exception类的字类
# class OneException(Exception):
#     "自定义异常类"
#     def __init__(self,length,long):
#         super().__init__(length,long)
#         self.length = length
#         self.long = long
# def main():
#     try:
#         a = input('请输入：')
#         if len(a) < 3:
#             raise OneException(len(a),3)
#     except OneException as e:
#         print('OneException:长度为：%s,应为 %s'%(e.length,e.long))
#     else:
#         print('没有异常')
# main()











# a = {'name' : 'zhangsan','age' : 'zhang san'}
# print('空格的长度为：' + str(len(a)))
# print('空格的长度为：' + str(len(a['age'])))



