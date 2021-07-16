'''
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

输入: [1,2,3,0,2]
输出: 3 
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

卖完要隔一天才能买，那么就多记录上一次卖的状态即可
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/solution/5xing-dai-ma-gao-ding-suo-you-gu-piao-ma-j6zo/
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell_pre, sell = -float("inf"), 0, 0
        for p in prices:
            # buy 只能从两个状态转来 本身保持不变 冷冻期买入
            buy = max(buy, sell_pre - p)
            sell_pre = sell
            sell = max(sell, buy + p)
        return sellß