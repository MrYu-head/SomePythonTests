# 注： 数组为一维数组，非一维数组都说了数组的形状
import numpy as np
from numpy import random
# 1. 创建一个长度为10并且除了第5个值为1的空向量
print('1'*40)
list1 = np.zeros(10,dtype=int)
list1[4] = 1
print(list1)


# 2. 创建一个值域范围从10到49的向量
print()
print('2'*40)
list2 = np.arange(10,50)
print(list2)


# 3. 反转一个向量(第一个元素变为最后一个)
print()
print('3'*40)
list3 = np.array((1,2,3,4,5))
list3_1 = list3[4::-1]
print(list3_1)

# 4. 创建一个 3x3 并且值从0到8的矩阵
print()
print('4'*40)
list4 = np.array(((0,1,2),(3,4,5),(6,7,8)))
print(list4)

# 5. 找到数组[1,2,0,0,4,0]中非0元素的位置索引
print()
print('5'*40)
list5 = np.array([1,2,0,0,4,0])
for k,v in enumerate(list5):
    print(k,v)
    if v != 0:
        print('非0位置：',k)

# 6. 创建一个 3×3×3的随机数组
print()
print('6'*40)
list6 = np.random.random((3,3,3))
print(list6)

# 7. 创建一个10×10 的随机数组并找到它的最大值和最小值
print()
print('7'*40)
list7 = np.random.randint(1,10,(10,10),dtype=int)
maxva = list7.max()
minva = list7.min()
print('最大值：',maxva,',最小值：',minva)

# 8.创建一个长度为30的随机向量并找到它的平均值
print()
print('8'*40)
list8 = np.random.randint(0,30,30)
avgva = list8.mean()
print(list8)
print(avgva)

# 9. 创建一个二维数组，其中边界值为1，其余值为0
print()
print('9'*40)
list9 = np.ones((10,10),dtype=int)
list9[1:-1,1:-1] = 0
# list9[0,1] = list9[9:10] = 1
print(list9)


#  10. 创建一个2*3的数组，和一个3*2的数组，计算他们的点积
print()
print()
print('10'*100)
list10_1 = np.random.randint(1,10,(2,3))
list10_2 = np.random.randint(1,10,(3,2))
print(np.dot(list10_1,list10_2))


# 11. 对大于5的元素取反
print()
print('11'*40)
list11 = np.random.randint(1,15,(10),dtype=int)
print(list11)
list11_1 = list11.tolist()
print(list11_1)
for i in list11_1:
    if i > 5:
        i = i * -1
        
# for k,v in enumerate(list11_1):
#     print(k,v)
#     for i in v:
#         print('这是现在的：',i,',这是v:',v)
#         if i > 5:
#             list11_1[k] = v * -1
#             continue
#     else:
#         pass
list11_2 = np.array(list11_1)
print(list11_2)

# 12. 找到两个数组中的共同元素
print()
print('12'*40)
list12_1 = np.random.randint(1,20,(15),dtype=int)
list12_2 = np.random.randint(1,20,(15),dtype=int)
print('数组1：',list12_1)
print('数组2：',list12_2)
new_list = []
for i in list12_1:
    if i in list12_2:
        print(i)
        new_list.append(i)
print(new_list)
# list12_3 = new_list.sort(reverse=False)
# print(list12_3)


# 13. 找到两个数组中相同位置的相同元素个数	
print()
print('13'*40)
print(list12_1)
print(list12_2)
sum = 0
print(np.count_nonzero(list12_1 == list12_2))
for i in range(0,len(list12_1)):
    if list12_1[i] == list12_2[i]:
        sum += 1
print(sum)


# 14. 找到两个数组中相同位置的相同元素	
print()
print('14'*40)
print(list12_1)
print(list12_2)
for i in range(0,len(list12_1)):
    if list12_1[i] == list12_2[i]:
        print('找到值：',list12_1[i])

# 15. 创建一个5×5的矩阵，其中每行的数值范围从0到4
print()
print('15'*40)
list15 = np.zeros((5,5),dtype=int)
list_add = np.array((0,1,2,3,4))
print(list15,list_add)
list15_2 = list15 + list_add
print(list15_2)


# 16. 创建一个长度为10的随机向量，并将其排序
print('16'*40)
list16 = np.random.randint(0,10,(10),dtype=int)
print(list16)
tmp = 0
for i in range(0,len(list16)):
    for j in range(0,i):
        if list16[j] > list16[i]:
            tmp = list16[j]
            list16[j] = list16[i]
            list16[i] = tmp
    else:
        pass
print(list16)







b = np.random.randint(1,40,15)
print(b.sort())
c = b.tolist()
print(c)
print(c.sort(reverse=False))

#  6 12 23  2  1 20 14 33  9 22 36 17  24 34
# ###
# 2, 3, 3, 7, 8, 8, 9, 10, 16, 19, 19, 24, 26, 28, 34


  