'''
适用于区间为空、答案不存在、有重复元素、搜索开/闭的上/下界等情况
注意：左闭右开  左边界为数组第一个数的下标  右边界为数组个数
'''
def binaySearch(arr, key):
    left = 0
    right = len(arr)
    
    while left < right:
        mid = left + (right-left) // 2
        '''
        若不要求找到第一个满足条件的 即可加上这句
        if arr[mid] == key:
            return mid
        '''
        if arr[mid] < key:
            left = mid + 1
        else:
            right = mid
    return left #此代码 返回left和last都行

if __name__ == "__main__":
    arr = [1,2,2,2,3,3,3,4,4,5,6]
    res = binaySearch(arr, key=0)
    print(res)
