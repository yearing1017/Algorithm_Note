'''
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度
子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列
例如：
    输入：nums = [10,9,2,5,3,7,101,18]
    输出：4
    解释：最长递增子序列是 [2,3,7,101]，因此长度为 4
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] 代表 以arr[i]结尾时，arr[0...i]中的最大递增子序列长度
        dp = [1 for _ in range(len(nums))]
        res = 0
        for i in range(len(nums)):
            for j in range(i):
                # 遍历i之前的数字 更新dp
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
            res = max(dp[i], res)
        return res