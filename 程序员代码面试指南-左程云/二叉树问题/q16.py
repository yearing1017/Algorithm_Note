"""
问题描述：给定一个有序数组sortArr,已知其中没有重复值，用这个有序数组生成一棵平衡二叉搜索树，并且该搜索二叉树
中序遍历结果与sortArr一致。
"""

from q3 import PrintTree


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ReconstructBalancedBST:
    @classmethod
    def reconstruct(cls, arr):
        if not arr or len(arr) == 0:
            return None
        return cls.reconstruct_detail(arr, 0, len(arr)-1)

    @classmethod
    def reconstruct_detail(cls, arr, start, end):
        if start > end:
            return None
        #搜索二叉树中序遍历结果的中间结点 是根节点
        pos = (start + end)//2
        head = Node(arr[pos])

        head.left = cls.reconstruct_detail(arr, start, pos-1)
        head.right = cls.reconstruct_detail(arr, pos+1, end)

        return head

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    PrintTree.print_tree(ReconstructBalancedBST.reconstruct(arr))
