"""
给定n个非负整数表示每个宽度为1的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水
例如：
    输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
    输出：6
    解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0
        res = 0
        n = len(height)
        leftmax = height[0]
        rightmax = height[n-1]
        L = 1
        R = n-2
        while L <= R:
            if leftmax <= rightmax:
                # 左边的短 为阈值 求L位置的水
                res += max(0, leftmax - height[L])
                leftmax = max(leftmax, height[L])
                L += 1
            else:
                res += max(0, rightmax-height[R])
                rightmax = max(rightmax, height[R])
                R -= 1
        return res
