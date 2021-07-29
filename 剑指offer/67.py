'''
剑指offer 67

字符串转为整数 例如：
输入: "   -42"
输出: -42
解释: 第一个非空白字符为 '-', 它是一个负号。
     我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。

输入: "4193 with words"
输出: 4193
解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字

输入: "-91283472332"
输出: -2147483648
解释: 数字 "-91283472332" 超过 32 位有符号整数范围。 
     因此返回 INT_MIN (−231)

'''
class Solution:
    def strToInt(self, str: str) -> int:
        res = 0  
        sign = 1 # 标记正负数
        i = 0   # 遍历str专用
        length = len(str)

        int_max, int_min, bundry = 2**31 - 1, -2**31, 2**31 // 10

        if not str: return 0

        # 先把前面的空格除掉
        while str[i] == ' ':
            i += 1
            # 说明全是空格
            if i == length:
                return 0
        # 首部符号
        if str[i] == '-':
            sign = -1
        # 判断完正负号 都要右移一步
        if sign in '+-':
            i += 1
        # 数字位
        for j in range(i, length):
            if str[j] < '0' or str[j] > '9':
                break
            # 溢出整型的上下边界时
            if res > bundry or(res == bundry and str[j] > '7'):
                return int_max if sign == 1 else int_min
            res = 10 * res + (ord(str[j]) - ord('0'))
        return sign * res
