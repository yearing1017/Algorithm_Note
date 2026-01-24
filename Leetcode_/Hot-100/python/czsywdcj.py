"""
给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
输入: [1,2,3,4]
输出: [24,12,8,6]
请不要使用除法，且在 O(n) 时间复杂度内完成此题 常数空间复杂度
解法：https://leetcode-cn.com/problems/product-of-array-except-self/solution/product-of-array-except-self-shang-san-jiao-xia-sa/
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        p = 1
        q = 1
        # 不乘以最后一个数  下三角
        for i in range(len(nums) - 1):
            p *= nums[i]
            res.append(p)
        # 不乘第一个数   上三角
        for j in range(len(nums)-1, 0, -1):
            q *= nums[j]
            res[j-1] *= q
        return res
