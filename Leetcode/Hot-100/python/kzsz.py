"""
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
例如：
    输入:nums = [1,1,1], k = 2
    输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
"""

class Solution:
    def subarraySum(self, nums, k):
        # 前缀和字典 代表该和对应的数量
        preSumDic = {0:1}
        cur_sum = 0
        count = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            # 判断 curcur_sum - k 是否在前缀和字典中 若在 说明 有子数组和为kk
            if cur_sum - k in preSumDic:
                count += preSumDic[cur_sum - k]
            # 没有 则添加1  有 就更新; 
            preSumDic[cur_sum] = preSumDic.get(cur_sum, 0) + 1
            # 这样就会把所有子数组的前缀和 添加进来  只有curcur_sum - k存在 则存在几个和为k的子数组
        return preSumDic, count

if __name__ == '__main__':
    nums = [1,2,3,2]
    k = 3
    slove = Solution()
    dic, cnt = slove.subarraySum(nums, k)
    print(dic)
    print(cnt)
