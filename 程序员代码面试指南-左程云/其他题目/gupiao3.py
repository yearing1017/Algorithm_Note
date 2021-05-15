'''
假定你知道某只股票每一天价格的变动。
你最多可以同时持有一只股票。但你可以无限次的交易（买进和卖出均无手续费）。
请设计一个函数，计算你所能获得的最大收益。
例如：输入[5,4,3,2,1] 输出0 由于每天股票都在跌，因此不进行任何交易最优。最大收益为0。
     输入[1,2,3,4,5] 输出4 第一天买进，最后一天卖出最优。中间的当天买进当天卖出不影响最终结果。最大收益为4。 
'''

class Solution:
    def maxProfit(self, prices):
        res = 0
        # 贪心 只要每段是上升的，我就买入卖出
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res
    def maxProfit(self, prices):
        # buy和sell都代表操作之后手里的钱
        buy, sell = -float("inf"), 0
        for p in prices:
            # 可以多次买入卖出 所以不断从上次的sell状态转来 sell-p
            buy = max(buy, sell - p)
            # sell的状态肯定是由buy的状态转来
            sell = max(sell, buy + p)
        return sell