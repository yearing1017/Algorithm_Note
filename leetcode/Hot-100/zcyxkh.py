"""
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度
例如：
    输入：s = "(()"
    输出：2
    解释：最长有效括号子串是 "()"
    输入：s = ")()())"
    输出：4
    解释：最长有效括号子串是 "()()"
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        # dp[i]代表以s[i]结尾的字符串 当前有效括号的最长长度
        dp = [0 for _ in range(len(s))]
        for i in range(1, len(s)):
            # 只有以右括号结尾时才是有效的
            if s[i] == ")":
                # 第一种情况 s[i-1] == "("
                if s[i-1] == "(":
                    # 此处的 = 可以不用 因为等于0 相当于前面只有一个括号
                    if i - 2 >= 0:
                        dp[i] = dp[i-2] + 2
                    # dp[i-2] 不存在 前面有效的长度为0
                    else:
                        dp[i] = 0 + 2
                # 情况2 ”()(())” 两个右括号紧挨着
                elif (i - dp[i-1] > 0) and s[i-1] == ")":
                    # 此处的 = 可以不用 因为等于0 相当于前面只有一个括号
                    if (i - dp[i-1] -2) >= 0:
                        dp[i] = dp[i - dp[i-2] -2] + dp[i-1] + 2
                    else:
                        dp[i] = dp[i-1] + 2
            max_len = max(max_len, dp[i])
        return max_len


