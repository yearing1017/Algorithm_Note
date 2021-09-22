# https://leetcode-cn.com/problems/house-robber-iii/solution/san-chong-fang-fa-jie-jue-shu-xing-dong-tai-gui-hu/
'''
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 
除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 
如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

输出: 7 
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
'''
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root) -> int:
        res = self.rob3(root)
        return max(res[0], res[1])

    def rob3(self, root):
        res = [0] * 2
        # 终止条件
        if not root:
            return res
        # res[0]表示不偷当前结点时偷到的最大的金额  res[1]表示偷当前结点偷到的最大的金额
        leftarr  = self.rob3(root.left)
        rightarr = self.rob3(root.right)

        # 当前结点不偷时，最大价值就是左儿子偷或不偷的最大价值，加上右儿子偷或不偷的最大价值
        res[0] = max(leftarr[0], leftarr[1]) + max(rightarr[0], rightarr[1])
        # 偷了当前结点值时，它的左右儿子就不能偷了，所以最大价值就是左儿子不偷的最大价值，加上右儿子不偷的最大价值，再加上 r 的价值
        res[1] = leftarr[0] + rightarr[0] + root.val

        return res