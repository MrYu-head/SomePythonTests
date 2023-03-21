# 异常
# 1.捕获异常
# try:
#     print('------')
#     open('111.txt','r')
# except FileNotFoundError:
#     print('文件不存在。')

# 1.2.捕获多个异常
# try:
#     print(num)
#     open('111.txt','r')
# except (IOError,NameError,Exception) as result:
#     print('出现异常',result)
    

# 如果没有捕获到异常 执行else
# try:
#     num = 10
#     print(num)
# except NameError as errorMsg:
#     print('出现异常' + errorMsg)
# else:
#     print('没有出现异常。')


# 3.finally  无论产生什么异常，finally都会执行，如文件的关闭等操作
# try:
#     num = 10
#     print(num)
# except NameError as errorMsg:
#     print('出现异常：' + errorMsg)
# else:
#     print('没有出现异常')
# finally:
#     print('num的值为：' + str(num))

# 文件操作
# with open
# with open('D:/1.txt','a',encoding='utf-8') as f:
#     data = f.write('\n我叫张三')
#     print(data)

# userList = ['张三','李四','王五','赵六','孙琪']
# with open('D:/2.txt','a',encoding='utf-8') as f:
#     for i in userList:
#         data = f.write(i+'\n')
#         print(data)

with open('D:/1.txt','r',encoding='utf-8') as f:
    data = f.read()
    print(data)

# 4.抛出异常
# try:
#     print(num)
#     raise Exception('异常。')
# except:
#     print('111')
#     raise
# print('结束')



# 5.自定义异常
# class ShortInputException(Exception):
#     '''自定义的异常类'''
#     def __init__(self, length, atleast):
#         super().__init__()
#         self.length = length
#         self.atleast = atleast

# def main():
#     try:
#         s = input('请输入 --> ')
#         if len(s) < 3:
#             # raise引发一个自定义的异常
#             raise ShortInputException(len(s), 3)
#     except ShortInputException as result:#这个变量被绑定到了错误的实例
#         print('ShortInputException: 输入的长度是 %d,长度至少应是 %d'% (result.length, result.atleast))
#     else:
#         print('没有异常发生.')

# main()







