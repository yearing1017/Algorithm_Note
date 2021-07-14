"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
要求：必须在原数组上操作，不能拷贝额外的数组
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        left = 0
        right = 0
        n = len(nums)
        for i in range(n):
            if nums[right] != 0:
                # left指向左边非0数的末尾
                # right指向右边全是0的首位
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
        '''
        n = len(nums)
        j = 0
        # 将所有非0的全挪到左边 强行赋值
        for i in range(n):
            if nums[i]:
                nums[j] = nums[i]
                j += 1
        # j 指向 非0 的最后一个数的下标
        for i in range(j, n):
            nums[i] = 0