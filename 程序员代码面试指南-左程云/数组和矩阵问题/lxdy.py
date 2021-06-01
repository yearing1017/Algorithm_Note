# -*- coding: utf-8 -*-
"""
问题描述:给定一个矩阵matrix,请按照转圈的方式打印它。

例如：
1  2  3  4
5  6  7  8
9  10 11 12
13 14 15 16

打印结果为:
1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10
"""
class Solution:
    @classmethod
    def spiralOrder(self , matrix):
        res = []
        if not matrix: return res
        l, r, t, b = 0, len(matrix[0])-1, 0, len(matrix)-1
        while True:
            # left to right
            for i in range(l, r+1): res.append(matrix[t][i])
            t += 1
            if t > b: break
            # top to bottom
            for i in range(t, b+1): res.append(matrix[i][r])
            r -= 1
            if r < l: break
            # right to left
            for i in range(r, l-1, -1): res.append(matrix[b][i])
            b -= 1
            if b < t: break
            # bottom to top
            for i in range(b, t-1, -1): res.append(matrix[i][l])
            l += 1
            if l > r: break
        return res

if __name__ == '__main__':
    arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print(Solution.spiralOrder(arr))