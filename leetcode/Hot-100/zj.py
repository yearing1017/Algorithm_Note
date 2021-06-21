# -*- coding: utf-8 -*-
"""
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
示例：
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""
class Solution:
    def subsets(self, nums):
        res = []
        n = len(nums)
        def helper(i, temp):
            for j in range(i, n):
                res.append(temp)
                # 每次都是将当前的temp去和他后面的元素组合
                helper(j+1, temp + [nums[j]])
        helper(0, [])
        return res
