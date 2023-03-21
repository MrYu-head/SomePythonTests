# import sys

# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))
#     for i in line:
#         if i == 'Allen':
#             exit()
#     else:
#         line.append('Allen')
list = []
list1 = input()
list = list1.split(' ')
print(list)
list.insert(0,'Allen')
print(list)