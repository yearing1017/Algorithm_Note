"""
给定一个二叉树，检查它是否是镜像对称的。
例如：
    1
   / \
  2   2
 / \ / \
3  4 4  3
"""
class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        return self.dfs(root.left, root.right)    
    def dfs(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val) and self.dfs(left.left, right.right) and self.dfs(left.right, right.left)