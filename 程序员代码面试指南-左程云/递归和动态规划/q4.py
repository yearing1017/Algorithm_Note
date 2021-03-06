'''
机器人到达指定位置方法数
排成一行的位置1-N，N大于等于2，开始时机器人在M位置，M一定属于1-N，机器人可以往左走也可以往右走
如果机器人在1位置，下一步只能往右走，在N位置，下一步只能往左走
规定机器人必须走K步，最终到达P位置，P属于1-N。
规定4个参数NMKP,返回方法数,时间复杂度要求O(N*K)
'''

class Root:
    # 暴力递归
    @classmethod
    def way1(cls, N, M, K, P):
        #  参数无效直接返回0
        if N<2 or K<1 or M<1 or M>N or P<1 or P>N:
            return 0
        return cls.walk(N, M, K, P)
    # cur 当前位置 rest 还剩多少步没走
    @classmethod
    def walk(cls, N, cur, rest, P):
        # 如果没有剩余步数 且 当前位置是p 则 移动有效 返回1 代表1种方法
        if rest == 0:
            return 1 if cur == P else 0
        # 当前位置为1 只能右走
        if cur == 1:
            return cls.walk(N, 2, rest-1, P)
        # 当前位置为N，只能向左走
        if cur == N:
            return cls.walk(N, N-1, rest-1, P)
        # cur 在中间 向左 向右 加起来 为总方法数
        return cls.walk(N, cur-1, rest-1, P) + cls.walk(N, cur+1, rest-1, P)
 

    # 优化为动态规划
    @classmethod
    def way2(cls, N, M, K, P):
         #  参数无效直接返回0
        if N<2 or K<1 or M<1 or M>N or P<1 or P>N:
            return 0
        dp = [[0 for _ in range(N+1)] for _ in range(K+1)]
        dp[0][P] = 1
        for i in range(1, K+1):
            for j in range(1, N+1):
                if j == 1:
                    dp[i][j] = dp[i-1][2]
                elif j == N:
                    dp[i][j] = dp[i-1][N-1]
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        return dp[K][M]


if __name__ == '__main__':
    # 3
    print(Root.way1(5, 2, 3, 3))
    print(Root.way2(5, 2, 3, 3))