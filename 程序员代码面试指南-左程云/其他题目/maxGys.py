'''
输入a和b 返回a和b的最大公约数
'''
class Solution:
    def gcd(self , a , b ):
        # 辗转相除法
        while b!= 0:
            result = a % b
            a = b
            b = result
        return a