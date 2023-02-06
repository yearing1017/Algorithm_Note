"""
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串
例如：
    输入："aaa"
    输出：6
    解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        n = len(s)
        # 动态规划  dp[i][j] 代表 s[i...j]是否为回文子串
        dp = [[0 for _ in range(n)] for _ in range(n)]
        ans = 0
        # 倒着来 因为 dp[i+1][j-1] 是dp[i][j] 的下方元素
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                # 情况1 长度等于1
                if i == j:
                    dp[i][j] = 1
                # 情况2 长度等于2 
                elif j == i+1 and s[i] == s[j]:
                    dp[i][j] = 1
                # 情况3 长度大于2时 首先 检测中间的子串 + 两段的单个字母
                elif j-i >= 2 and dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = 1
                # 得到一个值 就去计数
                if dp[i][j]: ans += 1
        return ans