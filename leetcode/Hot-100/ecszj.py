"""
给定一棵二叉树，你需要计算它的直径长度。
一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
注意题目里的：任意两个结点；可能不穿过根节点；
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 求任意节点 为根时 直径长度的最大值（即 左右子树的深度相加）
        def depth(node):
            nonlocal res
            # 递归结束
            if not node: return 0
            # 左子树深度
            L = depth(root.left)
            # 右子树深度
            R = depth(root.right)
            # 更新当前结点为根节点的最大直径长度
            res = max(res, L+R+1)
            # 返回当前树的深度
            return max(L,R) + 1
        res = 1
