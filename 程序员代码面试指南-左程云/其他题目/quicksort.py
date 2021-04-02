class Solution:
    def MySort(self , arr ):
        # write code here
        left = 0
        right = len(arr) - 1
        return self.quick_sort(arr, left, right)
    def quick_sort(self, arr, left, right):
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
        self.quick_sort(arr, left, l-1)
        self.quick_sort(arr, l+1, right)
        return arr

if __name__ == '__main__':
    solve = Solution()
    input_list = [6, 4, 8, 9, 2, 3, 1]
    print('排序前:', input_list)
    sorted_list = solve.MySort(input_list)
    print('排序后:', sorted_list)