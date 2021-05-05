'''
给定一棵二叉树，判断其是否是自身的镜像（即：是否对称）
例如：下面这棵二叉树是对称的
1
/  \
2    2
/ \    / \
3 4  4  3
下面这棵二叉树不对称。
1
/ \
2   2
\    \
3    3
'''
class Solution:
    def isSymmetric(self , root ):
        if not root:
            return True
        return self.recur(root.left, root.right)
    
    def recur(self, L, R):
        if not L or not R:
            return True
        elif not L or not R or L.val != R.val:
            return False
        else:
            return self.recur(L.left, R.right) and self.recur(L.right, R.left)