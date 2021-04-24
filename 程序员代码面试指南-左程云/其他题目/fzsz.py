'''
将给出的32位整数x翻转。
例1:x=123，返回321
例2:x=-123，返回-321
'''
class Solution:
    def reverse(self , x ):
        res = 0
        f = 1
        if x < 0:
            f = -1
            x = -x
        while x:
            res = res*10 + x%10
            x = x // 10
        return res * f