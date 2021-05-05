'''
给出n对括号，请编写一个函数来生成所有的由n对括号组成的合法组合。
例如，给出n=3，解集为：
"((()))", "(()())", "(())()", "()()()", "()(())"
'''
class Solution:
    def generateParenthesis(self , n):
        res = []
        cur_str = ''

        def dfs(cur_str, left, right):
            # 递归终止条件
            if left == 0 and right == 0:
                res.append(cur_str)
                return
            # 剪枝条件 若所剩右括号数量小于左括号数量，说明不合法
            if right < left:
                return
            # 有左括号 就先用左括号
            if left > 0:
                dfs(cur_str+'(', left-1, right)
            if right > 0:
                dfs(cur_str+')', left, right-1)
        dfs(cur_str, n, n)
        return res