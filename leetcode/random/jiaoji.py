'''
给定两个数组，编写一个函数来计算它们的交集
 输入：nums1 = [1,2,2,1], nums2 = [2,2]
 输出：[2]
若数组是有序的，不用排序即可
'''
class Solution:
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        
        left = 0
        right = 0

        res = []

        while left < len(nums1) and right < len(nums2):
            if nums1[left] < nums2[right]:
                left += 1
            elif nums1[left] == nums2[right]:
                if nums1[left] not in res:
                    res.append(nums1[left])
                left += 1
                right += 1
            else:
                right += 1

        return res