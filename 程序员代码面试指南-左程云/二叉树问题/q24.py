"""
问题描述：给定一棵完全二叉树的头结点head，返回这棵树的节点个数。

要求：如果完全二叉树的节点数为N，请实现时间复杂度低于O(N)的解法。
"""

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BCTNodeCounter:
    @classmethod
    def get_bct_node_num(cls, head):
        if head == None:
            return 0
        return cls.bs(head, 1, cls.get_most_left_level(head, 1))

    
    # bs函数的返回值表示以node为头节点的完全二叉树的节点是多少
    @classmethod
    def bs(cls, node, l, h):
        # 当前node所在层数 == 树的高度
        if l == h:
            return 1
        #node右子树的最左节点到达最后一层 说明node的整个左子树是完全二叉树
        if cls.get_most_left_level(node.right, l+1) == h:
            return 2**(h-l) + cls.bs(node.right, l+1, h)
        else:
            return 2**(h-l-1) + cls.bs(node.left, l+1, h)
        

    # 由于是完全二叉树，所以左边的层级可以代表整棵树的层级
    @classmethod
    def get_most_left_level(cls, head, start):
        while head is not None:
            start += 1
            head = head.left
        return start - 1

if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.left.right = Node(5)
    head.right.left = Node(6)
    num = BCTNodeCounter.get_bct_node_num(head)
    print(num)