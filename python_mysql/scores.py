import pymysql

'''
成绩表：
  id
  用户名
  课程
  分数
  可以根据用户名查询对应用户的课程成绩
'''

# 1.根据用户名查询用户的所有成绩
def nameQueryScores():
    db = pymysql.connect(host='localhost',user='root',password='111111',database='pythontest')
    cursor = db.cursor()
    name_query_sql = 'select * from scores where username = %s'
    query_name = input('请输入要查询成绩的用户名：')
    query_array = [(query_name)]
    try:
        cursor.execute(name_query_sql,query_array)
    except Exception as e:
        print('出现错误：',e)
    cursor.close()
    pass
        


# 2.根据课程查询该课程所有用户的成绩
def courseQueryScores():
    db = pymysql.connect(host='localhost',user='root',password='111111',database='pythontest')
    cursor = db.cursor()


def queryScores():
    print('*'*10,'查询成绩','*'*10,'\n',\
        '*'*3,'1.根据用户名查询成绩\n',\
        '*'*3,'2.根据课程查询成绩'   )
    queryTab = int(input('请输入要进行的操作：'))
    try:
        if queryTab == 1:
            print('----根据用户名查询成绩----')
            nameQueryScores()
        elif queryTab == 2:
            print('----根据课程查询成绩----')
            courseQueryScores()
        else:
            print('输入的指令不正确，请重试。')
            queryTab()
    except Exception as e:
        print(e)
        
queryScores()

