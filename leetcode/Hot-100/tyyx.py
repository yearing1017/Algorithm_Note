"""
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标
数组中的每个元素代表你在该位置可以跳跃的最大长度
判断你是否能够到达最后一个下标
例如：
    输入：nums = [2,3,1,1,4]
    输出：true
    解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 初始化能够到达的最远位置
        max_i = 0
        # for循环 一个一个点的判断
        for i in range(len(nums)):
            # 判断max_i是否可以达到 或 更远
            if max_i >=i and i + nums[i] >= max_i:
                max_i = i + nums[i]
        return max_i >= len(nums)-1

        """
        max_i = 0       #初始化当前能到达最远的位置
        for i, jump in enumerate(nums):   #i为当前位置，jump是当前位置的跳数
            if max_i>=i and i+jump>max_i:  #如果当前位置能到达，并且当前位置+跳数>最远位置  
                max_i = i+jump  #更新最远能到达位置
        return max_i>=i
        """·
