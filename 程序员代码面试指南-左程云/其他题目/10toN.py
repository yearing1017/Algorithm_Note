# 给定数10进制数M 转换为N进制

class Solution:
    def solve(self , M , N ):
        if M == 0:
            return 0
        # 转为1-16进制时的余数集合
        s = '0123456789ABCDEF'
        flag = False
        res = ''
        # 负数转为正数计算
        if M < 0:
            flag = True
            M = -M
        # 循环取余 转进制
        while M:
            res += s[M % N]
            M //= N
        if flag:
            res += '-'

        return res[::-1]