# 请实现无重复数字的升序数组的二分查找
class Solution:
    def search(self , nums , target ):
        # write code here
        if not nums: return -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1