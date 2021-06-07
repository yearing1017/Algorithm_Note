# -*- coding: utf-8 -*-

"""
问题描述:给定一个排序数组arr和整数k，不重复打印arr中所有相加和为k的不降序二元组。
例如，arr=[-8, -4, -3, 0, 1, 2, 4, 5, 8, 9], k=10，打印结果为:
1,9
2,8

补充题目：
给定排序数组arr和整数k，不重复打印arr中所有相加和为k的不降序三元组。
例如，arr=[-8, -4, -3, 0, 1, 2, 4, 5, 8, 9], k=10，打印结果为:
-4, 5, 9
-3, 4, 9
-3, 5, 8
0, 1, 9
0, 2, 8
1, 4, 5
"""

class KnumOfSum:
    @classmethod
    def get_two_tuple_of_sum(cls, arr, k):
        if not arr or len(arr) == 1:
            return
        res = []
        # 左右指针逼近
        left = 0
        right = len(arr) - 1
        while left < right:
            if arr[left] + arr[right] < k:
                left += 1
            elif arr[left] + arr[right] > k:
                right -= 1
            else:
                # 判断不重复
                if left == 0 or arr[left-1] != arr[left]:
                    res.append((arr[left], arr[right]))
                    left += 1
                    right -= 1
        return res

    @classmethod
    def get_three_tuple_of_sum(cls, arr, k):
        if not arr or len(arr) < 3:
            return
        for i in range(len(arr)):
            # 三元组问题转为二元组的解法
            new_k = k - arr[i]

            if i == 0 or arr[i] != arr[i-1]:
                # 固定第一个  转为二元组的解法
                res = cls.get_two_tuple_of_sum(arr[i+1:], new_k)
                if res:
                    for x, y in res:
                        print(arr[i], x, y)

if __name__ == '__main__':
    my_arr = [-8, -4, -3, 0, 1, 2, 2, 4, 5, 8, 9]
    print(KnumOfSum.get_two_tuple_of_sum(my_arr, 10))
    KnumOfSum.get_three_tuple_of_sum(my_arr, 10)