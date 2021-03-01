"""
问题描述：平衡二叉树的性质是：要么是一棵空树，要么任何一个节点的左右子树的高度差
的绝对值不超过1。现在给定一棵二叉树的头结点head，请判断它是否是一棵平衡二叉树。
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 递归求二叉树的深度
class TreeHeight:
    @classmethod
    def get_height(cls, root):
        if not root:
            return 0
        return max(get_height(root.left), get_height(root.right)) + 1

# 判断二叉树是否为平衡二叉树
class BlanceTreeTool:
    @classmethod
    def recur(cls, root):
        if not root:
            return 0
        left_h = cls.recur(root.left)
        if left_h == -1: return -1
        right_h = cls.recur(root.right)
        if right_h == -1: return -1
        # 若该节点左右子树深度差小于等于1，则返回高度，否则返回-1：代表不平衡
        if abs(left_h - right_h) <= 1:
            return max(left_h, right_h) + 1
        else: return -1

    @classmethod
    def is_blanced_tree(cls, root):
        return cls.recur(root) != -1
# 判断平衡二叉树的方法2：时间复杂度高于方法1
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and 
            self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root: return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1

if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.left.right = Node(5)
    head.right.left = Node(6)
    head.right.right = Node(7)

    print(BlanceTreeTool.is_blanced_tree(head))