'''
给出一个转动过的有序数组，你事先不知道该数组转动了多少
(例如,0 1 2 4 5 6 7可能变为4 5 6 7 0 1 2).
在数组中搜索给出的目标值，如果能在数组中找到，返回它的索引，否则返回-1。
假设数组中不存在重复项。
'''
class Solution:
    def search(self , arr , target ):
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = (l+r)//2
            if arr[mid] == target:
                return mid
            # 左半区
            if arr[mid] > arr[r]:
                if arr[l] <= target <= arr[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if arr[mid] <= target <= arr[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1