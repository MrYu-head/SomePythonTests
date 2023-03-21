'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 
和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。
'''
# 求nums[i] + nums[j] = target的i和j
nums = [2,7,11,15]
target = int(input('输入target:'))
# for k,v in enumerate(nums):
#     print('下标：',k,',值：',v)

# 循环遍历v
for i in range(0,len(nums)):
    for j in range(0,i-1):
        if (i != j) and (nums[i] + nums[j] == target):
            print('两个值为：',nums[i],nums[j])
            # print('两个值的下标为：',i,j)
    else:
        print('没有找到。')


