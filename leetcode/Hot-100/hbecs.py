# -*- coding: utf-8 -*-
'''
已知两颗二叉树，将它们合并成一颗二叉树。合并规则是：都存在的结点，就将结点值加起来，否则空的位置就由另一个树的结点来代替。例如：
两颗二叉树是:
Tree 1  
     1   
    / \   
   3   2 
  /      
 5   
    
Tree 2
   2
  / \
 1   3
  \   \
   4   7

合并后的树为
    3
   / \
  4   5
 / \    \
5  4    7
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees1(self, t1:TreeNode, t2:TreeNode):
        # 将t2合并到t1上
        t1.val = t1.val + t2.val

        if t1.left and t2.left:
            self.mergeTrees(t1.left, t2.left)
        if not t1.left and t2.left:
            t1.left = t2.left
        
        if t1.right and t2.right:
            self.mergeTrees(t1.right, t2.right)
        if not t1.right and t2.right:
            t1.right = t2.right
        return t1
    # 合并到新的树上
    def mergeTrees2(self, t1:TreeNode, t2:TreeNode):
        if not t1: return t2
        if not t2: return t1
        merge_node = TreeNode(t1.val + t2.val)
        merge_node.left = self.mergeTrees2(t1.left, t2.left)
        merge_node.right = self.mergeTrees2(t1.right, t2.right)
        return merge_node
