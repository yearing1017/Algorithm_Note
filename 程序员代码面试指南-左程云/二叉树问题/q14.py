"""
问题描述：给定一个整型数组arr，已知其中没有重复值，判断arr是否可能是节点值类型为整型的搜索二叉树后序遍历的结果。

进阶：如果整型数组arr中没有重复值，且已知是一棵搜索二叉树的后续遍历结果，通过数组arr重构二叉树。
"""

from q3 import PrintTree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ISBST:
    @classmethod
    def is_bst_tree(cls, arr):
        if not arr or len(arr) == 0:
            return False
        return cls.is_bst_tree_detail(arr, 0, len(arr)-1)
    
    @classmethod
    def is_bst_tree_detail(cls, arr, start, end):
        # 遍历完函数没结束，说明是搜索二叉树
        if start == end:
            return True
        # 代表比根节点小的左半部分结束索引位置
        less = -1
        # 代表比根节点大的右半部分开始索引位置
        more = end
        # 遍历找到less和more的索引位置
        for i in range(start, end):
            if arr[end] > arr[i]:
                less = i
            else:
                more = i if more == end else more
        # 此情况说明根节点左边全为小于根节点或大于根节点的值，在左或右
        if less == -1 or more == end:
            return cls.is_bst_tree_detail(arr, start, end-1)
        # 若不符合上述情况，则根节点左边有大有小，则须判断less和more的位置是否相邻
        if less != more-1:
            return False
        return cls.is_bst_tree_detail(arr,start,less) and cls.is_bst_tree_detail(arr,more,end-1)
        

    # 进阶问题
    @classmethod
    def recontruct_bst(cls, arr):
        if arr is None:
            return None
        return cls.recontruct_bst_detail(arr, 0, len(arr) - 1)

    @classmethod
    def recontruct_bst_detail(cls, arr, start, end):
        if start > end:
            return None

        less = -1
        more = end
        #建立头结点 后序遍历结果的最后一个点为头结点
        cur_node = Node(arr[end])

        for i in range(start, end):
            if arr[i] < arr[end]:
                less = i
            else:
                more = i if more == end else more
        # 递归建立左右子树
        cur_node.left = cls.recontruct_bst_detail(arr, start, less)
        cur_node.right = cls.recontruct_bst_detail(arr, more, end-1)
        return cur_node

if __name__ == '__main__':
    my_arr = [2, 1, 3, 6, 5, 7, 4]
    print(ISBST.is_bst_tree(my_arr))
    from q1 import RecursiveVisit
    RecursiveVisit.visit_in_last_order(ISBST.recontruct_bst(my_arr))
    PrintTree.print_tree(ISBST.recontruct_bst(my_arr))