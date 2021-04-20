# 顺时针旋转矩阵90度
def rotateMatrix(self, mat, n):
    # 水平翻转
    for i in range(n//2):
        for j in range(n):
            mat[i][j], mat[n - i - 1][j] = mat[n-i-1][j], mat[i][j]
    # 主对角线翻转
    for i in range(n):
        for j in range(i):
            mat[i][j], mat[j][i] = mat[i][j], mat[j][i]
    return mat