'''
给定一个无序数组arr，找到数组中未出现的最小正整数
例如arr = [-1, 2, 3, 4]。返回1
arr = [1, 2, 3, 4]。返回5
[要求]
时间复杂度 O(N)  空间复杂度 O(1)
'''
# 由例子知：数组从1开始，数N应该在索引为N-1的位置上，例如4应该放在索引3位置上

class Solution:
    def minNumberdisappered(self, arr):
        for i in range(len(arr)):
            if 1 <= arr[i] <= len(arr) and arr[i] != arr[arr[i]-1]:
                # 原地置换
                arr[i], arr[arr[i]-1] = arr[arr[i]-1], arr[i]
            
        # 交换完判断
        for i in range(len(arr)):
            if i+1 != arr[i]:
                return i+1
        
        # 否则就是后面未出现的那个

        return len(arr) + 1
