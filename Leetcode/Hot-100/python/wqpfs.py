'''
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。
完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
示例
    输入：n = 12
    输出：3 
    解释：12 = 4 + 4 + 4
'''
class Solution:
    def numSquares(self, n: int) -> int:
        # 存放 小于 n 的所有完全平方数 例如：12 得到的nums 0,1,4,9
        nums = [i**2 for i in range(int(math.sqrt(n))+1)]
        # dp[n] 表示 和为n的最少完全平方数数量 初始化为 i 也就是 12 最坏情况就是12个1组成 
        dp = [i for i in range(n+1)]
        for i in range(1, n+1):
            for num in nums:
                # i-num 不存在时 结束该dp[i]的求解
                if i < num:
                    break
                # 转移方程 拿i-num num是完全平方数 每次都遍历nums 去找最小的dp[i]
                dp[i] = min(dp[i], dp[i-num] + 1)
        return dp[-1]