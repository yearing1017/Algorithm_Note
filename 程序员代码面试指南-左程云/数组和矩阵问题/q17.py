# -*- coding: utf-8 -*-

"""
问题描述:给定一个矩阵matrix,其中的值有正、负和0,返回子矩阵的最大累加和.

例如,矩阵matrix为
-90  48  78
64   -40 64
-81  -7  66
其中,最大累加和的子矩阵为:
48  78
-40 64
-7  66
所以返回累加和209.

例如,matrix为:
-1  -1  -1
-1  2   2
-1  -1  -1

其中,最大累加和的子矩阵为:
2  2
所以返回累加和为4.
"""

import sys

class MaxMatrixSum:
    @classmethod
    def get_max_sum(cls, matrix):
        if not matrix or not len(matrix) or not len(matrix[0]):
            return 0
        
        max_val = -sys.maxsize
        cur = 0
        # 依次遍历每行开始的子矩阵    每次将多行的数字按列相加   求该数组的最大值
        for i in range(len(matrix)):
            # 累加数组
            s = [0] * len(matrix[0])
            for j in range(i, len(matrix)):
                cur = 0
                for k in range(len(matrix[0])):
                    s[k] += matrix[j][k]
                    cur += s[k]
                    max_val = max(max_val, cur)
                    cur = 0 if cur < 0 else cur
        
        return max_val

if __name__ == '__main__':
    my_matrix = [
        [-90, 48, 78],
        [64, -40, 64],
        [-81, -7, 66]
    ]

    print(MaxMatrixSum.get_max_sum(my_matrix))
