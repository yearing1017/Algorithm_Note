"""
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素
你可以假设数组是非空的，并且给定的数组总是存在多数元素
例如：
    输入：[2,2,1,1,1,2,2]
    输出：2 
解法：
    将数组排序，返回排序后的nums[n // 2],无论是排序前后，这个位置肯定是大于n/2的元素
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        return nums[n // 2]