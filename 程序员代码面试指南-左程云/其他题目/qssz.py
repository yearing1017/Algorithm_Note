'''
从0,1,2,...,n这n+1个数中选择n个数，找出这n个数中缺失的那个数，要求O(n)尽可能小。
例如：[0,1,2,3,4,5,7] ---》 6
'''

class Solution:
    def solve(self , a ):
        l = 0
        r = len(a) - 1
        while l<=r:
            mid = (l+r) // 2
            # 索引值==数值，说明左半区正确
            if a[mid] == mid:
                l = mid + 1
            else:
                r = mid - 1
        return l