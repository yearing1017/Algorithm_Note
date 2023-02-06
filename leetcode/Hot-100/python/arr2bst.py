"""
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。
高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。
注意：平衡二叉搜索树首先需要满足完全二叉树
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self , num ):
        # write code here
        def preOrder(arr, left, right):
            if left > right:
                return
            # leetcode 这两种都行 牛客只能上面
            # 这样取mid 例如 012345 5//2 取到2 左子树少 右子树多 
            #mid = (left + right)//2
            # 这样取mid 例如 012345 取到3 左子树多 右子树少
            mid = left + (right-left+1)//2
            root = TreeNode(arr[mid])
            root.left = preOrder(arr, left, mid-1)
            root.right = preOrder(arr, mid+1, right)
            return root
        if len(num) < 1:
            return 
        root = preOrder(num, 0, len(num)-1)
        return root