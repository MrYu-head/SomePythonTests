import numpy as np
a = np.array([1, 2, 3])
print(a)


# ones()
list1 = np.ones(4)
list2 = np.zeros(4)
print(list1)
print(list2)

list1_1 = np.ones((3,4),dtype=int)
print('----------------')
print(list1_1)

# 随机数
list3 = np.random.default_rng()
list3.random(4)
print(list3)
list4 = np.random.random()
print(list4)


# 索引和切片
data1 = np.array([1,2,3,4,5,6,7,8,9,10])
print(data1[1])  #2
print(data1[0:3])  #[1,2,3]
print(data1[1:])  #[2,3,4,5,6,7,8,9,10]
print(data1[:4])  #[1,2,3,4]
print(data1[-6:])  #[5,6,7,8,9,10]


data2 = np.array([1,2,3,4,5])
ones = np.ones((4,5),dtype=int)  #1指的是shape，就是维度,列要对应
print(ones)
print(data2+ ones)


print(data2 - ones)
print(data2 * ones)

# 广播
data3 = np.array((1,2,3))
data3_1 = 2
print(data3 * data3_1)



# 创建矩阵
data4 = np.array(((1,2),(3,4),(5,6)))
print(data4)
data4_1 = np.ones((3,2))
print(data4_1)
print(data4)
print('-----------')
print(data4[0,1])
print(data4[1:3])
print(data4[1:2])
print(data4[0:2])
print(data4[0:2,0])
print(data4[0:2,1])


print('++++++++++++++++++++')
data5 = np.array(((1,2),(5,3),(6,4)))
print(data5)
print(data5.max(axis = 0))
print(data5.max(axis = 1))
print('++++++++++++++++++++')


data6 = np.array(((1,2),(3,4)))
ones = np.array(((1,1),(2,2)))
print(data6 + ones)

ones2 = np.array(((2,3)))
print(data6 * ones2)


print('****************')
print(data6)
print(data5.reshape(2,3))




