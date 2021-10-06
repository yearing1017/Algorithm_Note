# 统计一个数字在升序数组中出现的起始下标
# 例如 [1,2,3,3,3,3,4,5],3  返回[2, 5]

def search(data, k):
    low = getlow(data,k)
    high = gethigh(data,k)
    if not 0 <= low < len(data) or not 0 <= high < len(data):
        return [-1, -1]
    elif data[low] != k or data[high] != k:
        return[-1, -1]
    else:
        return [low, high]

# 获取到 target第一次出现的下标 若数字大于最大的 则返回len(nums)
def getlow(data, k):
    l = 0
    r = len(data) - 1
    while l <= r:
        mid = (l+r) // 2
        if data[mid] < k:
            l = mid + 1
        else:
            r = mid - 1
    return l

# 获取到 target最后一次出现的下标 若数字小于最小的 则返回-1
def gethigh(data, k):
    l = 0
    r = len(data) - 1
    while l <= r:
        mid = (l+r)//2
        if data[mid] <= k:
            l = mid + 1
        else:
            r = mid - 1
    return r

nums = [1,2,3,3,3,3,3,3,5,6]
k = 4
print(search(nums, k))