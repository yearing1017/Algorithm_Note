# -*- coding: utf-8 -*-
"""
两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。
给你两个整数 x 和 y，计算并返回它们之间的汉明距离。
例如：
输入：x = 1, y = 4
输出：2
解释：
1   (0 0 0 1)
4   (0 1 0 0)
"""
class Solution:
    def hammingDistance(self, x, y):
        """
        对两个字符串进行异或运算，并统计结果为1的个数，那么这个数就是汉明距离
        bin() 返回一个整数 int 或者长整数 long int 的二进制表示; count() 方法用于统计字符串里某个字符出现的次数
        """
        return bin(x^y).count("1")