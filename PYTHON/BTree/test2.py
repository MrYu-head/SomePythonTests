'''
二叉树也可以用数组来存储，给定一个数组，
树的根节点的值储存在下标1，对于储存在下标n的节点，
他的左子节点和右子节点分别储存在下标2n和2n+1，====>相当于每一个节点都是一个完全二叉树
并且我们用-1代表一人节点为空，给定一个数组存储的二叉树， ====>完全二叉树子节点不存在，用-1代替
试求从根节点到最小的叶子节点的路径，路径由节点的值组成。

'''



# tree = [14, 11, 5, 9, 7, 13, 1, 4, 17]
# #  下标：0   1   2  3  4  5   6  7  8  
# 根节点：11
class Tree:
    def __init__(self,data = None,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right
    # 前序遍历
    def prechorder(self):
        # 1.需要从第一个下标开始遍历，每一个值都要走一次完全二叉树方法
        for n in range(0,len(tree)):
            if n < 2:
                print("根节点不存在。")
            else:
                # 根节点存在 下标为1
                self.data = tree[1]
                if self.left is not None:
                    # 如果左子节点存在，则递归平衡二叉树
                    return self.left.balanceTree(n)
                if self.right is not None:
                    # 如果右子节点存在，则递归平衡二叉树
                    return self.right.balanceTree(n)


    # 每一个节点都是完全二叉树，节点不存在用-1代替==>None = -1
    def balanceTree(self,n):
        # 如果子节点的左子节点存在，则赋值，不存在的话，赋值为-1
        if self.left is not None:
            self.left = tree.left
            # 向新列表执行下标添加节点
            newtree.insert(2*n,self.left)
        else:
            # self.left = -1
            newtree.insert(2*n+1,-1)
        if self.right is not None:
            self.right = tree.right
            newtree.insert(2*n,self.right)
        else:
            # self.right = -1
            newtree.insert(2*n+1,-1)
        print("这是newtree------------------")
        print(newtree)

t = Tree()
# 声明数组和新数组:
tree = [14, 11, 5, 9, 7, 13, 1, 4, 17]
newtree = []

t.prechorder()







# n = len(tree) - 1

# tree = [14, 11, 5, 9, 7, 13,  1,  4,  17]
#  下标：  0   1   2  3  4  5   6    7   8

# Wnewtree = [-1   11  5  14 1   9   7   -1  -1  -1  -1  -1    -1   4    -1    -1]
# 下标：0    1   2  3  4   5   6   7   8   9   10   11   12   13   14   15   16   17  18

# tree = [14, 11, 5, 9, 7, 13, 1, 4, 17]
# newtree = [-1, 11, 5, 14, 1, 9, 7, -1, -1, -1, -1, -1, -1, 4, -1, -1]








# n>1

# import random
# tree = []
# for i in range(1,12):
#     node = random.randint(1,20)
#     tree.append(node)
# print(tree)