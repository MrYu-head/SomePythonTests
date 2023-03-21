# import pandas as pd
# import numpy as np

# infoli = ['zhangsan',18,'180cm']
# data1 = pd.Series(infoli)
# data2 = pd.Series(data=infoli,index=list('abc'))
# print(data1,data2)


# info2 = {'name':'zhangsan','age':18,'sex':'nan'}
# data3 = pd.Series(info2)
# print(data3)
# info2_1 = data3.tolist()
# print(info2_1)
# info2_2 = data3.to_dict()
# print(info2_2)

# df = pd.DataFrame(data3)
# print('++++++++',df)
# df = pd.DataFrame(data = data3,columns=['信息'])
# print(df)

# print(data3,'-------')
# s = pd.Series(data=['001','002','003'],index=list('abc'))
# print(s)
# # astype
# a1 = s.astype(int)
# print(a1)

# # map1 = s.map(lambda x:float(x))
# map1 = s.map(float)
# print(map1)

# a2 = pd.Series(data=['005','006'],index=list('ab'))
# a2_1 = pd.concat([s,a2])
# print(a2_1)
# df = pd.concat([s,a2],axis=1)
# print(df)

# print('*'*100)
# info3 = {'name':'zhangsan','age':18,'sex':'nan'}
# df = pd.DataFrame(info3,index=[0])
# print(df)
# df = pd.DataFrame(list(info3.items()))
# print(df)

# # 字典创建
# info4 = {'id':[1,2],'name':['jack','rose'],'age':[18,19],'height':['180cm','190cm']}
# df = pd.DataFrame(info4)
# print(df)
# # 列表创建
# info5 = [[1,2],[11,12]]
# df = pd.DataFrame(info5,columns=['c1','c2'],index=['i1','i2'])
# print(df)


# df = pd.DataFrame(np.arange(12).reshape(3,4))
# print(df)


# date_range = pd.date_range(start='2022-01-01',periods=100)
# data = {
#     'normal' : np.random.normal(loc=0,scale=1,size=100)
# }
# df = pd.DataFrame(data=data,index=date_range)
# print(df)


# df = pd.read_csv('./tmp001.csv')
# print(df)
# print('info',df.info)
# print('dtypes:',df.dtypes)
# # df['DEPTNO'] = df['DEPTNO'].astype('string')
# print('dtypes:',df.dtypes)
# print('tail:',df.tail(3))
# print('head:',df.head(3))

# # 取单列
# print('取单列:',df['EMPNO'])
# print('取多列:',df[['EMPNO','ENAME']])
# print('按行取:',df[0:3])
# print('loc',df.loc[0:2,'EMPNO':'ENAME'])
# print('iloc:',df.iloc[0:4,1:3])
# print('*'*10)
# print(df['HIREDATE'].head(3))
# print(df['HIREDATE'].str.lower())
# print(df['HIREDATE'].str.replace('/','-'))
# print('split转列表:','\n',df['ENAME'].str.split(' '))

# print('+'*100)
# print(df)
# print(df[(df['DEPTNO'] >10) & (df['DEPTNO'] < 30)])


# df = pd.DataFrame([[1,2]])
# df.columns = ['col1','col2']
# print(df)
# df.rename(columns={'col1':'c1'},inplace=True)
# print(df)

# df.loc[0,'col2'] = 11
# print(df)

# df = pd.DataFrame(data = np.full((3,4),np.nan),columns=list('abcd'),index=list('xyz'))
# print(df)
# df.loc['x','a'],df.loc['y','b'],df.loc['z','c'] = 1,2,3
# print(df)
# df = pd.read_csv('./tmp001.csv')
# print(df['COMM'].isnull())
# print(df['COMM'].isna())

# print('%'*100)
# # 修改NaN
# f1 = df.fillna(0)
# f2 = df.fillna(method='ffill')
# print('原来的:',f1)
# print('原来的2：',f2)
# for i in df:
#     if df[i].isna().any():
#         df[i].fillna(value=df[i].mean(),inplace=True)
# print(df)

# print('1'*100)
# df = pd.read_csv('./tmp001.csv')
# df.sort_index(inplace=True,ascending=False,na_position='first')
# print(df)

# # 按值排序
# df.sort_values(by=['EMPNO','SAL'],inplace=True,ascending=True,na_position='last')
# print(df)

# # 设置索引列
# df.set_index(keys=['EMPNO'],inplace=True)
# print(df)

# # 重置索引列
# df.reset_index(inplace=True)
# print(df)

# # 表连接
# print('%'*100)
# left = pd.DataFrame(np.arange(6).reshape(3,2),columns=['a','b'],index=['i1','i2','i3'])
# right = pd.DataFrame(np.arange(4,10).reshape(3,2),columns=['c','d'],index=['i1','i2','i3'])
# print(left)
# print(right)

# # 内连接  inner
# inner = left.join(right,how='inner')
# print('内连接：',inner)
# # 外连接  outer
# outer = left.join(right,how='outer')
# print('外连接：',outer)
# # 左连接  left
# left_join = left.join(right,how='left')
# print('左连接：',left_join)
# # 右连接
# right_join = left.join(right,how='right')
# print('右连接',right_join)


# merge = pd.merge(left=left, right=right, left_on='b', right_on='d', how='left')
# print('merge', merge)


# import random
# a = np.random.randint(1,20,(15))
# print(a)


import pandas as pd
import numpy as np
# 窗口函数
df = pd.DataFrame(np.random.randint(1, 10, size=32).reshape(8, 4),
                  index=pd.date_range('2022-12-1', periods=8),
                  columns=list('ABCD'))
print(df)
df['A_rolling'] = df['A'].rolling(window=3).mean()
print(df)
print('*'*100)
# expanding  扩展窗口函数，从第一个元素开始向后逐个计算
df['A_expanding'] = df['A'].expanding(min_periods=2).sum()
print(df)
# shift移动函数,类似于lead()  lag()
# 获得后面的一个值
df['A_shift+1'] = df['A'].shift(periods=1)
print(df)
# huode前面的一个值
df['A_shitf-1'] = df['A'].shift(periods=-1)
print(df)

# 列转行
df = pd.DataFrame([['张三', 10, 20], ['李四', 30, 40]], columns=['姓名', '语文', '数学'])
print(df)
# 1.stack()  将不变的列设置为索引
df_stack = df.set_index('姓名').stack()
print(df_stack)
# 2.重置索引：
df_stack = df_stack.reset_index()
print(df_stack)
# 3.设置列名
df_stack.columns = ['姓名', '科目', '成绩']
print(df_stack)
print('---------------------')
df = pd.DataFrame([['张三', 10, 20], ['李四', 30, 40], [
                  '王五', 50, 60]], columns=['姓名', '语文', '数学'])
print(df)
# 1.先设置不变的列名为索引
df1 = df.set_index('姓名').stack()
print('11111', df1)
# 2.重置索引
df1 = df1.reset_index()
print('22222', df1)
# 3.设置列名
df1.columns = ['姓名', '科目', '成绩']
print('33333', df1)


# melt
df_melt = df.melt(id_vars='姓名',  # 列转行后不变的列
                  value_vars=['语文', '数学'],  # 需要变动的列名
                  var_name='科目',  # 转换后的字段名
                  value_name='成绩')  # 转换后新表的值的列名
print('df_melt', df_melt)


print('+'*100)
# 行转列
tmp = pd.DataFrame({'姓名': ['张三', '李四', '王五', '张三', '李四', '王五', '张三', '李四', '王五'],
                    '科目': ['英语', '英语', '英语', '数学', '数学', '数学', '语文', '语文', '语文'],
                    '分数': [90, 60, 70, 80, 98, 80, 85, 90, 75]})

print('行转列原始数据')
print(tmp)
# 1.unstack  相当于广播
tmp1 = tmp.set_index(['姓名', '科目'])['分数'].unstack()
print(tmp1)
tmp1 = tmp1.reset_index()
print(tmp1)
df = tmp1.rename_axis(columns=None)
print(df)

# 2.pivot
df = tmp.pivot(index='姓名', columns='科目',
               values='分数').reset_index().rename_axis(columns=None)
print(df)


# 新增一个字段，内容为所有父级ID，例：1.0->3.0->8
df0 = pd.DataFrame([
    (1, '总裁室', np.NaN),
    (2, '研发部', 1),
    (3, '市场部', 1),
    (4, '后端', 2),
    (5, '前端', 2),
    (6, '大数据', 2),
    (7, '数仓开发', 6),
    (8, '数据分析', 6)
], columns=['ID', 'PRODUCTNAME', 'PARENTID'])
print(df0)
print('%'*100)
df0['ID'] = df0['ID'].astype('float')
# df0['PARENTID'] = df0['PARENTID'].astype(int)
for i in df0['ID']:
    for j in df0['PARENTID']:
        if j[2:3] == i[0:1]:
            print(i)
        #     print(j)
        print('111',j)
    print('222',i)


