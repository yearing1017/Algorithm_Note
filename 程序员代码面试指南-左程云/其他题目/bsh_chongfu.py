'''
请实现有重复数字的升序数组的二分查找
给定一个 元素有序的（升序）整型数组 nums 和一个目标值 target ，
写一个函数搜索 nums 中的 target，如果目标值存在返回最先出现的下标，否则返回 -1
'''
def search(self , nums , target ):
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = (low+high) // 2
        if nums[mid] == target:
            while mid != 0 and nums[mid-1] == nums[mid]:
                mid -= 1
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid -1
    return -1