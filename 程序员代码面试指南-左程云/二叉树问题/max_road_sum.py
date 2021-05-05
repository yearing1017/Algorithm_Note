'''
给定一个二叉树，请计算节点值之和最大的路径的节点值之和是多少。
这个路径的开始节点和结束节点可以是二叉树中的任意节点
例如：
给出以下的二叉树，
(1,2,3) 1的左孩子2  右孩子3
返回的结果为6
'''
class Solution:
    def __init__(self):
        self.maxSum = float("-inf")
    def maxPathSum(self , root ):
        self.maxGain(root)
        return self.maxSum

    #  递归计算左右子节点的最大贡献值
    def maxGain(self, node):
        if not node:
            return 0
        
        # 只有在最大贡献值大于 0 时，才会选取对应子节点
        leftGain = max(self.maxGain(node.left), 0)
        rightGain = max(self.maxGain(node.right), 0)

        new_maxsum = node.val + leftGain + rightGain

        self.maxSum = max(self.maxSum, new_maxsum)
        # 题意要求满足是树的路径和，因为这里是dfs的遍历方式，向上找最大路径和，所以只能取一边的值，满足路径的含义
        return node.val + max(leftGain, rightGain)
