'''
给定一个仅包含数字0−9的二叉树，每一条从根节点到叶子节点的路径都可以用一个数字表示。
例如根节点到叶子节点的一条路径是1→2→3,那么这条路径就用123来代替。
找出根节点到叶子节点的所有路径表示的数字之和
这颗二叉树一共有两条路径，
根节点到叶子节点的路径 1→2 用数字 12 代替
根节点到叶子节点的路径 1→3 用数字 13 代替
所以答案为 12+13=25 
'''
class Solution:
    def sumNumbers(self , root ):
        if not root:
            return 0
        res = 0
        return self.preorder(root, res)

    def preorder(self, root, res):
        if not root:
            return 0
        res = 10*res + root.val
        if not root.left and not root.right:
            return res
        return self.preorder(root.left, res) + self.preorder(root.right, res)