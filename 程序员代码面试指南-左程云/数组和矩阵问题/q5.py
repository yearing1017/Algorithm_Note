# -*- coding: utf-8 -*-

"""
给定一个无序数组arr,求出需要排序的最短子数组长度。
例如:
arr=[1, 5, 3, 4, 2, 6, 7],返回４,因为只有[5, 3, 2, 4]需要排序。
"""

def getMinLength(arr):
    if not arr or len(arr) < 2:
        return 0
    # 从左到右遍历 min记录右侧出现的数最小值  noMinIndex记录当前值arr[i]>min时 要想有序 必须替换的坐标位置
    minValue = arr[len(arr)-1]
    noMinIndex = -1
    for i in range(len(arr)-2, -1, -1):
        if arr[i] > minValue:
            noMinIndex = i
        else:
            minValue = min(minValue, arr[i])
    
    # 若noMinIndex = -1 说明右到左是升序的 直接返回
    if noMinIndex == -1:
        return 0

    # 从右到左遍历 max记录左侧出现的数的最大值  noMaxIndex记录当前值arr[i]<max时 要想有序 必须替换的坐标位置
    maxValue = arr[0]
    noMaxIndex = -1
    for i in range(1, len(arr)):
        if arr[i] < maxValue:
            noMaxIndex = i
        else:
            maxValue = max(arr[i], maxValue)
    return noMaxIndex - noMinIndex + 1 

if __name__ == '__main__':
    print(getMinLength([1, 5, 3, 4, 2, 6, 7]))