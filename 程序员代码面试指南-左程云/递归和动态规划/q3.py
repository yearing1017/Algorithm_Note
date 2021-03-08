"""
问题描述：给定数组arr,arr中所有的值都为正数且不重复。每个值代表一种面值的货币，每种
面值的货币可以使用任意张，再给定一个整数aim代表要找的钱数，求组成aim的最少货币数。

补充题目：给定数组arr，arr中所有的值都为正数。每个值仅代表一张钱的面值，再给定一个整
数aim代表要找的钱数，求组成aim的最少货币数。
"""


class CoinsCounter:
    # 暴力递归
    @classmethod
    def min_coins_count_1(cls, arr, aim):
        if not arr or aim <0:
            return -1
        return cls.process(arr, 0, aim)
    
    @classmethod
    def process(cls, arr, i, rest):
        # base case
        if i == len(arr):
            return 0 if rest == 0 else -1
        # 最少张数 初始值为-1 因为还没找到有效解
        res = -1
        # 一次尝试当前面值arr[i] 0.1.2...k张 但不能超过rest
        for k in range(rest+1):
            # 使用了k张arr[i] 剩下的钱为rest - k*arr[i] 交给剩下的钱去搞
            after = cls.process(arr, i+1, rest-k*arr[i])
            if after != -1:
                # 说明这个后续有效
                if res == -1:
                    res = after + k
                else:
                    res = min(res, after+k)
        return res
    
    @classmethod
    def min_coins_count_2(cls, arr, aim):
        # dp[N+1][aim+1]的含义：从当前面值遍历，组成aim的最少货币数
        # 此题应求dp[0][aim]
        if not arr or aim < 0:
            return -1
        N = len(arr)
        dp = [[-1 for _ in range(aim+1)]for  _ in range(N+1)]
        # 设置最后一行的值 只有dp[N][0]为0 其余为-1 表示已经无面值考虑 且当前剩余钱为0
        dp[N][0] = 0
        # 从底向上计算每一行：
        for i in range(N-1, -1,-1):
            #从左到右计算每一列
            for rest in range(aim+1):
                # dp[i][rest]的初始值为-1 表示无效
                # 下面的值如果有效
                if dp[i+1][rest] != -1:
                    # 先设置成下面的值
                    dp[i][rest] = dp[i+1][rest]
                # 如果左边的位置不越界且有效
                if rest-arr[i] >=0 and dp[i][rest-arr[i]] != -1:
                    # 如果之前下面的值无效 就设置为左边的
                    if dp[i][rest] == -1:
                        dp[i][rest] = dp[i][rest-arr[i]] + 1
                    else:
                        #都有效
                        dp[i][rest] = min(dp[i][rest-arr[i]] + 1, dp[i][rest])
        return dp[0][aim]

    # 空间压缩
    @classmethod
    def min_coins_count_3(cls, arr, aim):
        if not arr or aim < 0:
            return -1
        N = len(arr)
        dp = [-1 for _ in range(aim+1)]
        # 设置最后一行的值 只有dp[N][0]为0 其余为-1 表示已经无面值考虑 且当前剩余钱为0
        dp[0] = 0

        # 从底向上计算每一行：
        for i in range(N-1, -1,-1):
            #从左到右计算每一列
            for rest in range(1, aim+1):
                # 如果左边的位置不越界且有效
                if rest-arr[i] >=0 and dp[rest-arr[i]] != -1:
                    # 如果之前下面的值无效 就设置为左边的
                    if dp[rest] == -1:
                        dp[rest] = dp[rest-arr[i]] + 1
                    else:
                        #都有效
                        dp[rest] = min(dp[rest-arr[i]] + 1, dp[rest])
        return dp[aim]


if __name__ == '__main__':
    print(CoinsCounter.min_coins_count_1([5,2,3],20))
    print(CoinsCounter.min_coins_count_2([5,2,3],20))
    print(CoinsCounter.min_coins_count_3([5,2,3],5))