"""
请根据每日 气温 列表 temperatures ，请计算在每一天需要等几天才会有更高的温度。如果气温在这之后都不会升高，请在该位置用 0 来代替
例如：
    输入: temperatures = [73,74,75,71,69,72,76,73]
    输出: [1,1,4,2,1,1,0,0]
"""
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # 单调栈 解法： 栈底到栈顶 存放的是索引 
        n = len(T)
        stack = list()
        res = [0 for _ in range(n)]
        for i in range(n):
            temp = T[i]
            # 从栈顶到 栈底 依次判断 当前元素 和 栈顶元素 当前元素大 则证明是距离栈顶索引元素最近的较大元素 栈顶索引出栈 
            while stack and temp > T[stack[-1]]:
                index = stack.pop()
                # 计算最近的大于栈顶的 离它的距离
                res[index] = i - index
            # 找到大的 先出大的 再入   若小于栈顶 直接入
            stack.append(i)
        return res

