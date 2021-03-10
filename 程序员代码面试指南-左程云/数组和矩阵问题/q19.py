"""
问题描述:给定一个double类型的数组arr，其中的元素可正、可负、可0，返回子数组累乘的最大
乘积。

例如:
arr=[-2.5,4,0,3,0.5,8,-1],子数组[3,0.5,8]累乘可以获得最大的乘积12,所以返回12.
"""


class SubArrMaxSum:
    @classmethod
    def get_max_sum(cls, arr):
        if not arr:
            return 0
        # 以arr[i-1]结尾的最大类乘积
        max_val = arr[0]
        # 以arr[i-1]结尾的最小类乘积
        min_val = arr[0]
        res = arr[0]
        maxend = 0
        minend = 0
        # 使用以arr[i-1]结尾的最大类乘积 和 最小 来求arr[i]结尾的最大乘积
        for i in range(1, len(arr)):
            
            maxend = max_val * arr[i]
            minend = min_val * arr[i]
            # 最大值有三种可能
            max_val = max(maxend, minend, arr[i])
            # 最小值也有这三种
            min_val = min(maxend, minend, arr[i])
            
            res = max(res, max_val)
        return res

if __name__ == '__main__':
    my_arr = [-2.5, 4, 0, 3, 0.5, 8, -1]
    print(SubArrMaxSum.get_max_sum(my_arr))