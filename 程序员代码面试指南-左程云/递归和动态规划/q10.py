"""
问题描述：给定两个字符串str1和str2，返回两个字符串的最长公共子序列。
举例：
str1="1A2C3D4B56", str2="B1D23CA45B6A"。
"123456"或者"12C4B6"都是最长公共子序列，返回哪一个都行。
"""
class SubSeqFinder:
    @classmethod
    def LCS(cls, s1 , s2 ):
        # write code here
        if not s1 or not s2:
            return ""
        dp = cls.getdp(s1, s2)
        m = len(s1)-1
        n = len(s2)-1
        # 最长公共子序列的长度
        res = [0] * dp[m][n]
        #print(res)
        index = len(res) - 1
        while index>=0:
            if n>0 and dp[m][n] == dp[m][n-1]:
                n -= 1
            elif m>0 and dp[m][n] == dp[m-1][n]:
                m -=1
            else:
                res[index] = s1[m]
                index -= 1
                m -= 1
                n -= 1
        #print(res)
        return ''.join(res)

    @classmethod
    def getdp(cls, s1,s2):
        dp = [[0 for _ in range(len(s2))]for _ in range(len(s1))]
        dp[0][0] = 1 if s1[0] == s2[0] else 0
        # 设置第一列的值
        for i in range(1, len(s1)):
            if s1[i] == s2[0]:
                dp[i][0] = 1
            else:
                dp[i][0] = max(dp[i-1][0],0)
        # 设置第一行的值
        for j in range(1, len(s2)):
            if s1[0] == s2[j]:
                dp[0][j] = 1
            else:
                dp[0][j] = max(dp[0][j-1],0)
        # i，j位置对应三种情况
        for i in range(1, len(s1)):
            for j in range(1, len(s2)):
                # 当末尾元素不等时
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                if s1[i] == s2[j]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)
        #print(dp)
        return dp

    @classmethod
    def get_dp_2(cls, str1, str2):
        str_len1 = len(str1)
        str_len2 = len(str2)

        dp = [[0 for _ in range(str_len2)] for _ in range(str_len1)]
        flag = False
        for col in range(str_len2):
            if flag == 1:
                dp[0][col] = 1
                continue

            if str1[0] == str2[col]:
                dp[0][col] = 1
                flag = 1

        flag = 0 if flag == 1 else 0
        for row in range(str_len1):
            if flag == 1:
                dp[row][0] = 1
                continue

            if str1[row] == str2[0]:
                dp[row][0] = 1
                flag = 1

        for row in range(1, str_len1):
            for col in range(1, str_len2):
                dp[row][col] = max([dp[row-1][col], dp[row][col-1]])
                if str1[row] == str2[col]:
                    dp[row][col] = max([dp[row][col], dp[row-1][col-1] + 1])
        return dp

if __name__ == '__main__':
    str1 = '1A2C3D4B56'
    str2 = 'B1D23CA45B6A'
    print(SubSeqFinder.LCS(str1, str2))
    #dp = SubSeqFinder.get_dp(str1,str2)
    #print(dp)