"""
二分查找  数组中的数字有重复
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写
一个函数搜索 nums 中的 target，如果目标值存在返回第一次出现的下标，否则返回 -1。
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                # 向左寻找第一次出现的位置
                while mid != 0 and nums[mid-1] == nums[mid]:
                    mid -= 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1