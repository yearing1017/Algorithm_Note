"""
问题描述:给定一个数组arr,返回子数组的最大累加和.

例如:
arr=[1, -2, 3, 5, -2, 6, -1],所有的子数组中,[3, 5, -2, 6]可以累加出
最大的和12,所以返回12.

要求:
如果arr长度为N,要求时间复杂度为O(N),额外空间复杂度为O(1).
"""
import sys

class MaxSum:
    @classmethod
    def get_max_sum(cls, arr):
        if not arr or len(arr) == 0:
            return 0
        max_sum = -sys.maxsize -1
        cur = 0
        for i in range(len(arr)):
            cur += arr[i]
            max_sum = max(max_sum, cur)
            # 如果累加到当前值cur小于0，说明之前的这部分不能作为最大累加和的左部分，重置cur=0
            if cur < 0:
                cur = 0
        return max_sum

if __name__ == '__main__':
    my_arr = [1, -2, 3, 5, -2, 6, -1]
    print(MaxSum.get_max_sum(my_arr))