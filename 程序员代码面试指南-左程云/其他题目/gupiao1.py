'''
假设你有一个数组，其中第 i 个元素是股票在第 i 天的价格。
你有一次买入和卖出的机会。（只有买入了股票以后才能卖出）。请你设计一个算法来计算可以获得的最大收益。
'''
class Solution:
    def maxProfit(self , prices ):
        cost = float('inf')
        pro = 0
        for p in prices:
            cost = min(cost, p)
            pro = max(pro, p-cost)
        return pro

    def maxProfit2(self, prices):
        # buy和sell都代表操作之后手里的钱
        buy, sell = -float("inf"), 0
        for p in prices:
            # 只有一次买入卖出 所以是0-p
            # sell的状态肯定是由buy的状态转来
            buy = max(buy, 0 - p)
            sell = max(sell, buy + p)

        return sell