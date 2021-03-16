"""
给定一个字符串类型的数组strs，请找到一种拼接顺序，使得将所有的字符串拼接起来组成的大写
字符串是所有可能性中字典顺序最小的，并返回这个大写字符串。

举例：
strs=['abc', 'de']，可以拼成'abcde'，也可以拼接成'deabc'，但前者的字典顺序更小，所
以返回'abcde'.
strs=['b', 'ba']，可以拼接成'bba'，也可以拼接成'bab'，但后者的字典顺序更小，所以返回
'bab'.
假设有两个字符串a和b，
1. 不能去比较a和b的字典序大小，来拼接；例如上例2
2. 比较a和b拼起来的a+b  和 b和a拼起来的b+a 的字典序，谁小就放前面
解法有效性的证明很复杂，涉及到贪心算法
"""
class compare(str):
    # 重写了字符串的比较 < 的函数
    def __lt__(x, y):
        return x+y <= y+x
class Solution:
    def minString(self , strs ):
        # write code here
        strs.sort(key=compare)
        return ''.join(strs)