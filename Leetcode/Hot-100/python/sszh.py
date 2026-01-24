"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。
例如：
    输入：nums = [-1,0,1,2,-1,-4]
    输出：[[-1,-1,2],[-1,0,1]]
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        length = len(nums)
        if not nums or length < 3:
            return res
        # 先排序  遇到正数即可停止
        nums.sort()
        for i in range(length):
            # 先定住第一个数
            if nums[i] > 0:
                break
            # 去重
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 定住第一个数的同时  从右边开始两边向中间缩
            L = i + 1
            R = length - 1
            while L < R:
                ans = nums[i] + nums[L] + nums[R]
                if ans == 0:
                    res.append(list(nums[i], nums[L], nums[R]))
                    # 去重
                    while L < R and nums[L] == nums[L+1]: L += 1
                    while L < R and nums[R] == nums[R-1]: R -= 1
                    L += 1
                    R -= 1
                elif ans < 0:
                    L += 1
                else:
                    R -= 1
            return res

