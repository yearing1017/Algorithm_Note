# -*- coding: utf-8 -*-
"""
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
示例：
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""
class Solution1:
    def subsets(self, nums):
        res = []
        n = len(nums)
        def helper(i, temp):
            res.append(temp)
            for j in range(i, n):
                # 每次都是将当前的temp去和他后面的元素组合
                helper(j+1, temp + [nums[j]])
        helper(0, [])
        return res

"""
给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
"""
class Solution:
    def subsetsWithDup(self, nums):
        res = []
        n = len(nums)
        # 不排序会出现[4,1] [1,4]这样的组合
        nums.sort()
        def helper(i, temp):
            if temp not in res:
                res.append(temp)
            for j in range(i, n):
                helper(j+1, temp + [nums[j]])
        helper(0, [])
        return res

if __name__ == "__main__":
    s = Solution1()
    nums = [1,2,3]
    print(s.subsets(nums))