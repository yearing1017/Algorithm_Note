"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
时间复杂度为 O(log n) 的算法解决

讲解：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/zai-pai-xu-shu-zu-zhong-cha-zhao-yuan-su-de-di-3-4/
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False) - 1
        # 找到之后检验一下是否符合条件
        if left <= right and right <= len(nums)-1 and nums[left] == target and nums[right] == target:
            return [left, right]
        else:
            return [-1, -1]
    # lower 为true代表找第一个位置
    def binarySearch(self, nums, target, lower):
        l = 0
        r = len(nums) - 1
        # 只有一个数时 [1] 找到第一个大于1的下标为1 再 -1
        ans = len(nums)
        while l <= r:
            mid = (l+r) // 2
            # 找第一个target 即找到第一个>=target的位置 第二个 即找到 >target的位置 再 -1
            if (nums[mid] > target) or (lower and nums[mid] >= target):
                r = mid - 1
                ans = mid 
            else:
                l = mid + 1
        return ans