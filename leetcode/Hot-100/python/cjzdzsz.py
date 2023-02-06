"""
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积
例如：
    输入: [2,3,-2,4]
    输出: 6
    解释: 子数组 [2,3] 有最大乘积 6
    输入: [-2,0,-1]
    输出: 0
    解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxval = nums[0]
        minval = nums[0]
        res = nums[0]
        maxend = 0
        minend = 0

        for i in range(1, len(nums)):
            maxend = maxval * nums[i]
            minend = minval * nums[i]
            # 最大的结果 和 最小的结果 都只能从下面三个结果中选择
            maxval = max(maxend, minend, nums[i])
            minval = min(maxend, minend, nums[i])
            # 取最大的
            res = max(res, maxval)
        
        return res
