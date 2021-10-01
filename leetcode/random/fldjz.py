'''
在给定的网格中，每个单元格可以有以下三个值之一：
    值 0 代表空单元格；
    值 1 代表新鲜橘子；
    值 2 代表腐烂的橘子。
    每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。
返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1

思路：
    层次遍历的思想；先将腐烂的橘子入队，然后出队，遍历和它相邻的新鲜橘子，腐烂掉并入队；
'''
class Solution:
    def orangesRotting(self, grid):
        row, col, time = len(grid), len(grid[0]), 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = []
        # 先将腐烂的橘子 入队
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i, j, time))
        # bfs
        while queue:
            i, j, time = queue.pop(0)
            for di, dj in directions:
                # 找到4个方向上相邻的新鲜橘子
                if 0 <= i + di < row and 0 <= j + dj < col and grid[i + di][j + dj] == 1:
                    # 腐烂掉并入队
                    grid[i + di][j + dj] = 2
                    queue.append((i + di, j + dj, time + 1))
        # 若最终仍存在新鲜的 返回-1
        for row in grid:
            if 1 in row: return -1

        return time