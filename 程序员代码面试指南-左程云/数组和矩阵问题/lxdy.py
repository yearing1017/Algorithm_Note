# 给定一个m x n大小的矩阵（m行，n列），按螺旋的顺序返回矩阵中的所有元素
class Solution:
    def spiralOrder(self , matrix ):
        res = []
        if not matrix: return res
        l, r, t, b = 0, len(matrix[0])-1, 0, len(matrix)-1
        while True:
            # 左到右
            for i in range(l, r+1): res.append(matrix[t][i])
            t += 1
            if t > b: break
            # 上到下
            for i in range(t, b+1): res.append(matrix[i][r])
            r -= 1
            if r < l: break
            # 右到左
            for i in range(r, l-1, -1): res.append(matrix[b][i])
            b -= 1
            if b < t: break
            # 下到上
            for i in range(b, t-1, -1): res.append(matrix[i][l])
            l += 1
            if l > r: break
        return res
