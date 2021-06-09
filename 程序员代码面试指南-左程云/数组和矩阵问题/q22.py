# -*- coding: utf-8 -*-
"""
问题描述:给定一个整型数组arr,返回不包含本位置值的累乘数组.

例如:
arr=[2, 3, 1, 4],它的累乘数组是[12, 8, 24, 6]

要求:
1.时间复杂度为O(N)
2.除需要返回的结果数组外,额外空间复杂度为O(1)

"""

class ArrProduct:
    @classmethod
    def get_product_by_div(cls, arr):
        if not arr or len(arr) < 2:
            return
        
        all_value = 1
        res = [0 for _ in range(len(arr))]
        count = 0
        # 统计0的个数
        for i in range(len(arr)):
            if arr[i] == 0:
                count += 1
                zero_index = i
            else:
                all_value = arr[i] * all_value
        if count > 1:
            # pass 不做任何事情，一般用做占位语句
            pass
        elif count == 1:
            res[zero_index] = all_value
        else:
            for i in range(len(arr)):
                res[i] = int(all_value / arr[i])
        return res

if __name__ == '__main__':
    my_arr = [1, 2, 3, 4]
    print(ArrProduct.get_product_by_div(my_arr))


