'''
定义重复字符串是由两个相同的字符串首尾拼接而成，例如 abcabc 便是长度为6的一个重复字符串，而 abcba 则不存在重复字符串。
给定一个字符串，请返回其最长重复子串的长度。若不存在任何重复字符子串，则返回 0 。

数据范围：
字符串长度不大于 2 * 10^4
'''
class Solution:
    def solve(self , a ):
        # write code here
        n = len(a)
        if len(a) < 2:
            return 0
        # 代表当前这一轮查找 找到的重复子串的长度
        flag = 0
        # i 代表枚举的子串的长度 由题意知道重复子串是首尾拼接的，所以最长是n/2
        for i in range(n//2, 0, -1):
            # j是枚举的起点
            for j in range(n-i):
                # 依次向后遍历判断字符是否相等
                if a[j] == a[j + i]:
                    flag += 1
                else:
                    # 只要该长度下有不相等的  说明最长的不是这个长度
                    flag = 0
                if flag == i:
                    return i * 2
        return 0