# -*- coding: utf-8 -*-
"""
给你一个字符串 s，找到 s 中最长的回文子串
例如：
    输入：s = "babad"
    输出："bab"
    解释："aba" 同样是符合题意的答案。
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return None
        if n == 1:
            return s
        start = 0
        max_len = 1
        # dp[i][j] 表示以A[i]开头和A[j]结尾的字符串是否为回文串
        dp = [[False for _ in range(n)]for i in range(n)]

        for i in range(n):
            dp[i][i] = True
        # 依次从倒数第2个往后判断
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                # 首尾字母是否相同 才能满足回文子串的最基本要求
                if s[i] == s[j]:
                    if j-i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                
                # 每次判断完dp[i][j] 都记录一下最长长度
                if d[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        # 最长回文子串的起始字母的下标
                        start = i
        return s[start:start+max_len]
                

