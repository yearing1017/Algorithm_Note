"""
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。
同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。

给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。

输入：nums = [1,2,3,1]
输出：4
解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
    # 这题和打家劫舍1唯一区别就是首尾只能选一个偷，那么我们可以分为两种情况
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        # 如果不偷第一个，那么问题就变成了在后n-1个里面偷取的最大价值。
        m1 = self.rob1(nums[1:n])
        # 如果不偷最后一个，那么问题就变成了在前n-1个里面偷取的最大价值。
        m2 = self.rob1(nums[0:n-1])

        return max(m1, m2)

    def rob1(self, nums):
        if not nums: return 0
        n = len(nums)

        prepre, pre, now = 0, 0, 0

        for i in range(n):
            now = max(prepre + nums[i], pre)
            prepre = pre
            pre = now

        return now

    