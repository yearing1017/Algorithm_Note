"""
问题描述：给定字符串str，判断是不是整体有效的括号字符串。
举例：
str="()"，返回true;str="(()())",返回true;str="(())"，返回true.
str="(()"，返回false;str="()(",返回false;str="()a()"，返回false.

补充题目：
给定一个括号字符串str，返回最长的有效括号子串。
举例：
str="(()())",返回6；str="())"，返回2;str="()(()()(",返回4。
"""

class ParenthesesProblem:
    @classmethod
    def is_valid(cls, strs):
        if not strs or len(strs) == 1:
            return False
        length = len(strs)
        # 左右括号到目前位置出现的次数
        left_num = 0
        right_num = 0
        for s in strs:
            if s != '(' or s != ')':
                return False
            if s == '(':
                left_num += 1
            if s == ')':
                right_num += 1
            # 到当前位置 若左括号少于右括号出现的次数  则不是有效的
            if left_num < right_num:
                return False
        # 到最后左右数量不等  不是有效的
        if left_num != right_num:
            return False
        return True
        
    @classmethod
    def get_max_length(cls, strs):
        if not strs or len(strs) == 1:
            return 0

        res = 0
        length = len(strs)
        # dp[i] 代表 必须以str[i]结尾的最长有效括号子串长度
        dp = [0 for _ in range(length)]
        i = 0
        while i < length:
            if strs[i] == ')':
                pre = i - dp[i-1] - 1
                # 情况1 （（）（）） 最后的右括号前面有一个有效的最长括号  + 左括号
                if pre >= 0 and strs[pre] == '(':
                    dp[i] = dp[i-1] + 2
                    # 情况2 （）（（）（）） 最后的右括号 + 前面有一个有效的最长括号长度 + 左括号 + 左括号前面的一个最长有效括号长度 
                    if pre > 0:
                        dp[i] = dp[i] + dp[pre-1]
            res = max([res, dp[i]])
            i += 1
        return res


if __name__ == '__main__':
    str1 = '((())())'
    print(ParenthesesProblem.is_valid(str1))
    print(ParenthesesProblem.get_max_length(str1))

    str2 = '(())(()(()))'
    print(ParenthesesProblem.is_valid(str2))
    print(ParenthesesProblem.get_max_length(str2))

    str3 = '()(()()('
    print(ParenthesesProblem.is_valid(str3))
    print(ParenthesesProblem.get_max_length(str3))
