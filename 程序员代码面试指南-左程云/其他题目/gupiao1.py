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