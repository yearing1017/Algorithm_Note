"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
时间复杂度为 O(log n) 的算法解决

讲解：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/zai-pai-xu-shu-zu-zhong-cha-zhao-yuan-su-de-di-3-4/
"""
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        left = self.bi_left(nums, target)
        right = self.bi_right(nums, target)

        if not 0 <= left < len(nums) or not 0 <= right < len(nums):
            return [-1, -1]
        elif nums[left] != target or nums[right] != target:
            return [-1, -1]
        else:
            return[left, right]

    def bi_left(self, nums, target):
        # 5,7,7,8,8,10     8
        i = 0
        j = len(nums)-1
        while i <= j:
            m = (i+j)//2
            if nums[m] < target:
                i = m + 1
            else:
                j = m - 1
        return i
    
    def bi_right(self, nums, target):
        # 5,7,7,8,8,10     8
        i = 0
        j = len(nums)-1
        while i <= j:
            m = (i+j)//2
            if nums[m] <= target:
                i = m + 1
            else:
                j = m - 1
        return j