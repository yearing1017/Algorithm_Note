"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
例如：
    输入：nums = [1,2,3]
    输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums:
            return res
        
        n = len(nums)
        # 标记该位置的数字已访问过
        vis = [0 for _ in range(n)]

        def helper(length, temp):
            if length == n:
                res.append(temp)
                return
            for i in range(n):
                if vis[i]:
                    continue
                # 标记访问过
                vis[i] = 1
                helper(length + 1, temp + [nums[i]])
                # 回溯 [1,2,3] -> [1,3,2]时，vis[1] vis[2] 都会回溯为0 但helper(2)的for循环会继续遍历nums[2]
                vis[i] = 0
            
        helper(0, [])
        return res