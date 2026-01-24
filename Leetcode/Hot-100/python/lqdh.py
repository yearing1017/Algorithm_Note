"""
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
你可以认为每种硬币的数量是无限的
例如：
    （1，2，3） 6  ===>  3枚
"""
class Solution:
    def coinChange(self, coins, amount) -> int:
        # dp[i] 表示组成金额i 所需最少的硬币数
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        # dp(i) = min(dp(i-cj)) + 1; cj代表枚举的最后一枚硬币的金额 需要从这个状态转移归来  在加上这枚硬币的1
        # 依次遍历加上该种硬币凑的话 最小需要几块金币
        for coin in coins:
            for i in range(coin, amount+1):
                # 依次根据前面的dp[0] ~ dp[i-1] 来计算当前的dp[i]
                dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1 