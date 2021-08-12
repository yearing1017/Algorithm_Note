# 两个矩阵乘法 

class Solution:
    def solve(self , a , b ):
        # write code here
        m = len(a)
        p = len(a[0])
        n = len(b[0])
        
        res = [[0 for _ in range(n)]for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                t = 0
                for k in range(p):
                    t += a[i][k] * b[k][j]
                res[i][j] = t
        return res