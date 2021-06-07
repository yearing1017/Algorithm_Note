# -*- coding: utf-8 -*-

"""
问题描述:给定一个长度为N的整型数组arr,其中有N个互不相等的自然数1~N,请实现
arr的排序,但是不要把下标0~N-1位置上的数通过直接赋值的方式替换成1~N.

要求:
时间复杂度为O(N),额外空间复杂度是O(1)
"""

class ArrSorter:
    @classmethod
    def sort_arr(cls, arr):
        # 原地置换
        if not arr or len(arr) < 2:
            return arr
        # 对每个位置进行判断交换
        for i in range(len(arr)):
            while arr[i] != i + 1:
                # 当前位置的数 应该放在的坐标 交换的时候需要使用临时变量，因为arr[i]会改变
                temp = arr[i] - 1
                arr[i], arr[temp] = arr[temp], arr[i]
        return arr

if __name__ == '__main__':
    my_arr = [3, 5, 1, 2, 8, 6, 4, 7]
    print(ArrSorter.sort_arr(my_arr))