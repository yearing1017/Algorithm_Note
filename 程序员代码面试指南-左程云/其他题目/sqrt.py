class Solution:
    def sqrt(self , x ):
        # write code here
        if x<=1: return x
        left=0
        right=x
        res = 0
        while left <= right:
            mid = (left + right) // 2
            # x平方根是 k的平方 <= x 的 最大k值
            if mid * mid <= x:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res

