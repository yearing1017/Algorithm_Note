"""
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积
输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：4
"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not len(matrix) or not len(matrix[0]):
            return 0
        
        max_side = 0
        m = len(matrix)
        n = len(matrix[0])
        # dp[i,j] 代表以[i,j]位置为右下角的正方形的最大边长
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # 只有元素为1时才考虑
                if matrix[i][j] == '1':
                    # 边界上的dp[i,j]都是1
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        # dp[i,j]以左边、上边、左上角 三个正方形的最小边为 边界
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    # 每次都比较一下
                    max_side = max(max_side, dp[i][j])
        res = max_side * max_side
        return res
