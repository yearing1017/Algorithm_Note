# 统计一个数字在升序数组中出现的次数
# 例如 [1,2,3,3,3,3,4,5],3  返回4
def GetNumberOfK(data, k):
    low = getlow(data,k)
    high = gethigh(data,k)
    return low - high + 1

def getlow(data, k):
    l = 0
    r = len(data) - 1
    while l <= r:
        mid = (l+r) // 2
        if data[mid] < k:
            l = mid +1
        else:
            r = mid - 1
    return l

def gethigh(data, k):
    l = 0
    r = len(data) - 1
    while l <= r:
        mid = (l+r)//2
        if data[mid]<=k:
            l = mid+1
        else:
            r = mid-1
    return r