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
        buy, sell, res = -float("inf"), 0, 0
        for p in prices:
            # 只有一次买入卖出 所以是0-p
            # sell的状态肯定是由buy的状态转来
            buy = max(buy, 0 - p)
            sell = max(sell, buy + p)
            if sell > 0:
                res += 1
        return res

    def maxProfit3(self, prices):
        # buy和sell都代表操作之后手里的钱
        buy, sell = -float("inf"), 0
        p1 = 0
        p2 = 0
        for p in prices:
            # 记录  最大利润时 对应的买入 卖出 价格
            cur_buy = buy
            if (0-p) > cur_buy:
                buy = 0-p
                p1 = p
            
            cur_sell = sell
            if (buy + p) > cur_sell:
                sell = buy + p
                p2 = p
        return p1, p2, sell

if __name__ == '__main__':
    s = Solution()
    prices = [1,2,3]
    print(s.maxProfit2(prices))