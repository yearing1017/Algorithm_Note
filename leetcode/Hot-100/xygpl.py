"""
实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）
必须 原地 修改，只允许使用额外常数空间
例如：
    输入：nums = [1,2,3]
    输出：[1,3,2]
    输入：nums = [3,2,1]
    输出：[1,2,3]
    输入：nums = [1,1,5]
    输出：[1,5,1]
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        # 从后向前先找到第一个非降序的数字 例如：[4,5,2,6,3,1]中的2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        # 2的位置是2 在[3, 5]中找到第一个比2大的数字并交换
        if i >= 0:
            j = len(nums) - 1
            while j >=0  and nums[i] >= nums[j]:
                j -= 1
            # 交换找到的 较小数 与 较大数
            nums[i], nums[j] = nums[j], nums[i]
        # 区间 [i+1, n-1]必为降序  变为升序 即 [4,5,3,6,2,1] 改为[4,5,3,1,2,6]
        left = i + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1