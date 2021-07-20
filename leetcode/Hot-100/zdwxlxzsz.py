"""
给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
请你找出符合题意的 最短 子数组，并输出它的长度。
输入：nums = [2,6,4,8,10,9,15]
输出：5
解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序
要求：设计一个时间复杂度为 O(n) 的解决方案
若没时间复杂度限制  则可以使用最简单的先排序 再对比两段不一样的元素 得到长度  时间复杂度 O(nlog(n)) 空间复杂度 O(n)
"""
class Solution:
    def findUnsortedSubarray1(self, nums: List[int]) -> int:
        n = len(nums)
        # 从左到右 遍历一遍 找到需要调整的右边界
        right = 0
        max_num = nums[0]
        for i in range(n):
            # 递增说明 不需要调整
            if nums[i] >= max_num:
                max_num = nums[i]
            # 一旦遇到递减的 保存下标 最终保存的是最后一个递减的下标
            else:
                right = i
        # 从右到左 遍历一遍 找到需要调整的左边界
        left = n  # 这个地方若为n-1的话  一个元素会返回1的长度  题意要求返回0
        min_num = nums[n-1]
        for i in range(n-1, -1, -1):
            if nums[i] <= min_num:
                min_num = nums[i]
            # 一旦遇到递增的 保存下标 最终保存的是最后一个递增的下标
            else:
                left = i
        
        # 最终返回 右边界-左边界+1
        return right-left+1 if (right-left+1 > 0) else 0

    def findUnsortedSubarray2(self, nums: List[int]) -> int:
        nums_copy=nums[:]
        nums_copy.sort()
        left=float("inf")
        right=0
        for i in range(len(nums)):
            if(nums_copy[i]!=nums[i]):
                left=min(left,i)
                right=max(right,i)
        return right-left+1 if(right-left+1 > 0) else 0
