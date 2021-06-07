# -*- coding: utf-8 -*-

"""
问题描述:给定一个长度不小于２的数组arr,实现一个函数调整arr,要么让所有的偶数
下标都是偶数,要么让所有的奇数下标都是奇数.

要求:
如果arr的长度为N,函数要求时间复杂度为O(N),额外空间复杂度为O(1).
"""
class EvenOddPlacer:
    @classmethod
    def place_the_num(cls, arr):
        # 最左边的偶数下标
        even = 0
        # 最右边的奇数下标
        odd = 1
        # 最后的数字下标
        end = len(arr) - 1
        while even <= end and odd <= end:
            if arr[end] %2 == 0:
                # 若为偶数，则与之前的even下标代表的数字交换
                arr[even], arr[end] = arr[end], arr[even]
                # even后移
                even += 2
            else:
                arr[odd], arr[end] = arr[end], arr[odd]
                odd += 2
        return arr
        
if __name__ == '__main__':
    my_arr = [1, 8, 3, 2, 4, 6]
    print(EvenOddPlacer.place_the_num(my_arr))