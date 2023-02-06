"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
例如：
    输入：n = 3
    输出：["((()))","(()())","(())()","()(())","()()()"]
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur_str = ''
        # left: 当前剩余可用的左括号的个数 right:当前可用的右括号的个数
        def dfs(cur_str, left, right):
            # 递归终止条件
            if left == 0 and right == 0:
                res.append(cur_str)
                return
            # 剪枝条件
            # 若当前右括号个数小于左括号  则说明之前先使用了右  结果肯定不合法
            if right < left:
                return
            # 有左先用左
            if left > 0:
                dfs(cur_str+'(', left-1, right)
            if right > 0:
                dfs(cur_str+')', left, right-1)
        dfs(cur_str, n, n)
        return res