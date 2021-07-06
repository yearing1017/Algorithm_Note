"""
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
例如：
    输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
    输出：7
    解释：因为路径 1→3→1→1→1 的总和最小。
"""
import copy
class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        # 深拷贝 一份 直接在原地修改
        grid_copy = copy.deepcopy(grid)
        for i in range(len(grid_copy)):
            for j in range(len(grid_copy[0])):
                # 左右都是边界 即 原点
                if i == j == 0: continue
                # 第一行的 只能来自左边
                elif i == 0: grid_copy[i][j] = grid_copy[i][j-1] + grid_copy[i][j]
                # 第一列 只能来自上边
                elif j == 0: grid_copy[i][j] = grid_copy[i-1][j] + grid_copy[i][j]
                # 选左边 或 上边的较小值
                else: grid_copy[i][j] = min(grid_copy[i-1][j], grid_copy[i][j-1]) + grid_copy[i][j]
        return grid_copy[-1][-1] 