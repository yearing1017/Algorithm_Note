"""
问题描述: 给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。
一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设
网格的四个边均被水包围。
示例
    输入:
    11000
    11000
    00100
    00011
输出: 3
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    self.infect(grid, i, j, m, n)
        return res

    def infect(self, grid, i, j, m, n):
        if i<0 or i>=m or j<0 or j>=n or grid[i][j] != '1':
            return
        grid[i][j] = '2'
        self.infect(grid, i-1, j, m, n)
        self.infect(grid, i+1, j, m, n)
        self.infect(grid, i, j-1, m, n)
        self.infect(grid, i, j+1, m, n)