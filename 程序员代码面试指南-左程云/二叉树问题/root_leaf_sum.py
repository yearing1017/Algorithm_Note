# 给定一个二叉树和一个值 sum，请找出所有的根节点到叶子节点的节点值之和等于 sum 的路径

class Solution:
    def pathSum(self , root , sum ):
        res = []
        path = []

        def recur(root, sum):
            if not root: return

            path.append(root.val)
            sum -= root.val
            # 题目要求叶子节点
            if sum == 0 and not root.left and not root.right:
                res.append(list(path))
            recur(root.left, sum)
            recur(root.right, sum)
            # 回溯
            path.pop()
        
        recur(root, sum)
        return res