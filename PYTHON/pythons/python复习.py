# 2022-12-19
# python是一种解释性、互动性、面向对象的脚本语言  没有编译的环节

# chr(x)--将一个整数转换为一个字符
# ord(x)--将一个字符转换为他的整数值

# a = 12
# print(a)
# a += 10
# print(a)

# %c  %s  %d  %f
# a = 2
# b = 3
# # 计算a的b次方
# print(a**b)
# # 取整数，向下取整
# print(24//9)
# print(9//2)


# 条件控制
# 循环四要素：初始变量  循环条件  循环操作  循环迭代


'''
1.编写程序，完成以下要求：
提示用户进行输入数据-input
获取用户的数据数据（需要获取2个）
对获取的两个数字进行求和运行，并输出相应的结果
'''
# a = int(input('请输入第一个数：'))
# b = int(input('请输入第二个数：'))
# print(a + b)

'''
3. 编写程序，从键盘获取一个人的信息，然后按照下面格式显示
   ==================================
    姓名: 李四    
    QQ:xxxxxxx
    手机号:131xxxxxx
    公司地址:北京市xxxx
    ==================================
'''
# name = input('请输入姓名：')
# qq = int(input('请输入qq号：'))
# phone = int(input('请输入手机号：'))
# address = input('请输入地址：')
# print('='*20)
# print('姓名：' + name)
# print('QQ:' + str(qq))
# print('手机号：' + str(phone))
# print('公司地址：' + address)
# print('='*20)

'''
4.从键盘获取用户名、密码
如果用户名和密码都正确（预先设定一个用户名和密码），
那么就显示“欢迎进入xxx的世界”，否则提示密码或者用户名错误
'''
# username = 123
# password = 123123
# name = int(input('请输入用户名：'))
# pwd = int(input('请输入密码：'))
# if (name == username) and (pwd == password):
#     print('欢迎进入。')
# else:
#     print('用户名或密码错误。')

'''
5.设计猜拳
随机数代码如下:
import random
print(random.randint(1,3))  可以随机产生1或2或3
1      2      3
石头    剪刀   布
'''
# import random
# b = random.randint(1,3)
# a = int(input('请输入你要出的数字：'))
# if (a == 1) and (b == 2):
#     print('我赢。')
# elif (a == 1) and (b == 3):
#     print('机器赢。')
# elif (a == 2) and (b == 1):
#     print('机器赢。')
# elif (a == 2) and (b == 3):
#     print('我赢。')
# elif (a == 3) and (b == 1):
#     print('我赢。')
# elif (a == 3) and (b == 2):
#     print('机器赢。')
# else:
#     print('平局。')

'''
6.编写程序，完成以下要求:
提示用户进行输入数据
获取用户的数据数据（需要是3位数）
判断是否是水仙花数。水仙花数是指一个 3 位数，
它的每个位上的数字的 3次幂之和等于它本身（例如153：1^3 + 5^3+ 3^3 = 153）
'''
# a = int(input('请输入一个三位数：'))
# if (a - 100 >= 0) and (999 - a >= 0):
#     b = int(a/100)
#     c = int(a/10%10)
#     d = int(a%10)
#     if (b**3 + c**3 + d**3 == a):
#         print('%d是水仙花数。'%a)
#     else:
#         print('%d不是水仙花数。'%a)
# else:
#     print('输入的数不是一个三位数。')


'''
列表 []
字典{} { key:value }



'''
# nameList = ['张三','李四','王五','赵六','小明']
# nameList.append('赵六')
# print(nameList)
# for tmp in nameList:
#     print(tmp,end='')
# print()
# # 修改元素
# nameList[1] = '小王'
# for tmp in nameList:
#     print(tmp,end='')
# 查找元素：
# name = input('请输入要查找的姓名:')
# if name in nameList:
#     print('找到姓名。' + name)
# else:
#     print('没有找到。')

# print(nameList)
# 删除元素
# del:根据下标删除
# del nameList[2]
# print(nameList)
# pop：删除最后一个元素
# nameList.pop()
# print(nameList)
# remove：根据值删除元素
# nameList.remove('王五')
# print(nameList)
# nameList.reverse()
# print(nameList)


# a = [1,2,3]
# b = [4,5,6]
# a.extend(b)
# print(a)
# a.extend(b)
# print(a)
# a.insert(1,3)
# print(a)
# a = [1,5,8,3,7,6,2,0]
# a.reverse()
# a.sort()
# print(a)


# userInfo = {'name' : '张三','age' : 18,'sex' : '男'}
# print(userInfo)
# print(userInfo['name'])
# age1 = userInfo.get('age')
# print(age1)
# 修改元素
# userInfo['age'] = 20
# print(userInfo)
# 删除元素
# del userInfo['name']
# print(userInfo)
# 清空整个字典  clear
# userInfo.clear()
# print(userInfo)

# for k,v in enumerate(userInfo):
#     print(k,v)

# 1. 计算1~100的和（包含1和100）
# s = 0
# for i in range(1,101):
#     s = s + i
# print(s)

# 2. 计算1~6的乘积（包含1和6）
# sum = 1
# for i in range(1,7):
#     sum = i * sum
# print(sum)

# 3. 计算1~100之间偶数的和（包含1和100）
# s = 0
# for i in range(1,101,2):
#     s = s + i
# print(s)

# 4. 计算1~100之间可以被3又能被5整数的数的个数（包含1和100）
# s = 0
# for i in range(1,101):
#     if (i%3==0) and (i%5==0):
#         s = s + 1
# print(s)

# 5.使用循环，完成以下图形的输出
# *
# * *
# * * *
# * * * *
# * * * * *
# for i in range(1,6):
#     for j in range(1,i+1):
#         print('* ',end='')
#     print('')

# 6.使用循环九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         c = i * j
#         print(str(i)+'*'+str(j)+'='+str(c),end=' ')
#     print()
# 7.判断一个是是否是质数(质数就是除了1和本身，没有其他的公约数)
# a = int(input('请输入一个数：'))
# for i in range(2,a):
#     if (a%i==0):
#         print(str(a) + '不是质数。')
# else:
#     print(str(a) + '是质数。')

# 8.求2-1000的质数的个数
# n = 0
# for i in range(2,1001):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         n += 1
# print(n)


# def zhangsan(a,b):
#     "文档说明"
#     print(a+b)
# zhangsan(1,2)

# a = 100
# def test():
#     print(a)
# def test2():
#     global a
#     a = 300
#     print(a)
# test()
# test2()

# 递归
# n = 0
# def f1():
#     global n
#     n += 1
#     print('执行第%d次'%n)
#     if n < 10:
#         f1()
# f1()

# 计算阶乘
# def info(n):
#     if n == 1:
#         return n
#     else:
#         return n * info(n-1)
# print(info(4))

# 编写程序，设计“学生管理系统”项目
# 需要完成的基本功能：
# 添加学生(包括学号，姓名，年龄，性别)
# 删除学生
# 修改修改
# 查询查询
# 退出系统
# 程序运行后，除非选择退出系统，否则重复执行功能

# 学生列表
# nameList = []
# def addStu():
#     # 设定数据的输入格式不能为空或者空格
#     sno = input('请输入学生学号：')
#     if len(sno.strip()) == 0:
#         print('输入的信息不符合标准，请重新输入。')
#         addStu()
#     else:
#         name = input('请输入学生姓名：')
#         if len(name.strip()) == 0:
#             print('输入的信息不符合标准，请重新输入。')
#             addStu()
#         else:
#             age = input('请输入年龄：')
#             if len(age.strip()) == 0:
#                 print('输入的信息不符合标准，请重新输入。')
#                 addStu()
#             else:
#                 sex = input('请输入性别：')
#                 if len(sex.strip()) == 0:
#                     print('输入的信息不符合标准，请重新输入。')
#                     addStu()
#                 else:
#                     stuInfo = {}
#                     stuInfo['sno'] = sno
#                     stuInfo['name'] = name
#                     stuInfo['age'] = int(age)
#                     stuInfo['sex'] = sex
#                     # 以学号作为标识符，判断输入的学生是否存在
#                     # for循环、find、get()
#                     # 1.for循环判断  实现成功。
#                     # for i in nameList:
#                     #     if stuInfo['sno'] == i['sno']:
#                     #         print('该学生已存在，不能重复添加！')
#                     #         break
#                     # else:
#                     #     nameList.append(stuInfo)
#                     #     print('添加成功。')
#                     #     print('学生信息添加成功。',nameList)
#                     # caozuo()
#                     # 2.find判断  实现失败。
#                     # for i in nameList:
#                     #     tmp = i['sno']
#                     #     print(tmp)
#                     #     if(i.find(tmp)) == -1:
#                     #         print('该学生已存在，不能重复添加！')
#                     #         break
#                     # else:
#                     #     nameList.append(stuInfo)
#                     #     print('添加成功。')
#                     #     print('学生信息添加成功。',nameList)
#                     # caozuo()

#                     # 3.get()判断  实现成功。
#                     for i in nameList:
#                         if i.get('sno') == sno:
#                             print('学生已存在，请重试。')
#                             break
#                     else:
#                         nameList.append(stuInfo)
#                         print('添加成功。')
#                         print('学生信息添加成功。\n',nameList)
#                         caozuo()


# def delStu():
#     # 删除  del-删除整个字典、clear-清空字典数据，字典还存在。
#     del_sno = input('请输入要删除的学生的学号：')
#     for k,v in enumerate(nameList):
#         if v.get('sno') == del_sno:
#             del nameList[k]
#             print('删除学生成功。')
#             caozuo()
#     else:
#         print('要删除的学生的学号不存在。')
#         caozuo()


# def modStu():
#     # 修改全部信息、修改学号、修改姓名、修改年龄、修改性别
#     mod_tab = int(input('------可进行的操作如下所示：\n1------根据学号修改学生的全部信息\n2------修改学号\n3------修改姓名\n4----修改年龄\n5------修改性别\n请输入要进行的操作：'))
#     if mod_tab == 1:
#         mod_all_sno = input('******根据学号修改学生的全部信息******\n请输入要修改信息的学生的学号：')
#         for kno,val in enumerate(nameList):
#             if val.get('sno') == mod_all_sno:
#                 print('找到该学生,信息如下：')
#                 print(val)
#                 mod_new_sno = input('请输入修改后的学号：')
#                 if len(mod_new_sno.strip()) == 0:
#                     print('输入的信息不符合标准，请重新输入。')
#                     modStu()
#                 else:
#                     mod_new_name = input('请输入修改后的姓名：')
#                     if len(mod_new_name.strip()) == 0:
#                         print('输入的信息不符合标准，请重新输入。')
#                         modStu()
#                     else:
#                         mod_new_age = int(input('请输入修改后的年龄：'))
#                         if len(str(mod_new_age).strip()) == 0:
#                             print('输入的信息不符合标准，请重新输入。')
#                             modStu()
#                         else:
#                             mod_new_sex = input('请输入修改后的性别：')
#                             if len(mod_new_sex.strip()) == 0:
#                                 print('输入的信息不符合标准，请重新输入。')
#                                 modStu()
#                             else:
#                                 nameList[kno]['sno'] = mod_new_sno
#                                 nameList[kno]['name'] = mod_new_name
#                                 nameList[kno]['age'] = mod_new_age
#                                 nameList[kno]['sex'] = mod_new_sex
#                                 print('学生信息修改成功，已修改 ' + mod_all_sno + ' 学生的全部信息。\n')
#                                 caozuo()
#         else:
#             print('学生不存在。')
#             caozuo()
#     elif mod_tab == 2:
#         mod_stu_sno = input('------修改学生的学号。\n  请输入要修改的学生的学号：')
#         for k,val in enumerate(nameList):
#             if val.get('sno') == mod_all_sno:
#                 print('找到该学生,下标为：' + str(k) + ',学生学号为：' + nameList[k]['sno'])
#                 mod_new_stu_sno = input('请输入修改后的学号：')
#                 if len(mod_new_stu_sno.strip()) == 0:
#                     print('输入的信息不符合标准，请重新输入。')
#                     modStu()
#                 else:
#                     nameList[k]['sno'] = mod_new_stu_sno
#                     print('学生学号修改成功！旧学号：' + mod_stu_sno + ',新学号：' + mod_new_stu_sno)
#                     print('该学生完整信息如下：')
#                     print(nameList[k])
#                     print()
#                     caozuo()
#             else:
#                 print('学生列表中找不到该学号对应的学生信息，学生不存在。\n')
#                 caozuo()
#     elif mod_tab == 3:
#         mod_stu_sno = input('------修改学生的姓名。\n  请输入要修改姓名的学生的学号：')
#         for k,val in enumerate(nameList):
#             if val.get('sno') == mod_stu_sno:
#                 print('找到该学生,下标为：' + str(k) + ',姓名为：'+nameList[k]['name'])
#                 mod_new_stu_name = input('请输入修改后的姓名：')
#                 if len(mod_new_stu_name.strip()) == 0:
#                     print('输入的信息不符合标准，请重新输入。')
#                     modStu()
#                 else:
#                     nameList[k]['name'] = mod_new_stu_name
#                     print('学生姓名修改成功！旧姓名：' + nameList[k]['name'] + ',新姓名：' + mod_new_stu_name)
#                     print('该学生完整信息如下：')
#                     print(nameList[k])
#                     print()
#                     caozuo()
#             else:
#                 print('学生列表中找不到该学号对应的学生信息，学生不存在。\n')
#                 caozuo()
#     elif mod_tab == 4:
#         mod_stu_sno = input('------修改学生的年龄。\n  请输入要修改年龄的学生的学号：')
#         for k,val in enumerate(nameList):
#             if val.get('sno') == mod_stu_sno:
#                 print('找到该学生,下标为：' + str(k) + ',年龄为：'+nameList[k]['age'])
#                 mod_new_stu_age = input('请输入修改后的年龄：')
#                 if len(mod_new_stu_age.strip()) == 0:
#                     print('输入的信息不符合标准，请重新输入。')
#                     modStu()
#                 else:
#                     nameList[k]['name'] = mod_new_stu_name
#                     print('学生年龄修改成功！旧年龄：' + nameList[k]['age'] + ',新年龄：' + mod_new_stu_age)
#                     print('该学生完整信息如下：')
#                     print(nameList[k])
#                     print()
#                     caozuo()
#             else:
#                 print('学生列表中找不到该学号对应的学生信息，学生不存在。\n')
#                 caozuo()
#     elif mod_tab == 5:
#         mod_stu_sno = input('------修改学生的性别。\n  请输入要修改性别的学生的学号：')
#         for k,val in enumerate(nameList):
#             if val.get('sno') == mod_stu_sno:
#                 print('找到该学生,下标为：' + str(k) + ',性别为：'+nameList[k]['sex'])
#                 mod_new_stu_sex = input('请输入修改后的性别：')
#                 if len(mod_new_stu_sex.strip()) == 0:
#                     print('输入的信息不符合标准，请重新输入。')
#                     modStu()
#                 else:
#                     nameList[k]['sex'] = mod_new_stu_sex
#                     print('学生性别修改成功！旧性别：' + nameList[k]['sex'] + ',新性别：' + mod_new_stu_sex)
#                     print('该学生完整信息如下：')
#                     print(nameList[k])
#                     print()
#                     caozuo()
#             else:
#                 print('学生列表中找不到该学号对应的学生信息，学生不存在。\n')
#                 caozuo()
#     else:
#         print('输入的指令错误，请重新输入！')
#         modStu()


# def viewStu():
#     view_item = int(input('可进行的操作如下：\n      1----------查询所有学生信息\n      2----------根据学号查询学生信息\n请输入要查询的选项：'))
#     if view_item == 1:
#         if len(nameList) == 0:
#             print('学生列表为空，请先添加学生。')
#             caozuo()
#         else:
#             print('查询到的学生表信息如下：')
#             for view_list in nameList:
#                 print(view_list)
#                 print()
#             caozuo()
#     if view_item == 2:
#         view_one_item = input('请输入要查询信息的学生的学号：')
#         for view_list in nameList:
#             if view_list.get('sno') == view_one_item:
#                 print('数据查询成功，学生数据如下：')
#                 print(view_list)
#                 print()
#                 caozuo()
#         else:
#             print('很抱歉，学生不存在，查询不到该学生的信息。')
#             caozuo()
#     else:
#         print('输入的指令不正确。')
#         caozuo()


# def caozuo():
#     print('*' * 20)
#     print('学生管理系统')
#     print('可进行如下操作：\n'
#          + '  1----添加学生\n'
#          + '  2----删除学生\n'
#          + '  3----修改学生信息\n'
#          + '  4----查看学生信息\n'
#          + '  5----退出系统')
#     print('*' * 20)
#     node = int(input('请输入你要进行的操作：'))
#     if node == 1:
#         print('*'*10,'添加学生','*'*10)
#         addStu()
#     elif node == 2:
#         print('*'*10,'删除学生','*'*10)
#         delStu()
#     elif node == 3:
#         print('*'*10,'修改学生信息','*'*10)
#         modStu()
#     elif node == 4:
#         print('*'*10,'查询学生信息','*'*10)
#         viewStu()
#     elif node == 5:
#         print('退出系统，再见！')
#     else:
#         print('出入的指令不正确，请重新输入。')

# caozuo()


# 推导式
# list = [i for i in range(1,11) if i%2]
# print(list)


# print(ord('A'))
# print(ord('Z'))

# 1．编写一个类A，该类创建的对象可以调用方法f输出小写的英文字母表。然
# 后再编写一个A类的子类B，子类B创建的对象不仅可以调用方法f输出小写的英文字母表，
# 而且可以调用子类新增的方法g输出大写的英文字母表。测试类A与类B。
# class A:
#     def f(self):
#         for i in range(97,123):
#             print(chr(i),end=' ')
# print()

# class B(A):
#     def g(self):
#         for j in range(65,91):
#             print(chr(j),end=' ')

# obj1 = B()
# obj1.f()
# obj1.g()


# 2．按要求编写一个应用程序：
# （1）定义一个类，描述一个矩形，包含有长、宽两种属性，和计算面积方法。
# （2）编写一个类，继承自矩形类，同时该类描述长方体，具有长、宽、高属性，
# 和计算体积的方法。
# （3）创建一个长方体，定义其长、宽、高，输出其面积和体积。
# class juxing:
#     def __init__(self,l,k):
#         self.l = l
#         self.k = k
#     def mianji(self,l,k):
#         mianji = l * k
#         print('面积为：'+ str(mianji))
# class changfangti(juxing):
#     def __init__(self,h):
#         self.h = h
#     def tiji(self,l,k,h):
#         tiji = l * k * h
#         print('体积为：' + str(tiji))

# obj2 = changfangti(2)
# obj2.mianji(2,3)
# obj2.tiji(2,3,2)


# 3.要求编写一个应用程序：
# 定义类Circle(圆)，属性有半径，构造方法可以为属性初始化，返回圆的面积
# 定义类Cylinder(圆柱),属性有半径，高;返回圆柱的体积
# class Circle:
#     def __init__(self,r):
#         self.r = r
#     def mianji(self):
#         mianji = 3 * self.r**2
#         print('面积为：' + str(mianji))
# class Cylinder:
#     def __init__(self,r2,h):
#         self.r2 = r2
#         self.h = h
#     def tiji(self):
#         tiji = 3 * self.r2**2 * self.h
#         print('体积为：' + str(tiji))
# obj3 = Circle(2)
# obj3.mianji()
# obj4 = Cylinder(2,3)
# obj4.tiji()

# 4.从键盘上接收2个数
#
# ，完成2个数相除功能；考虑发生的异常并处理(处理方式给出提示即可)
# a = int(input('第一个数：'))
# b = int(input('第一个数：'))
# if len(str(a)) == 0 or len(str(b)) == 0:
#     print('除数不能为0')
# else:
#     c = a / b
#     print(str(c))



# def xiangchu(a, b):
#     try:
#         a = int(input('第一个数：'))
#         b = int(input('第一个数：'))
#         if len(a) == 0 or len(b) == 0:
#             raise LengthInputException(len(a))
#     except:
#         print()


# map()
list(map(lambda x:x*x,[1,2]))




