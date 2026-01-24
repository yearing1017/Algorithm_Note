"""
你是一个专业的小偷，计划偷窃沿街的房屋
每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警
给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额
例如：
    输入：[2,7,9,3,1]
    输出：12
    解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。偷窃到的最高金额 = 2 + 9 + 1 = 12 。
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        # dp[i] 代表有 i 间房，偷取到的最大利益
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        # 后续每个dp[i]的计算方法：比较dp[i-1](偷i-1) 和 dp[i-2]+nums[i]（不偷i-1）
        for i in range(2, n):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]

    # 优化空间 只用前两个元素即可
    def rob2(self, nums: List[int]) -> int:
        # 优化空间 只用前两个元素即可
        if not nums: return 0
        n = len(nums)
        
        prepre = 0
        pre = 0
        now = 0

        for i in range(n):
            now = max(prepre + nums[i], pre)
            prepre = pre
            pre = now
        return now
