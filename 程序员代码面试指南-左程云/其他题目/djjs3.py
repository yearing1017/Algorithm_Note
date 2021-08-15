# https://leetcode-cn.com/problems/house-robber-iii/solution/san-chong-fang-fa-jie-jue-shu-xing-dong-tai-gui-hu/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
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