'''
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 快排思想 改为降序排序 每趟会找到一个位置，左边的数都小于它 右边的数都大于它
        n = len(nums)
        return self.quick_sort(nums, 0, n-1, k)

    def quick_sort(self, arr, left, right, k):
        # 递归终止条件
        if left > right: return
        l = left
        r = right
        pivot = arr[l]
        while l < r:
            while l < r and arr[r] <= pivot:
                r -= 1
            arr[l] = arr[r]

            while l < r and arr[l] >= pivot:
                l += 1
            arr[r] = arr[l]
        arr[l] = pivot
        if l == k-1:
            return arr[l]
        elif l < k-1:
            # 继续在右边遍历寻找
            return self.quick_sort(arr, l+1, right, k)
        else:
            return self.quick_sort(arr, left, l-1, k)
