"""
问题描述：给定彼此独立的两棵树头结点分别为t1和t2，判断t1树是否包含t2树全部的拓扑结构。
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BSTTop:
    @classmethod
    def contains(cls, t1, t2):
        if t2 is None:
            return True
        if t1 is None:
            return False
        # 找t1和t2的一样的头结点
        return cls.check(t1, t2) or cls.contains(t1.left, t2) or cls.contains(t1.right, t2)

    @classmethod
    def check(cls, h, t2):
        if t2 is None:
            return True
        if h is None or h.value != t2.value:
            return False
        # 如果两点的值相等，继续检查左右子树
        return cls.check(h.left, t2.left) and cls.check(h.right, t2.right)

if __name__ == '__main__':
    t1 = Node(1)
    t1.left = Node(2)
    t1.right = Node(3)
    t1.left.left = Node(4)
    t1.left.right = Node(5)
    t1.right.left = Node(6)
    t1.right.right = Node(7)
    t1.left.left.left = Node(8)
    t1.left.left.right = Node(9)
    t1.left.right.left = Node(10)

    t2 = Node(2)
    t2.left = Node(4)
    t2.left.left = Node(8)
    t2.right = Node(5)

    print(BSTTop.contains(t1, t2))
        