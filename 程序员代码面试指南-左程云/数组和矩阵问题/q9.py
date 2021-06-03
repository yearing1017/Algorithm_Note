# -*- coding: utf-8 -*-

"""
问题描述:先给出可整合数组的定义.如果一个数组在排序之后,每相邻两个数差的绝对值
都为１,则该数组为可整合数组.例如,[5, 3, 4, 6, 2]排序之后为[2, 3, 4, 5, 6],
符合每相邻两个数差的绝对值都为１,所以这个数组为可整合数组.
给定一个整型数组arr,请返回其中最大可整合子数组的长度.例如, [5, 5, 3, 2, 6, 4, 3]
的最大可整合子数组为[5, 3, 2, 6, 4],所以返回5.

思路： 依次遍历子数组（O(N^2)），查看子数组是否符合条件: 根据子数组的最大值-最小值 + 1 是否等于 子数组长度来判断 （O(1)）
"""
import sys

class IntegratedNumCounter:
    @classmethod
    def getLength(cls, arr):
        if not arr:
            return 0
        length = 0
        max_value = 0
        min_value = 0
        my_set = set()
        for i in range(len(arr)):
            max_value = -sys.maxsize
            min_value = sys.maxsize
            for j in range(i, len(arr)):
                if arr[j] in my_set:
                    break
                my_set.add(arr[j])
                max_value = max(arr[j], max_value)
                min_value = min(arr[j], min_value)

                if max_value - min_value == j - i:
                    length = max(length, j - i + 1)
            my_set.clear()
        
        return length

if __name__ == '__main__':
    my_arr = [5, 5, 3, 2, 4, 6, 4]
    print(IntegratedNumCounter.getLength(my_arr))
