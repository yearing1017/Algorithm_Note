'''
给定一个数组，满足2 * A[i] < A[i+1]，给定target，判断数组A中是否存在两个数，a，b使得，a + b = target
如存在，返回true，不存在，返回false。 e.g.  A = [1, 4, 9, 21, 48, 112], target = 52，返回true。
'''

def twoSum(nums, target):
    i = 0
    j = len(nums) - 1

    while i <= j:
        m = (i + j) // 2
        if nums[m] < target:
            i = m + 1
            if i >= len(nums) and target > 2 * nums[-1]:
                return False
        else:
            j = m - 1
            if j <= 0:
                return False
    # j代表 第一个不等于target 且 最接近的数的 下标
    max_val = nums[j]

    if max_val < target // 2:
        return False

    i = 0
    while i <= j:
        m = (i + j) // 2
        if nums[m] == target - max_val:
            return True
        elif nums[m] < target - max_val:
            i = m + 1
        else:
            j = m - 1
    return False

nums = (1,3,7,15,31,63)
print(twoSum(nums, 46))