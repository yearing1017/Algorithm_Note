"""
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序
异位词 指字母相同，但排列不同的字符串。s 和 p 仅包含小写字母

输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m = len(s)
        n = len(p)
        res = []
        if m < n:
            return res
        # s 和 p 仅包含小写字母 建立两个26个小写字母的维护数组 每个位置代表含有该字母的次数
        s_arr = [0] * 26
        p_arr = [0] * 26
        # 首先从头开始遍历 p的长度 看看从头开始能不能匹配上
        for i in range(n):
            s_arr[ord(s[i]) - ord('a')] += 1
            p_arr[ord(p[i]) - ord('a')] += 1
        if s_arr == p_arr:
            res.append(0)

        # 从n位置继续遍历  每次删掉一个s_arr中的旧字母的同时，旧字母指的是前面位置的； 添加一个新字母后面，新的位置的
        for i in range(n, m):
            # 旧的
            s_arr[ord(s[i-n]) - ord('a')] -= 1
            # 新的
            s_arr[ord(s[i]) - ord('a')] += 1
            # 一步一步判断 每次删一个旧的 加一个新的 就判断
            if s_arr == p_arr:
                res.append(i-n+1)
        return res


