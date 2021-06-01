# -*- coding: utf-8 -*-

"""
问题描述:给定一个矩阵,大小是N*N,把这个矩阵调整成顺时针转动90度后的形式。

例如:
１　２　３　４
５　６　７　８
9  10 11 12
13 14 15 16

顺时针转动90度,为:
13  9  5  1
14  10 6  2
15  11 7  3
16  12 8  4
"""

def rotateMatrix(mat, n):
    # 水平翻转
    for i in range(n//2):
        for j in range(n):
            mat[i][j], mat[n-i-1][j] = mat[n-i-1][j], mat[i][j]
    # 主对角线翻转
    for i in range(n):
        for j in range(i):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    return mat

if __name__ == '__main__':
    arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print(rotateMatrix(arr, 4))