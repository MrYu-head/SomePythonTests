# 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。


class BTree(object):
    def __init__(self,data = None,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right

    # 中序遍历  先中序左子树，再访问根节点，再中序右子树
    # 前提：已知根节点存在
    def middleOrder(self):
        if self.left is not None:
            self.left.middleOrder()
        elif self.left is None:
            self.left = -1
        elif self.data is not None:
            print(self.data,end=' ')
        elif self.right is not None:
            self.right.middleOrder()
        elif self.right is None:
            self.right = -1
        elif self.left is None and self.right is None:
            # 左右子树都为空，则只存在根节点  直接输出
            print(self.data,end=' ') 
        else:
            # 左右子树都不为空，则分别进行中序遍历s
            self.left.middleOrder()
            self.right.middleOrder()

# 从键盘输入节点数据构造
root = list(map(int,input('输入节点：').split()))
print('输入的节点数据如下：',root)

# [6, 12, 23, 2, 1, 20, 14]
# 构造子树及其分支节点
# 方法1：先遍历列表，比根节点小的放在左子树，比根节点大的放在右子树
# [6, 12, 23, 2, 1, 20, 14]
# left_list = [2,1]
# right_list = [12,23,20,14]
left_list = []
right_list = []
for i in root[1:len(root)+1]:
    if i < root[0]:
        left_list.append(i)
    elif i > root[0]:
        right_list.append(i)
    else:
        # 如果有和根节点相同的数，则排除掉
        root.remove(i)
print('左子树节点列表：',left_list)
print('右子树节点列表：',right_list)


left_tree = BTree(left_list[0])
# 对左子树进行遍历，小的放左，大的放右
# [2,4,5,1,3]
if len(left_list) <= 1:
    # 只存在根节点或不存在根节点
    left_tree = BTree(left_list[0])
else:
    for left_i in range(0,len(left_list)-1):
        if left_list[left_i+1] == left_list[left_i]:
            left_list.remove(left_list[left_i+1])
        elif left_list[left_i+1] < left_list[left_i]:
            left_tree.left = left_list[left_i+1]
        elif left_list[left_i+1] > left_list[left_i]:
            left_tree.right = left_list[left_i+1]
        else:
            # 如果只有一个节点，则左子树就是一个
            left_tree = BTree(left_list[0])

        # left_tree.middleOrder()
print('遍历后的左子树列表：',left_list)

right_tree = BTree(right_list[0])
# 对右子树进行遍历，小的放左，大的放右
if len(right_list) <= 1:
    # 只存在根节点或不存在根节点
    right_tree = BTree(right_list[0])
else:
    for right_i in range(0,len(right_list)-1):
        if right_list[right_i+1] == right_list[right_i]:
            right_list.remove(right_list[right_i+1])
        elif right_list[right_i+1] < right_list[right_i]:
            right_tree.left = right_list[right_i+1]
        elif right_list[right_i+1] > right_list[right_i]:
            right_tree.right = right_list[right_i+1]
        else:
            right_tree = BTree(right_list[0])
        # right_tree.middleOrder()
print('遍历后的右子树列表：',right_list)


# 根节点：
tree = BTree(root[0])
# 左子树：
tree.left = left_tree
# 右子树：
tree.right = right_tree
print('中序遍历结果为：')
tree.middleOrder()













            

        
