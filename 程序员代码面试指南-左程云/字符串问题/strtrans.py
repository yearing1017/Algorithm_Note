'''
对于一个给定的字符串，我们需要在线性(也就是O(n))的时间里对它做一些变形。
首先这个字符串中包含着一些空格，就像"Hello World"一样，
然后我们要做的是把着个字符串中由空格隔开的单词反序，同时反转每个字符的大小写。
比如"Hello World"变形后就变成了"wORLD hELLO"。
'''
class Solution:
    def trans(self, s, n):
        p = n-1
        res = ''
        # 倒序遍历 查找空格位置 找到单词 转换
        for i in range(p, -1, -1):
            if s[i] == ' ':
                for j in range(i+1, p+1):
                    res += self.reverse(s[j])
            res += ' '
            p = i-1# 从此处继续倒序遍历
        # 最后结尾的单词
        for i in range(p+1):
            res += self.reverse(s[i])
        return res
        
        
    def reverse(self, ch):
        if 'a' <= ch <= 'z':
            return ch.upper()
        else:
            return ch.lower()