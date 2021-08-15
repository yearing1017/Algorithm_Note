"""
问题描述：给定两个字符串str1和str2，再给定三个整数ic、dc和rc，分别代表插入、删除和替换一个字符的代价，返回将str1编辑成str2的最小代价。

举例：
str1='abc', str2='adc', ic=5, dc=3, rc=2
从'abc'编辑成'adc'，把'b'替换成'd'是代价最小的，所以返回2.
str1='abc',str2='adc',ic=5,dc=3,rc=100
从abc编辑成adc，先删除b,然后插入d代价是最小的，所以返回8
str1='abc',str2='abc'，ic=5,dc=3,rc=2
不用编辑了，本来就是一样的字符串，所以返回0
"""


class LowestEditCost:
    # 动态规划
    @classmethod
    def get_lowest_edit_cost_way_1(cls, str1, str2, ic, dc, rc):
        if str1 is None or str2 is None:
            return 0

        len1 = len(str1)
        len2 = len(str2)
        # dp[i][j] 表示将str1[0...i-1] 编辑成 str2[0..j-1]的最小代价
        dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
        # 第一列  word1由原字符串变为word2空字符串的步数 每次都删除一个字符  
        for i in range(len1+1):
            dp[i][0] = dc * i
        # 第一行  word1由空字符串变为word2的步数  每次都新增一个字符
        for j in range(len2+1):
            dp[0][j] = ic * j

        for i in range(1, len1+1):
            for j in range(1, len2+1):
                # 当尾部字符相等时 等价于去看前面的字符转换所需步数
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # 三种情况取最小
                    # 情况1：word1:xxxxE word2:xxxxF 替换尾部字符 说明等于前面字符的转换次数 + word1的1次替换代价
                    # 情况2：word1:xxxD  word2:xxx   删除word1的尾部字符  说明等于前面字符的转换次数 + word1的1次删除代价
                    # 情况3：word1:xxx  word2:xxxD   word1尾部添加字符   说明等于前面字符的转换次数 + word1的1次添加代价
                    dp[i][j] = min(dp[i-1][j-1] + rc, dp[i-1][j] + dc, dp[i][j-1] + ic)
        return dp[len1][len2]

    # 空间压缩后
    @classmethod
    def get_lowest_edit_cost_way_2(cls, str1, str2, ic, dc, rc):
        if str1 is None or str2 is None:
            return 0
        #长度较长的做行对应的字符串  较短的做列对应的字符串
        longs = str1 if len(str1) >= len(str2) else str2
        shorts = str1 if len(str1) < len(str2) else str2
        # 上面的动态规划是str2做列 ，若str1做列 将插入代价和删除代价交换一下
        # 不太理解？？
        if len(str1) < len(str2):
            temp = ic
            ic = dc
            dc = temp
        
        dp = [0 for _ in range(len(shorts)+1)]
        for i in range(1, len(shorts)+1):
            dp[i] = ic * i
        # 行大 行更新  列大 列更新
        for i in range(1, len(longs)+1):
            pre = dp[0] # 保存的左上角的值
            dp[0] = dc * i
            for j in range(1, len(shorts)+1):
                temp = dp[j]
                if longs[i-1] == shorts[j-1]:
                    dp[j] = pre
                else:
                    dp[j] = pre + rc
                dp[j] = min([dp[j], dp[j-1]+ic])
                dp[j] = min([dp[j], temp+dc])
                pre = temp # 更新左上角

        return dp[len(shorts)]


if __name__ == '__main__':
    str1 = "ab12cd3"
    str2 = "abcdf"
    print(LowestEditCost.get_lowest_edit_cost_way_1(str1, str2, 5, 3, 2))
    print(LowestEditCost.get_lowest_edit_cost_way_2(str1, str2, 5, 3, 2))

    str1 = "abcdf"
    str2 = "ab12cd3"
    print(LowestEditCost.get_lowest_edit_cost_way_1(str1, str2, 3, 2, 4))
    print(LowestEditCost.get_lowest_edit_cost_way_1(str1, str2, 3, 2, 4))

    str1 = ""
    str2 = "ab12cd3"
    print(LowestEditCost.get_lowest_edit_cost_way_1(str1, str2, 1, 7, 5))
    print(LowestEditCost.get_lowest_edit_cost_way_2(str1, str2, 1, 7, 5))

    str1 = "abcdf"
    str2 = ""
    print(LowestEditCost.get_lowest_edit_cost_way_1(str1, str2, 2, 9, 8))
    print(LowestEditCost.get_lowest_edit_cost_way_2(str1, str2, 2, 9, 8))
