'''
以字符串的形式读入两个数字，编写一个函数计算它们的和，以字符串形式返回。
（字符串长度不大于100000，保证字符串仅由'0'~'9'这10种字符组成）
'''
class Solution:
    def solve(self , s , t ):
        # write code here
        '''
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
        '''

        max_len = max(len(s), len(t))
        s =s.zfill(max_len)
        t = t.zfill(max_len)
        
        plus = 0
        res = ''
        for i in range(max_len-1, -1, -1):
            ans = int(s[i]) + int(t[i]) + plus
            plus = ans // 10
            res += str(ans % 10)
        if plus:
            res += str(plus)
        return res[::-1]