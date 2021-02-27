"""
问题描述：给定一个无序数组arr，其中元素可正、可负、可0，给定一个整数k。求
arr所有的子数组中累加和为k的最长子数组长度。

【补充题目】
给定一个无序数组arr,其中元素可正、可负、可0，求arr所有的子数组中正数和负数
个数相等的最长子数组长度。

该问题的解法可以从原问题的解法出发，把正数变成1，把负数变成-1，则问题转化为了
求给定数组中，和为0的最长子数组。

【补充题目】
给定一个无序数组arr,其中元素只是1或0.求arr所有的子数组中0和1个数相等的最长
子数组长度。

该问题的解法也可以从原问题的解法出发，把0变成-1，则该问题转化为了求给定数组中，
和为0的最长子数组。
"""

class LongestSumOfSubArray:
    @classmethod
    def get_longest_sum(cls, arr, k):
        if len(arr) == 0:
            return 0
        i = 0
        total = 0
        max_len = 0
        sum_map = dict()
        sum_map.setdefault(0,-1)
        while i < len(arr):
            total += arr[i]
            if total not in sum_map:
                sum_map[total] = i
            if total - k in sum_map:
                max_len = max(i - sum_map[total-k], max_len)
            i += 1
        return max_len

if __name__ == '__main__':
    # 3
    arr = [1, 2, 3, 3]
    print(LongestSumOfSubArray.get_longest_sum(arr, 6))

    # 6
    arr = [2, 3, 3, 0, 0, 5, 3, -2, 5, 0, -2, 5, -1, 4, 4, 4, 4, -3, 5, 3]
    print(LongestSumOfSubArray.get_longest_sum(arr, 10))

    # 9
    arr = [4, 0, 1, 0, 0, 4, 0, -5, 5, 3, 3, 4, 2, -1, -3, 4, -4, 1, 5, 2]
    print(LongestSumOfSubArray.get_longest_sum(arr, 10))