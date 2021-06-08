# -*- coding: utf-8 -*-
"""
问题描述:定义局部最小的概念。
1. arr长度为1时,arr[0]是局部最小。
arr长度为N(N>1)时，
2. 如果arr[0]<arr[1],那么arr[0]是局部最小;
3. 如果arr[N-1]<arr[N-2],那么arr[N-1]是局部最小;
4. 如果0<i<N-1,既有arr[i]<arr[i-1],又有arr[i]<arr[i+1],那么arr[i]是局部最小。
给定一个无序数组arr,已知arr中任意两个相邻的数都不相等。写一个函数,只需返回arr中任意
一个局部最小出现的位置即可。
"""
class LocalMinValue:
    @classmethod
    def get_local_min_value(cls, arr):
        # 首先判断给定的情况
        if not arr:
            return -1
        if len(arr) == 1 or arr[0] < arr[1]:
            return 0
        if arr[-1] < arr[-2]:
            return len(arr) - 1
        # 二分查找
        left = 1
        right = len(arr) - 2
        while left < right:
            mid = (left + right) // 2
            # mid > mid-1 说明左边肯定存在局部最小位置 
            if arr[mid] > arr[mid - 1]:
                right = mid - 1
            # mid > mid+1 说明右边肯定存在局部最小位置
            elif arr[mid] > arr[mid + 1]:
                left = mid + 1
            else:
                return mid
        return left

if __name__ == '__main__':
    my_arr = [6, 5, 3, 4, 6, 7, 8]
    print(LocalMinValue.get_local_min_value(my_arr))