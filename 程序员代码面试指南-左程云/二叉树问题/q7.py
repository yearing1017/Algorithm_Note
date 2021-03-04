"""
问题描述：给定一棵二叉树的头结点head,已知其中所有节点的值都不一样，找出含有节点
最多的搜索二叉树，并返回这棵子树的头结点。

要求：如果节点数为N，要求时间复杂度为O(N)，额外空间复杂度为O(h)，h为二叉树的高度。
"""
import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ReturnType:
    def __init__(self, maxBSTHead, maxBSTSize, minValue, maxValue):
        self.maxBSTHead = maxBSTHead
        self.maxBSTSize = maxBSTSize
        self.minValue = minValue
        self.maxValue = maxValue

class findBigBST:
    @classmethod
    def process(cls, head):
        if not head:
            return ReturnType(None, 0, sys.maxsize, -sys.maxsize - 1)
        lData = cls.process(head.left)
        rData = cls.process(head.right)

        minValue = min(head.value, min(lData.minValue, rData.minValue))
        maxValue = max(head.value, max(lData.maxValue, rData.maxValue))

        maxBSTSize = max(lData.maxBSTSize, rData.maxBSTSize)

        maxBSTHead = lData.maxBSTHead if lData.maxBSTSize > rData.maxBSTSize else rData.maxBSTHead

        if lData.maxBSTHead == head.left and rData.maxBSTHead == head.right and head.value > lData.maxValue and head.value < rData.minValue:
            maxBSTSize = lData.maxBSTSize + rData.maxBSTSize + 1
            maxBSTHead = head

        return ReturnType(maxBSTHead, maxBSTSize, minValue, maxValue)

if __name__ == '__main__':
    head = Node(6)
    head.left = Node(1)
    head.left.left = Node(0)
    head.left.right = Node(3)
    head.right = Node(12)
    head.right.left = Node(10)
    head.right.left.left = Node(4)
    head.right.left.left.left = Node(2)
    head.right.left.left.right = Node(5)
    head.right.left.right = Node(14)
    head.right.left.right.left = Node(11)
    head.right.left.right.right = Node(15)
    head.right.right = Node(13)
    head.right.right.left = Node(20)
    head.right.right.right = Node(16)
    res = findBigBST.process(head).maxBSTHead
    print(res.value)


