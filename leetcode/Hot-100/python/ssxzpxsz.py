"""
整数数组 nums 按升序排列，数组中的值互不相同 
在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了旋转
使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）
例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        # 没有= 会找不到某些数
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # 判断在左半区
            if nums[mid] > nums[r]:
                # 判断在左半区的左边
                if target >= nums[l] and target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # 判断在右半区
            else:
                # 判断在右半区的右边
                if target >= nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1