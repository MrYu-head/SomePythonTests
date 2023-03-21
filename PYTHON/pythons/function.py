''''''


# 定义一个函数，能够完成打印信息的功能
# def printinfo():
#     "打印功能"
#     print('---')
# printinfo()


# def test1(a,b):
#     "完成对两个数求和"
#     print("%d"%(a+b))
# test1(1,3)
# #函数说明
# help(test1)

# def addnum(a,b):
#     c = a + b
#     print(c)
# addnum(1,4)
# addnum(b = 9,a = 1)


##缺省函数
# def printinfo(name,age = 35):
#     "打印任何传入的字符串"
#     print("name:",name)
#     print("age:",age)
# printinfo(name = "李四")
# printinfo(name = "张三",age = 18)


# 不定长参数  *args为没有声明的参数，元组  **kwargs存放命名参数，字典
# def fun(a,b,*args,**kwargs):
#     "可变参数"
#     print("a=",a)
#     print("b=",b)
#     print("args=",args)
#     print("kwargs=",kwargs)
#     for k,v in kwargs.items():
#         print(k,"=",v)
# fun(1,2,3,4,5,m=6,n=7,p=8)
# def func(a,b,*args,**kwargs):
# def func(a,b,*yuanzu,**zidian):
#     print(a)
#     print(b)
#     print(yuanzu)
#     print(zidian)
# func(1,2,3,4,5,6,7,8,9,name='张三',age='19',sex='男')


# # 引用传参
# def selfAdd(a):
#     "引用传参s"
#     print(a)
# b = 10
# selfAdd(b)
# c = [1,2,3]
# selfAdd(c)


# ##函数的嵌套调用
# def funa():
#     print('---这是a')
#     print('---aaa---')
#
# def funb():
#     print('---这是b')
#     funa()
#     print('---bbb---')
# funb()


#可变类型变量：集合、字典、列表
#不可变类型变量：数字类型、字符串类型、元组

# a = 1
# def func():
#     a += 1
#     print(a)
# func()

#修改列表
# list = [1]
# def func():
#     for i in range(1,11):
#         list.append(i)
#     print(list)
# func()

# #修改字典
# info = {'name' : '张三'}
# def func():
#     info['age'] = 19
#     print(info)
# func()

# #修改集合
# aset = {1,2,3,4,5,6,7,8,9}
# bset = {1,3,5,7,9}
# def func():
#     print(aset - bset)
# func()



############################################################
############################################################
############################################################
# 1.写一个函数求三个数的和
# def func1(a,b,c):
#     print('%d'%(a+b+c))
# func1(1,3,5)
# print('##############################')
# 2.写一个函数求三个数的平均值
# def func2(a,b,c):
#     print('%d'%((a+b+c)/3))
# func2(1,3,5)
# print('##############################')
# 3.请用函数实现一个判断用户输入的年份是否是闰年的程序
# y = int(input('请输入一个年份：'))
# def func3(y):
#     if y <= 0:
#         print('请输入正确格式的年份!')
#     else:
#         if (y%4 == 0) and (y%100 != 0):
#             print('%d年是闰年。'%y)
#         if (y%400 == 0):
#             print('%d年是闰年。'%y)
#         else:
#             print('%d年是平年。'%y)
# func3(y)
# print('##############################')
# 4.编写“学生管理系统”，要求如下：
# 	必须使用自定义函数，完成对程序的模块化
# 	学生信息至少包含：姓名、年龄、学号，除此以外可以适当添加
# 	必须完成的功能：添加、删除、修改、查询、退出
'''
userList = []
# 添加学生
def addStu():
    print('======现在进行添加学生操作。')
    newsno = input('请输入学号：')
    newname = input('请输入姓名：')
    newsex = input('请输入性别：')
    newage = input('请输入年龄：')

    # 添加学生之前需要进行判断，判断要添加的学生是否已经存在了，判定条件是按照学号去判定
    for i in userList:
        if i['sno'] == newsno:
            print('存在学号为%s的学生，不能重复添加。' %newsno)
            break
    else:
        # 每次增加名片，学生的id增加1
        userInfo = {}
        userInfo['sno'] = newsno
        userInfo['name'] = newname
        userInfo['sex'] = newsex
        userInfo['age'] = newage
        userList.append(userInfo)
        print('学生添加成功！\n')
# 删除学生
def deleteStu():
    print('现在进行删除学生的操作.')
    dno = input('删除学生。请输入要删除的学生的学号:')
    if len(userList) > 0:
        for i in userList:
            if i['sno'] == dno:
                # 查找到要删除的学生对应的列表的下标
                for k, v in enumerate(userList):
                    # 当下标对应的字典与要删除的学生字典匹配成功，则删除该字典
                    if i == v:
                        del userList[k]
                        print('删除成功，删除了学号为%s的学生\n' % dno)
                        break
    else:
        print('学生字典不存在，请重试。\n')
# 修改学生
def modifyStu():
    print('现在进行修改学生的操作.')
    btn = input('请输入要修改信息的学生的学号：')  # 根据学号修改学生字典信息，查出userList对应的k,v,然后根据k修改
    # 修改之前先判断名片字典是否存在
    if len(userList) > 0:
        # 遍历列表，查找学号对应的字典
        for i in userList:
            if i['sno'] == btn:
                # 查找到学生字典,可以进行修改操作
                print('++++++++找到了该学号对应的学生字典如下：++++++++')
                print(i)
                for k, v in enumerate(userList):
                    # 当进行修改操作的学生学号查找到了对应的字典，则可以进行修改操作
                    if v['sno'] == i['sno']:
                        choice = int(input(
                            '======可进行的修改操作如下:\n1-修改部分信息\t2-修改全部信息\n请输入要进行的修改操作：'))
                        if choice == 1:
                            print(
                                '======部分修改。可进行的修改操作如下:\n\t1------修改学号\n\t2------修改姓名\n\t3------修改性别\n\t4------修改年龄')
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
                        # 修改多条数据，包括所有数据
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
# 查询学生
def checkStu():
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
# # 退出系统
# def exitSys():
#     print('退出系统。')

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
    if tab == 1:
        addStu()
    if tab == 2:
        deleteStu()
    if tab == 3:
        modifyStu()
    if tab == 4:
        checkStu()
    if tab == 5:
        print('退出系统')
        break
'''

# 5.编写程序，实现文件复制


































