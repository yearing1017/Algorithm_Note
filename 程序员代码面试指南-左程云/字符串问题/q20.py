"""
问题描述：给定一个字符串str，返回str的最长无重复字符子串的长度。

举例：
str="abcd"，返回4
str="aabcb"，最长无重复字符子串为"abc"，返回3

要求：
如果str的长度为N,请实现时间复杂度为O(N)的方法。
"""

class LongestNotRepeatStr:
    @classmethod
    def get_longest_sut_str(cls, s):
        pre = -1 # 最长不重复子串开始前的一个位置 左指针
        length = 0 # 最终结果
        dic = {} # key是每个字符 val是该字符最后出现的位置 离最长不重复子串的最近位置
        # i为最长不重复子串的最后字符位置
        for i in range(len(s)):
            if s[i] in dic:
                pre = max(pre, dic[s[i]])
            dic[s[i]] = i
            cur_len = i - pre # 遍历到当前字符 最长不重复子串的长度
            length = max(length, cur_len)
        return length

if __name__ == '__main__':
    my_str = 'kqetrpslqrpbbdmjvjba'
    print(LongestNotRepeatStr.get_longest_sut_str(my_str))