class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if tinput is None:
            return []
        if k > len(tinput): 
            return []
        n = len(tinput)-1
        return self.quick_sort(tinput, 0, n)
    def quick_sort(self, tinput, left, right):
        if left > right:
            return
        l = left
        r = right
        pivot = tinput[l]
        while l < r:
            while l < r and tinput[r] >= pivot:
                r -= 1
            tinput[l] = tinput[r]
            while l <r and tinput[l] <= pivot:
                l += 1
            tinput[r] = tinput[l]
        tinput[l] = pivot
        self.quick_sort(tinput, left, l-1)
        self.quick_sort(tinput, l+1, right)
        if k == l:
            return tinput[:k]
        elif k < l:
            return self.quick_sort(tinput, left, l-1)
        else:
            return self.quick_sort(tinput, l+1, right)

if __name__ == '__main__':
    arr = [4,5,1,6,2,7,3,8]
    k = 4
    s = Solution()
    print(s.GetLeastNumbers_Solution(arr, k))
    print(arr)
