"""
问题描述：给定一个矩阵m，从左上角开始每次只能向右或者向下走，最后到达右下角的位置，路径上所有的数字累加起来
就是路径和，返回所有的路径中最小的路径和。比如，给定m如下：
1 3 5 9
8 1 3 4
5 0 6 1
8 8 4 0
路径1， 3， 1， 0， 6， 1， 0是所有路径中路径和最小的，所以返回12.
"""


class ShortestWay:
    # 方法一：建立完整的dp矩阵，时间复杂度和空间复杂度都为O(M*N)
    @classmethod
    def find_shortest_way_1(cls, arr):
        if not arr or len(arr) == 0 or not arr[0] or len(arr[0]) == 0:
            return 0
        row = len(arr)
        col = len(arr[0])
        dp = [[None for _ in range(col)]for _ in range(row)]
        dp[0][0] = arr[0][0]
        # 针对第一行和第一列进行初始化
        for i in range(1, col):
            dp[0][i] = dp[0][i-1] + arr[0][i]
        for j in range(1, row):
            dp[j][0] = dp[j-1][0] + arr[j][0]
        # 根据关系式 dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + arr[i][j] 动态规划
        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] =  min(dp[i-1][j],dp[i][j-1]) + arr[i][j]

        return dp[-1][-1]

    # 方法二 因为此题不需求完整的路径 所以对dp矩阵可进行空间压缩，使用一维数组代替dp矩阵
    @classmethod
    def find_shortest_way_2(cls, arr):
        if not arr or len(arr) == 0 or not arr[0] or len(arr[0]) == 0:
            return 0
        more = max(len(arr),len(arr[0])) #表示行数和列数较大的一方
        less = min(len(arr),len(arr[0])) #表示行数和列数较小的一方
        rowmore = True if more == len(arr) else False # 表示行数是否大于等于列数
        res = [None for _ in range(less)] #较小的一方为结果数组的长度
        res[0] = arr[0][0]
        # 当行大于等于列时，进行每行的滚动更新，因为此时数值是列，列小，本题求最小值
        # 当行小于列时，进行每列的滚动更新，因为此时数值是行，行小，本题求最小值
        #第一行 或 第一列的初始化
        for i in range(1, less):
            if rowmore:
                res[i] = res[i-1] + arr[0][i]
            else:
                res[i] = res[i-1] + arr[i][0]
        for i in range(1, more):
            # 进行 下一行第一个元素的更新 或 下一列第一个元素的更新
            if rowmore:
                res[0] = res[0] + arr[i][0]
            else:
                res[0] = res[0] + arr[0][i]
            for j in range(1, less):
                if rowmore:
                    res[j] = min(res[j-1], res[j]) + arr[i][j]
                else:
                    res[j] = min(res[j-1], res[j]) + arr[j][i]
        return res[-1]
 



if __name__ == '__main__':
    m = [
            [1, 3, 5, 9],
            [8, 1, 3, 4],
            [5, 0, 6, 1],
            [8, 8, 4, 0]
    ]

    print(ShortestWay.find_shortest_way_1(m))
    print(ShortestWay.find_shortest_way_2(m))