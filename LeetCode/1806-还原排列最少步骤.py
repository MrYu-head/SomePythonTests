# 1806.还原列表的最少操作步数
# 给你一个偶数 n​​​​​​ ，已知存在一个长度为 n 的排列 perm ，
# 其中 perm[i] == i​（下标 从 0 开始 计数）。
# 一步操作中，你将创建一个新数组 arr ，对于每个 i ：
# 如果 i % 2 == 0 ，那么 arr[i] = perm[i / 2]
# 如果 i % 2 == 1 ，那么 arr[i] = perm[n / 2 + (i - 1) / 2]
# 然后将 arr​​ 赋值​​给 perm 。
# 要想使 perm 回到排列初始值，至少需要执行多少步操作？返回最小的 非零 操作步数。
# i = 0  1  2  3  4  5  6  7  8  9
# arr=0  5  1  6  2  7  3  8  4  9


def jisuan():
    n = int(input('输入n:'))
    if n%2==0 and n <= 1000:
        perm = []
        perm_origin = []
        arr = []
        for i in range(0,n):
            perm.append(i)
            perm_origin.append(i)
        for j in range(0,len(perm)):
            if j % 2 == 0:
                arr.append(perm[j // 2])
            if j % 2 == 1:
                arr.append(perm[n//2 + ((j - 1) // 2)])
        # 把arr赋值给perm
        perm = arr
        # print('原来的值：',perm)
        # print(perm_origin)
        # print('*'*20)

        # 还原步骤
        #临时变量，用来交换值
        tmp = 0   
        # i用来计数
        i = 1
        for n in range(0,len(perm)-1):
            for m in range(0,n):
                if perm[n] < perm[m]:
                    # 当前一个的值大于后边的值的时候，进行交换
                    tmp = perm[n]
                    perm[n] = perm[m]
                    perm[m] = tmp 
                    i += 1
                    # print('交换后的值：',perm[n],perm[m])
                else:
                    pass
        print(i)
        # print(perm)
    else:
        jisuan()
jisuan()


