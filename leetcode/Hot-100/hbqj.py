"""
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
例如：
    输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
    输出：[[1,6],[8,10],[15,18]]
    解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 先按照每个单个区间的左端点升序排列
        intervals.sort(k=lambda x: x[0])
        # 依次遍历当前区间和 merged 的最后一个区间的右端点
        merged = []
        for interval in intervals:
            # 如果列表为空 或 当前区间 与 上一区间 不重合 则 直接加入
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 合并
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged