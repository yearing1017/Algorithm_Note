class Solution:
    def maxArea(self, height: List[int]) -> int:
        # O(N) O(1)
        i = 0
        j = len(height) -1
        res = 0
        # 每次的面积大小都由短板决定
        while i < j:
            # 每次向内收缩短板 面积才有可能扩大 收缩长板 短板大小可能不变可能减少
            if height[i] < height[j]:
                res = max(res, height[i]*(j-i))
                i += 1
            else:
                res = max(res, height[j]*(j-i))
                j -= 1
        return res