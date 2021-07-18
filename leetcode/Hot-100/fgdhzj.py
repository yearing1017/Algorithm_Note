"""
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
例如：
    输入：nums = [1,5,11,5]
    输出：true
    解释：数组可以分割成 [1, 5, 5] 和 [11]
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 问题转化为：能否在数组中找到若干数的和 等于 总和的一半
        m = len(nums)
        total = sum(nums)
        # 如果总和不是偶数 可以直接返回fasle
        if total % 2 != 0: return False
        target = total // 2
        # 如果最大值已经大于target了  那么无论如何划分 两边都会有一边存在该值  导致大于target 直接返回fasle
        max_num = max(nums)
        if max_num > target:
            return False

        # dp[i][j] 表示是否可在nums[0...i]中 找到若干数(可以是0个) 其和 等于 j
        # m行表示m个数 target+1列 表示从和 等于 0 开始
        dp = [[False for _ in range(target+1)] for _ in range(m)]

        # 边界1：第一列的初始化  nums[0...i]中是否存在 若干数 和 等于 0 存在  不选择任何数 和 就等于0
        for i in range(m):
            dp[i][0] = True
        # 边界2：第一行第二列  当i==0时 只有一个正整数 nums[0]可以选取 所以该位置为true
        dp[0][nums[0]] = True

        # 其他位置dp的判断
        for i in range(1, m):
            for j in range(1, target+1):
                # j >= nums[i] 时 考虑不选取当前nums[i] 和 选取当前nums[i]
                if j >= nums[i]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
                # j < nums[i] 时 只能考虑不选取当前nums[i]
                else:
                    dp[i][j] = dp[i-1][j]
        
        # 最终返回 在nums[0...m-1]中 找到若干数(可以是0个) 其和 等于 target
        return dp[m-1][target]
