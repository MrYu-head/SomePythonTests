'''
二叉树
  根节点
  左子树
  右子树
  左子节点
  右子节点

  深度--即二叉树的层数
  遍历二叉树：先序遍历、中序遍历、后序遍历


[ 9 16 13 10 17 6 14 4 9 15 10 4 15 9 7]


'''

# 构建二叉树
class BTree(object):
    def __init__(self,data = None,left = None,right= None):
        self.data = data  #根节点
        self.left = left  #左子树
        self.right = right  #右子树

    # 前序遍历：先访问根节点，然后前序遍历左子树，再前序遍历右子树``````````
    # 18 7 3 4 11 5 1 3 6 2 4
    def preOrder(self):
        if self.data is not None:
            print(self.data,end=' ')
        if self.left is not None:
            # 对左子树进行前序遍历，递归
            self.left.preOrder()
        if self.right is not None:
            # 对右子树进行前序遍历，递归
            self.right.preOrder()
    # # 前序遍历
    # def qianxu(self):
    #     if self.data is not None:
    #         print(self.data,end=' ')
    #     if self.left is not None:
    #         self.left.qianxu()
    #     if self.right is not None:
    #         self.right.qianxu()

    # 中序遍历：先中序遍历根节点的左子树，再访问根节点，最后访问右子树
    # 3 7 4 18 1 5 3 11 2 6 4
    def middleOrder(self):
        if self.left is not None:
            # 中序遍历左子树
            self.left.middleOrder()
        if self.data is not None:
            print(self.data,end=' ')
        if self.right is not None:
            # 中序遍历右子树
            self.right.middleOrder()

    # 后序遍历：从左到右的顺序，先叶子后节点的方式遍历左子树，然后是右子树，最后是根节点
    # 3 4 7 1 3 5 2 4 6 11 18
    def postOrder(self):
        if self.left is not None:
            # 后序遍历左子树
            self.left.postOrder()
        if self.right is not None:
            # 后序遍历右子树
            self.right.postOrder()
        if self.data is not None:
            print(self.data,end=' ')
        
    # 层次遍历：从根节点开始从上往下逐层遍历，同一层按照从左到右的顺序逐个访问节点
    # 18 7 11 3 4 5 6 1 3 2 4
    def levelOrder(self):
        # 返回某个节点的左孩子
        def lchild_of_node(node):
            # 如果节点存在左孩子，则赋值，如果不存在，则为空
            return node.left if node.left is not None else None
        
        # 返回某个节点的右孩子
        def rchild_of_node(node):
            # 如果节点存在右孩子，则赋值，如果不存在，则为空
            return node.right if node.right is not None else None
        
        # 层序遍历列表
        level_order = []
        # 是否添加根节点中的顺序
        if self.data is not None:
            level_order.append([self])
        
        # 二叉树的高度(深度)
        height = self.height()
        if height >= 1:
            # 存在根节点或者度大于1.即存在子树
            # 对第二层及其以后的层数进行操作，再level_order中添加节点而不是数据
            for i in range(2,height + 1):  #第二层往后
                level = []  #当前层的节点列表,包含当前层的左节点和右节点
                for node in level_order[-1]:
                    # 让节点从最后一层开始遍历
                    if lchild_of_node(node):  

                        #如果存在左孩子,就把它添加到左子树中
                        level.append(lchild_of_node(node))
                    if rchild_of_node(node):
                        # 如果存在右孩子，就把它添加到右子树中
                        level.append(rchild_of_node(node))
                # 如果当前层为空，则添加该层,每一层的左子树和右子树分别是一个列表
                if level:
                    level_order.append(level)
            
            # 取出每层中的数据
            for i in range(0,height):
                for index in range(len(level_order[i])):
                    # 分别添加到每层对应的位置
                    level_order[i][index] = level_order[i][index].data
        # 返回每一层的节点列表
        return level_order
 
    # 树的高度，即深度
    def height(self):
        # 空树高度为0
        if self.data is None:
            return 0
        elif self.left is None and self.right is not None:
            # 左子树为空，右子树存在，则高度为右子树的高度+1
            return 1 + self.right.height()
        elif self.left is not None and self.right is None:
            # 左子树存在，右子树不存在，则高度为左子树的高度+1
            return 1 + self.left.height()
        elif self.left is None and self.right is None:
            # 左右子树都不存在，则高度为1，即只存在根节点
            return 1
        else:
            # 左右子树都存在的前提下，哪边的深度最深，高度就是当前深度+1
            return 1 + max(self.left.height(),self.right.height())

    # 叶子节点
    def leaves(self):
        if self.data is None:
            # 如果根节点为空，则不存在叶子节点，也不存在树
            return 0
        elif self.left is None and self.right is None:
            # 左右子树都为空，则根节点就是叶子节点
            # return self.data
            print(self.data,end=' ')
        elif self.left is not None and self.right is None:
            # 左子树不为空，右子树为空，则叶子节点只存在于左子树
            # 递归遍历左子树
            self.left.leaves()
        elif self.left is None and self.right is not None:
            # 右子树不为空，左子树为空，则叶子节点只存在于右子树
            # 递归遍历右子树
            self.right.leaves()
        else:
            # 左右子树都不为空，则叶子节点为全部
            self.left.leaves()
            self.right.leaves()



# 实例化对象，生成一个随机二叉树进行验证
# 深度优先遍历，从深度最大的层开始往上遍历
# 最后一层左子树 [5,[1,3]]
left_tree = BTree(5)
left_tree.left = BTree(1)
left_tree.right = BTree(3)
# 最后一层右子树[6,[2,4]]
right_tree = BTree(6)
right_tree.left = BTree(2)
right_tree.right = BTree(4)
# 从下往上第一个完全二叉树，倒数第二层  [11,[5,[1,3]],[6,[2,4]]]
tree = BTree(11) 
tree.left = left_tree
tree.right = right_tree
# 倒数第二层对应层数的左子树   [7,[3,4]]
left_tree = BTree(7)
left_tree.left = BTree(3)
left_tree.right = BTree(4)
# 左子树和右子树组合成为完全二叉树，找出父节点
right_tree = tree   #[11,[5,[1,3]],[6,[2,4]]]
tree = BTree(18)
tree.left = left_tree  #[7,[3,4]]
tree.right = right_tree  #[11,[5,[1,3]],[6,[2,4]]]


# 分别执行
print('先序遍历结果为：')
tree.preOrder()
print()

print('中序遍历结果为：')
tree.middleOrder()
print()

print('后序遍历结果为：')
tree.postOrder()
print()

print('层次遍历结果为：')
levelOrder = tree.levelOrder()
print(levelOrder)
print()

height = tree.height()
print('树的深度为：%s'%height)
print()

print('树的叶子节点分别是：')
tree.leaves()



