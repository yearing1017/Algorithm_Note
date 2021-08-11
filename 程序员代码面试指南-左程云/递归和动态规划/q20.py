"""
问题描述：给定无序数组arr,返回其中最长的连续序列的长度。

举例：
arr=[100, 4, 200, 1, 3, 2]，最长的连续序列为[1, 2, 3, 4]，所以返回4
"""

class LongestSeq:
    @classmethod
    def get_longest_sequce_from_arr1(cls, arr):
        # 方法1  找起始数 再从起始数开始找最长的序列
        arr = set(arr)
        res = 0
        for num in arr:
            if num - 1 in arr:
                continue
            # 找到最长序列的起始数
            start = num
            while start in arr:
                start += 1
            res = max(res, start - num)
        return res

    
    @classmethod
    def get_longest_sequce_from_arr2(cls, nums):
        hash_dict = dict()
        # key是数  value是该数所在序列的最长长度
        max_length = 0
        for num in nums:
            if num not in hash_dict:
                left = hash_dict.get(num - 1, 0)
                right = hash_dict.get(num + 1, 0)
                
                cur_length = 1 + left + right
                if cur_length > max_length:
                    max_length = cur_length
                
                hash_dict[num] = cur_length
                hash_dict[num - left] = cur_length
                hash_dict[num + right] = cur_length
                
        return max_length


    @classmethod
    def get_longest_sequce_from_arr(cls, arr):
        if not arr:
            return 0
        max_len = 1
        dic = dict() # key代表arr[i] val 代表这个数所在序列的最长长度
        for i in range(len(arr)):
            # 只处理没出现过的数
            if arr[i] not in dic:
                dic[arr[i]] = 1
                if arr[i] - 1 in dic:
                    max_len = max(max_len, cls.merge(dic, arr[i]-1, arr[i]))
                if arr[i] + 1 in dic:
                    max_len = max(max_len, cls.merge(dic, arr[i], arr[i] + 1))
        return max_len
    @classmethod
    def merge(cls, dic, less, more):
        # 此处的left和right代表求出less所在序列的最小值 more所在序列的最大值
        left = less - dic[less] + 1
        right = more + dic[more] - 1
        length = right - left + 1
        # 更新最小值和最大值对应的长度
        dic[left] = length
        dic[right] = length
        return length

    

if __name__ == '__main__':
    print(LongestSeq.get_longest_sequce_from_arr([100, 4, 200, 1, 3, 2]))