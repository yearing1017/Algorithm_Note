""" 操作给定的二叉树，将其变换为源二叉树的镜像。
比如：    源二叉树 
            8
           /  \
          6   10
         / \  / \
        5  7 9 11
        镜像二叉树
            8
           /  \
          10   6
         / \  / \
        11 9 7  5 """

class Solution:
    def Mirror(self, pRoot):
        if not pRoot:
            return
        stack = []
        stack.append(pRoot)
        while stack:
            cur = stack.pop()
            if cur.left: stack.append(cur.left)
            if cur.right: stack.append(cur.right)
            cur.left, cur.right = cur.right, cur.left
        return cur 