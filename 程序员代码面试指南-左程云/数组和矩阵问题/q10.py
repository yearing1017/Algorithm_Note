# -*- coding: utf-8 -*-

"""
给定一个数组arr，该数组无序，但每个值均为正数，再给定一个正数k。求arr的
所有子数组中所有元素相加和为k的最长子数组长度。
例如，arr=[1, 2, 1, 1, 1]， k=3
累加和为3的最长子数组长度为[1, 1, 1]，所以结果返回3
"""

class MaxLength:
    @classmethod
    def get_max_length_for_unsigned_arr(cls, arr, k):
        if not arr or k < 0:
            return 0
        length = len(arr)
        # 子数组的左右边界
        left = 0
        right = 0
        total = arr[0]
        max_len = 0
        while right < length:
            # 当前子数组的和等于k时
            if total == k:
                # 因为都是正数 所以arr[left, i(i>right)]的子数组和肯定大于k。此时使left从左边重新开始找子数组
                max_len = max(max_len, right-left+1)
                total -= arr[left]
                left += 1
            # 当前子数组的和小于k时
            elif total < k:
                # 需要left不动  right+1
                right += 1
                if right == length:
                    break
                total += arr[right]
            # 当前子数组的和大于k时
            else:
                # 因为都是正数 所以arr[left, i(i>right)]的子数组和肯定大于k。此时使left从左边重新开始找子数组
                total -= arr[left]
                left += 1
        return max_len

if __name__ == '__main__':
    cur_arr = [1,2,1,1,1]
    print(MaxLength.get_max_length_for_unsigned_arr(cur_arr, 3))