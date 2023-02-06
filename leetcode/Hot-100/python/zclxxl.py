"""
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
进阶：你可以设计并实现时间复杂度为 O(n) 的解决方案吗？
例如：
    输入：nums = [100,4,200,1,3,2]
    输出：4
    解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        # key是nums[i] val是该数所在序列的最长长度 例如[2,3,4,5] dic[4] = 4
        dic = dict() 
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
                # 检查 nums[i] - 1 和 +1
                if nums[i] - 1 in dic:
                    # 根据读取该符合题意序列的长度，将该数代表的长度修改为最长的
                    max_len = max(max_len, self.merge(dic, nums[i]-1, nums[i]))
                if nums[i] + 1 in dic:
                    max_len = max(max_len, self.merge(dic, nums[i], nums[i]+1))
    # 负责将该数左边连续的数和右边连续的数合并进来
    def merge(self, dic, less, more):
        # left 代表 less所在序列的左边界 最小值 例如：[2,3,4,5] 5-4+1 = 2
        left = less - dic[less] + 1
        # right 代表 more所在序列的右边界 最大值     [6,7,8,9] 6+4-1 = 9
        right = more + dic[more] - 1
        # 求 此时 left和right 所在最长序列的长度
        cur_len = right - left + 1
        # 更新此时left和right的长度
        dic[left] = cur_len
        dic[right] = cur_len
        return cur_len


class Solution2:
    def MLS(self , arr ):
        # leetcode上会超时
        # 方法1  找起始数 再从起始数开始找最长的序列
        arr = set(arr)
        res = 0
        for num in arr:
            if num - 1 in arr:
                continue
            # 找到最长序列的起始数
            start = num
            while start in arr:
                start += 1
            res = max(res, start - num)
        return res

class Solution3:
    def longestConsecutive(self, nums: List[int]) -> int:
      
        hash_dict = dict()
        # key是数  value是该数所在序列的最长长度
        max_length = 0
        for num in nums:
            if num not in hash_dict:
                left = hash_dict.get(num - 1, 0)
                right = hash_dict.get(num + 1, 0)
                
                cur_length = 1 + left + right
                if cur_length > max_length:
                    max_length = cur_length
                
                hash_dict[num] = cur_length
                hash_dict[num - left] = cur_length
                hash_dict[num + right] = cur_length
                
        return max_length