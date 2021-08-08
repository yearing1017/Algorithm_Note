"""
给定一个二叉树和一个值 sum，判断是否有从根节点到叶子节点的节点值之和等于 sum 的路径
"""

class Solution:
    def hasPathSum(self , root , sum ):
        def recur(node, target):
            if not node: return False
            
            target -= node.val
            if target == 0 and not node.left and not node.right:
                return True
            return recur(node.left, target) or recur(node.right, target)
        
        return recur(root, sum)