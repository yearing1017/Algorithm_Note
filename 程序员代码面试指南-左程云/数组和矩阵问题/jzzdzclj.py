'''
给定一个矩阵，矩阵内所有数均为非负整数。
求一条路径，该路径上所有数是递增的。
这个路径必须满足以下条件：
1、对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外。
2、你不能走重复的单元格。即每个格子最多只能走一次。

题解：https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/solution/ji-ge-wen-da-kan-dong-shen-du-sou-suo-ji-yi-hua-sh/
'''
class Solution:
    def solve(self, matrix):
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        # record[i][j]表示走到当前位置时，最长的递增路径长度
        record = [[0 for _ in range(n)]for _ in range(m)]
        res = 0

        # 深度遍历 根据四个方向上值的大小 找到i，j位置的值
        def dfs(i, j):
            if record[i][j]:
                return record[i][j]
            templen = 0
            # 遍历4个方向进行计算，找到四个方向中最大的+1
            for dx, dy in [[1,0], [-1,0], [0,1], [0,-1]]:
                x, y = i+dx, j+dy
                if 0<=x<m and 0<=y<n and matrix[x][y] > matrix[i][j]:
                    templen = max(templen, dfs(x, y))
            record[i][j] = templen + 1
            return templen + 1

        for i in range(m):
            for j in range(n):
                record[i][j] = dfs(i,j)
                res = max(res, record[i][j])
        return res

    
            


