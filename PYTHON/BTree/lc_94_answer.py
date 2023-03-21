# 递归遍历
# 中序遍历
# class BTree(object):
#     def middleOrder(self,root,res):
#         if root == None:
#             return;
#         self.middleOrder(root.left,res)
#         res.append(root.val)
#         self.middleOrder(root.right,res)
#     def middleOrderTreversal(self,root):
#         res = []
#         self.middleOrder(root,res)
#         return res

# root = list(map(int,input('输入列表：').split()))
# tree = BTree(root)

# 二叉树类
class TreeNode(object):
    def __init__(self,val=0,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right

# 列表递归创建二叉树
def createTree(root,list,i):
    if i < len(list):
        if list[i] == 'null':
            


class Tree(object):
    def middleOrderTraversal(self,root:TreeNode):
        def middleOrder(root:TreeNode):
            if not root:
                # 列表不存在，返回空
                return
            # 把列表中的数据添加到res中
            res.append(root.val)
            middleOrder(root.left)
            middleOrder(root.right)
        
        res = []
        middleOrder(root)
        return res

# 前序遍历


