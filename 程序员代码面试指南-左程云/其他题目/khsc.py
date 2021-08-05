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
            '''
            :param cur_str: 从根结点到叶子结点的路径字符串
            :param left: 左括号还可以使用的个数
            :param right: 右括号还可以使用的个数
            '''
            #递归终止条件
            if left == 0 and right == 0:
                res.append(cur_str)
                return
            # 剪枝条件
            # 若所剩右括号xiao于左括号 则说明先使用的右 不合法
            if right < left:
                return
            # 只有还有左括号就先用左
            if left > 0:
                dfs(cur_str + '(', left-1, right)
            if right > 0:
                dfs(cur_str+')', left, right-1)
        dfs(cur_str, n, n)
        return res
        