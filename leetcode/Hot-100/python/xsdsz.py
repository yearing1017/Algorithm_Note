"""
给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果
例如：
    输入：nums = [4,3,2,7,8,2,3,1]
    输出：[5,6]
"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 数组中 都是 1-N的 数字 对下标做标记 
        for num in nums:
            # 判断0-N-1 这些下标那些出现过 负的代表这些下标出现过
            if nums[abs(num)-1] > 0:
                nums[abs(num)-1] *= -1
        # 存放未出现的结果下标
        res = []
        for i in range(len(nums)):
            # 做完标记之后 正的表示该下标的代表的数字没出现
            if nums[i] > 0:
                res.append(i+1)
        return res
