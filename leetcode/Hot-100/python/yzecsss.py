"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。
假设一个二叉搜索树具有如下特征：
    节点的左子树只包含小于当前节点的数
    节点的右子树只包含大于当前节点的数
    所有左子树和右子树自身必须也是二叉搜索树
例如：
    输入:
     2
    / \
   1   3
    输出: true
"""
# class TreeNode:
def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        cur  = root
        stack = []
        pre = float('-inf')
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                node = stack.pop()
                if node.val <= pre:
                    return False
                pre = node.val
                cur = node.right
        return True
