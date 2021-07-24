class Solution:
    
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if tinput is None:
            return []
        if k > len(tinput): 
            return []
        # 不加这个 当k == 该长度时  会输出none
        if k == len(arr):
            return arr
        n = len(tinput)-1
        return self.quick_sort(tinput, 0, n, k)
    def quick_sort(self, tinput, left, right, k):
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
        #self.quick_sort(tinput, left, l-1)
        #self.quick_sort(tinput, l+1, right)
        if k == l:
            return tinput[:k]
        elif k < l:
            return self.quick_sort(tinput, left, l-1, k)
        else:
            return self.quick_sort(tinput, l+1, right, k)
        

    '''
    def getLeastNumbers(self, arr, k):
        if arr is None or k > len(arr):
            return []
        if k == len(arr):
            return arr
        left = 0
        right = len(arr) - 1
        return self.quickSearch(left, right, arr, k)
        

    def quickSearch(self, left, right, arr, k):
        if left > right: return
        l = left
        r = right
        pivot = arr[l]
        while l < r:
            while l < r and arr[r] >= pivot:
                r -= 1
            arr[l] = arr[r]
            while l < r and arr[l] <= pivot:
                l += 1
            arr[r] = arr[l]
            
        arr[l] = pivot
        if k == l:
            return arr[:k]
        elif k < l:
            return self.quickSearch(left, l-1, arr, k)
        else:
            return self.quickSearch(l+1, right, arr, k)
    '''


if __name__ == '__main__':
    arr = [3,2,1]
    k = 3
    s = Solution()
    #print(s.getLeastNumbers(arr, k))
    print(s.GetLeastNumbers_Solution(arr, k))
    print(arr)
