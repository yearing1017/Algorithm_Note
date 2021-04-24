'''
给出一组区间，请合并所有重叠的区间。
请保证合并后的区间按区间起点升序排列。

例如：[[10,30],[20,60],[80,100],[150,180]] ---》 [[10,60],[80,100],[150,180]]
'''
# class Interval:
#     def __init__(self, a=0, b=0):
#         self.start = a
#         self.end = b
# @param intervals Interval类一维数组 
# @return Interval类一维数组
class Solution:
    def merge(self , intervals ):
        intervals.sort(key=lambda x: x.start)

        res = []
        for interval in intervals:
            if not res or res[-1].end < interval.start:
                res.append(interval)
            else:
                res[-1].end = max(res[-1].end, interval.end)
        return res
