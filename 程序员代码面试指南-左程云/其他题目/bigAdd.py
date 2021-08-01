#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 计算两个数之和
# @param s string字符串 表示第一个整数
# @param t string字符串 表示第二个整数
# @return string字符串
#
class Solution:
    def solve1(self, s, t):
        # write code here
        mlen = max(len(s), len(t))
        # 通过在前面补0 右对齐
        s = s.zfill(mlen)
        t = t.zfill(mlen)
        # 代表进位
        plus = 0
        res = ''
        for i in range(mlen-1, -1, -1):
            last = int(s[i]) + int(t[i]) + plus
            if last > 9:
                plus = 1
                res += str(last - 10)
            else:
                plus = 0
                res += str(last)
        # 处理最后的进位
        if plus: res += str(plus)
        return res[::-1]

    def solve2(self, s, t):
        
        mlen = max(len(s), len(t))
        # 通过在前面补0 右对齐
        s = s.zfill(mlen)
        t = t.zfill(mlen)
        # 代表进位
        plus = 0
        res = ''
        for i in range(mlen-1, -1, -1):
            last = int(s[i]) + int(t[i]) + plus
            plus = last // 10
            res += str(last % 10)
        # 处理最后的进位
        if plus: res += str(plus)
        return res[::-1]