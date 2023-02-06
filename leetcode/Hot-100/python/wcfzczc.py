# -*- coding: utf-8 -*-
"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
    输入: s = "abcabcbb"
    输出: 3 
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        pre = -1
        length = 0
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                pre = max(pre, dic[s[i]])
            # 将s[i]的索引加到字典 或更新索引
            dic[s[i]] = i
            # pre代表与当前子串中相同字母的最大位置索引
            cur_len = i - pre
            length = max(length, cur_len)
        return length