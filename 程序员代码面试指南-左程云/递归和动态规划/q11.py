"""
问题描述：给定两个字符串str1和str2，返回两个字符串的最长公共子串。

举例
str1="1AB2345CD", str2="12345EF", 返回2345

要求
如果str1长度为M，str2长度为N，实现时间复杂度为O(M*N)，额外空间复杂度为O(1)的方法。
"""


class MaxSubPubstrFinder:
    # 传统的动态规划方法 先求dp矩阵 dp[i][j]代表将str1[i] 和 str[j] 当做公共子串最后一个字符的情况下 公共子串的最长长度
    @classmethod
    def get_max_common_length(cls, str1, str2):
        str_len1 = len(str1)
        str_len2 = len(str2)

        dp = [[0 for _ in range(str_len2)]for _ in range(str_len1)]

        # 第一列的处理
        for i in range(str_len1):
            if str1[i] == str2[0]:
                dp[i][0] = 1

        # 第一行的处理
        for j in range(str_len2):
            if str1[0] == str2[j]:
                dp[0][j] = 1

        # ij位置：向左扩多长 
        for i in range(1, str_len1):
            for j in range(1, str_len2):
                if str1[i] == str2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1

        return dp

    # 表示从dp矩阵中找到最大值和最大值对应的最后一个字符的索引
    @classmethod
    def get_max_common_str(cls, str1, str2):
        if not str1 or not str2:
            return ''

        dp = cls.get_max_common_length(str1, str2)

        max_length = 0
        row = 0
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    row = i

        return str1[row-max_length+1:row+1]   

# 空间压缩 斜线求法 从右上角开始 向右下方斜线求
# 因为矩阵中的ij位置的元素 = 左上方+1
    @classmethod
    def LCS(self , str1 , str2 ):
        # write code here
        # 动态规划的空间压缩版本 
        if not str1 or not str2 or str1 == '' or str2 == '':
            return ''
        row = 0 # 斜线开始的行
        col = len(str2)-1 #斜线开始的列
        max_len = 0 # 记录最大长度
        end = 0 # 记录最大长度时对应的子串结尾位置
        while row < len(str1):
            i = row
            j = col
            zs = 0 # 代表当前所求值的左上方的值
            while i<len(str1) and j<len(str2):
                if str1[i] != str2[j]:
                    zs = 0
                else: 
                    zs += 1
                # 纪录最大值和位置
                if zs > max_len:
                    end = i
                    max_len = zs
                # 此处 i++ j++代表当前斜线向右下方移动计算
                i += 1
                j += 1
            # 斜线开始的位置列先向左移动
            if col > 0:
                col -= 1
            # 列移动到最左之后 行下移
            else:
                row += 1
        return str1[end - max_len + 1 : end+1]
        

if __name__ == '__main__':
    str1 = "1AB2345CD"
    str2 = "12345EF"
    print(MaxSubPubstrFinder.get_max_common_str(str1, str2))
    print(MaxSubPubstrFinder.LCS(str1, str2))