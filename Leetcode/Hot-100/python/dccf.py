"""
给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
说明：
拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
example:
    输入: s = "applepenapple", wordDict = ["apple", "pen"]
    输出: true
    解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        # dp[i] 表示 s[0...i-1] 是否可被表示
        dp = [False for _ in range(n+1)]
        # dp的大小设置为n 是为了取到 dp[n] s[0..n-1]
        dp[0] = True
        # dp[j] 的判断： 分为前半部分 s[0...i-1](d[i]) 和 后半部分 s[i...j-1]的判断
        for i in range(n):
            for j in range(i+1, n+1):
                if dp[i] and (s[i:j] in wordDict):
                    dp[j] = True
        # 返回最终的dp[n]
        return dp[-1]