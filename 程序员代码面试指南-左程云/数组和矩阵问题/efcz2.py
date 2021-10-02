'''
请实现有重复数字的升序数组的二分查找
给定一个 元素有序的（升序）整型数组 nums 和一个目标值 target，写一个函数搜索 nums 中的第一个出现的target
如果目标值存在返回下标，否则返回 -1

输入：[1,2,4,4,5],4
输出：2
'''
class Solution:
    def search(self , nums , target ):
        # write code here
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low+(high-low)//2
            if nums[mid] == target:
                while mid!=0 and (nums[mid-1] == nums[mid]):
                    mid -= 1
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def search2(self, nums, target):
        if not nums: return -1
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low+(high-low)//2
            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
        return low if nums[low] == target else -1