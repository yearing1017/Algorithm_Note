'''
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。

输入：nums = [1,2,0]
输出：3

输入：nums = [3,4,-1,1]
输出：2
'''



def firstMissingPositive(nums) -> int:
    size = len(nums)
    for i in range(size):
        # 先判断这个数字是不是索引，然后判断这个数字是不是放在了正确的地方
        while 1 <= nums[i] <= size and nums[i] != nums[nums[i] - 1]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    
    for i in range(size):
        if i + 1 != nums[i]:
            return i + 1
    # 像1234  返回5
    return size + 1

nums = [3, 4, -1, 1]
firstMissingPositive(nums)