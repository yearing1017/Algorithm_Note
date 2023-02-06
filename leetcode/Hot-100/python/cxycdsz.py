"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
解法：
    异或运算
        任何数和 0 做异或运算，结果仍然是原来的数；
        任何数和其自身做异或运算，结果是 0
        异或运算满足交换律和结合律
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res