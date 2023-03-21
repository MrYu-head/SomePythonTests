import pandas as pd
import numpy as np
# 1如何使用列表和字典创建 Series
#     使用列表创建 Series
df = pd.Series([1,2,3],index=list('abc'))
print(df)
#     使用 name 参数创建 Series
# df = pd.Series(name=)
#     使用字典创建 Series
df = pd.Series({'name':'zhangsan','age':18,'sex':'male'})
print(df)
# 2如何使用 Numpy 函数创建 Series
df = pd.Series(np.arange(1,10,2),index=list('abcde'),dtype='float')
print(df)
# 3如何获取 Series 的索引和值
df = pd.Series([1,2,3],index=list('abc'))
print('获取索引：',df.index)
print('获取值:',df.values)
# 4如何在创建 Series 时指定索引
df = pd.Series([1,2,3,4,5],index=list('abcde'))
print(df)
# 5如何获取 Series 的大小和形状
print('Series大小：',df.size)
print('Series形状：',df.shape)
# 6如何获取 Series 开始或末尾几行数据
print('开始3行：',df[0:4])
print('末尾2行：',df[-3:])
# 7使用切片获取 Series 子集
print(df)
# 8如何创建 DataFrame
df = pd.DataFrame([1,2,3,4,5,6,7,8,9],index=list('abcdefghi'))
print(df)
# 9如何设置 DataFrame 的索引和列
df = pd.DataFrame([1,2,3,4,5,6,7,8,9],columns=['值'],index=list('abcdefghi'))
print(df)
# 10如何重命名 DataFrame 的列名称
df.rename(columns={'值':'实际值'},inplace=True)
print(df)
# 如何根据 Pandas 列中的值从 DataFrame 中选择或过滤行
df = pd.DataFrame(np.arange(12).reshape(3,4),columns=['一列','二列','三列','四列'],index=list('abc'))
# print(df[df['EMPNO'] == '7499'])
# 11迭代 DataFrame 的行 和列
# print('--------------------------')
# print(df)
# # 迭代行：
# for i in range(0,4):
#     print(df[i:0])

# 12如何通过名称或索引删除 DataFrame 的列

# 13向 DataFrame 中新增列
# 14如何从 DataFrame 中获取列标题列表
df = pd.read_csv('./tmp001.csv')


# 15如何随机生成 DataFrame
df = pd.DataFrame(np.random.randint(0,10,(3,4)))
print(df)
# 16如何选择 DataFrame 的多个列
# 17如何将字典转换为 DataFrame
df = pd.DataFrame({'id':[1,2],'name':['jack','rose'],'age':[18,19],'height':['180cm','190cm']})
print(df)
# 18使用 ioc 进行切片
# 19检查 DataFrame 中是否是空的
# 20在创建 DataFrame 时指定索引和列名称
# 21使用 iloc 进行切片
# 22iloc 和 loc 的区别
# 23使用时间索引创建空 DataFrame
# 24如何改变 DataFrame 列的排序
# 25检查 DataFrame 列的数据类型
# 26更改 DataFrame 指定列的数据类型
# 27如何将列的数据类型转换为 DateTime 类型
# 28将 DataFrame 列从 floats 转为 ints
# 29如何把 dates 列转换为 DateTime 类型
# 30两个 DataFrame 相加
# 31在 DataFrame 末尾添加额外的行
# 32为指定索引添加新行
   
# 33在 DataFrame 顶部添加一行
# 34如何向 DataFrame 中动态添加行
# 35在任意位置插入行
# 36使用时间戳索引向 DataFrame 中添加行
# 37为不同的行填充缺失值
# 38append, concat 和 combine_first 示例
# 39取行和列的平均值
# 40计算行和列的总和
# 41连接两列
# 42过滤包含某字符串的行
# 43过滤索引中包含某字符串的行
# 44使用 AND 运算符过滤包含特定字符串值的行
# 45查找包含某字符串的所有行
# 46如果行中的值包含字符串，则创建与字符串相等的另一列
# 47计算 pandas group 中每组的行数
# 48检查字符串是否在 DataFrme 中
# 49从 DataFrame 列中获取唯一行值
# 50计算 DataFrame 列的不同值
# 51删除具有重复索引的行
# 52删除某些列具有重复值的行
# 53从 DataFrame 单元格中获取值
# 54使用 DataFrame 中的条件索引获取单元格上的标量值
# 55设置 DataFrame 的特定单元格值
# 56从 DataFrame 行获取单元格值
# 57用字典替换 DataFrame 列中的值
# 58统计基于某一列的一列的数值
# 59处理 DataFrame 中的缺失值
# 60删除包含任何缺失数据的行
# 61删除 DataFrame 中缺失数据的列
# 62按降序对索引值进行排序
# 63按降序对列进行排序
# 64使用 rank 方法查找 DataFrame 中元素的排名
# 65在多列上设置索引
# 66确定 DataFrame 的周期索引和列
# 67导入 CSV 指定特定索引
# 68将 DataFrame 写入 csv
# 69使用 Pandas 读取 csv 文件的特定列
# 70Pandas 获取 CSV 列的列表
# 71找到列值最大的行
# 72使用查询方法进行复杂条件选择
# 73检查 Pandas 中是否存在列
# 74为特定列从 DataFrame 中查找 n-smallest 和 n-largest 值
# 75从 DataFrame 中查找所有列的最小值和最大值
# 76在 DataFrame 中找到最小值和最大值所在的索引位置
# 77计算 DataFrame Columns 的累积乘积和累积总和
# 汇总统计
# 78查找 DataFrame 的均值、中值和众数
# 79测量 DataFrame 列的方差和标准偏差
# 7计算 DataFrame 列之间的协方差
# 80计算 Pandas 中两个 DataFrame 对象之间的相关性
# 81计算 DataFrame 列的每个单元格的百分比变化
# 82在 Pandas 中向前和向后填充 DataFrame 列的缺失值
0
1
2
3
4
5
6
7
8
9

