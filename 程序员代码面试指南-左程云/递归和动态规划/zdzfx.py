# 给定一个由0和1组成的2维矩阵，返回该矩阵中最大的由1组成的正方形的面积
class Solution:
    def solve(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        # 最大正方形的边长
        max_side = 0
        dp = [[0 for _ in range(col)]for _ in range(row)]
        # dp[i][j] 代表以i，j为右下角点的正方形的边长
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        # 取决于左边、上边、左上的正方形的边长的最小值
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_side = max(max_side, dp[i][j])
        return max_side * max_side    