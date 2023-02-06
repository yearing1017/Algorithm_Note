"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
例如：
    输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
    输出：6
    解释：连续子数组 [4,-1,2,1] 的和最大，为 6 
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val = nums[0]
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            max_val = max(max_val, temp)
            if temp < 0:
                temp = 0 
        return max_val