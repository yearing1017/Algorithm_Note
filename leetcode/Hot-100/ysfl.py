"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
例如：
    输入：nums = [2,0,2,1,1,0]
    输出：[0,0,1,1,2,2]
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        # 遍历将0全都交换到ptr的前面
        ptr = 0
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                # 交换之后 ptr 后移一位
                ptr += 1
        # 调整1
        for i in range(ptr, n):
            if nums[i] == 1:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                # 交换之后 ptr 后移一位
                ptr += 1