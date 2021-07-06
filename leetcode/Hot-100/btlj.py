"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？
例如：
    输入：m = 3, n = 2
    输出：3
    解释：
        从左上角开始，总共有 3 条路径可以到达右下角。
        1. 向右 -> 向下 -> 向下
        2. 向下 -> 向下 -> 向右
        3. 向下 -> 向右 -> 向下
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 时间复杂度和空间复杂度都为O(m * n)的方法
        dp = [[0 for _ in range(n)]for _ in range(m)]
        # dp[i][j] 代表走到(i,j)位置的路径数
        # 初始化 第一行 和 第一列 都是1 因为只能向左 向右 
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        # dp[i,j]的计算公式
        for i in range(m):
            for j in range(n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

        '''
        #空间优化
        # 一行一行求解
        dp = [1 for _ in range(n)]
        for i in range(1, m):
            # 每次都是左边 + 上边
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[-1]
        '''