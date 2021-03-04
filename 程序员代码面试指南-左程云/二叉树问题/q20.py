"""
问题描述：从二叉树的节点A出发，可以向上或者向下走，但是沿途的节点只能经过一次，当到达节点B时，路径上的节点
数叫做A到B的距离。现给定一棵二叉树的头结点head，求整个二叉树上节点间的最大距离。

要求：如果二叉树的节点数为N，时间复杂度要求为O(N)
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ReturnType:
    def __init__(self, maxDistance, height):
        self.maxDistance = maxDistance
        self.height = height

class MaxDistance:
    @classmethod
    def process(cls, head):
        if head is None:
            return ReturnType(0, 0)
        leftData = cls.process(head.left)
        rightData = cls.process(head.right)
        height = max(leftData.height, rightData.height) + 1
        maxDistance = max(leftData.height + rightData.height + 1, max(leftData.maxDistance, rightData.maxDistance))
        return ReturnType(maxDistance, height)
    
    @classmethod
    def find_max_distance(cls, head):
        return cls.process(head).maxDistance

if __name__ == '__main__':
    head1 = Node(1)
    head1.left = Node(2)
    head1.right = Node(3)
    head1.left.left = Node(4)
    head1.left.right = Node(5)
    head1.right.left = Node(6)
    head1.right.right = Node(7)
    head1.left.left.left = Node(8)
    head1.right.left.right = Node(9)
    print(MaxDistance.find_max_distance(head1))