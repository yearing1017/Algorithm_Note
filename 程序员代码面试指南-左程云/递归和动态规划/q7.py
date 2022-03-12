"""
问题描述：给定数组arr,返回arr的最长递增子序列。比如
arr=[2, 1, 5, 3, 6, 4, 8, 9, 7],返回的最长递增子序列为[1, 3, 4, 8, 9]

要求：如果arr长度为N,请实现时间复杂度为O(NlogN)的方法
"""


class MaxSubSeq:
    @classmethod
    def find_dp_way_1(cls, arr):
        """复杂度为O(N^2)"""
        # dp[i] 代表以arr[i]结尾时，arr[0...i]中的最大递增子序列长度
        dp = [1 for _ in range(len(arr))]

        for i in range(len(arr)):
            for j in range(i):
                if arr[j] < arr[i]:
                    # 计算到位置i时，找一个倒数第二个数字 使得长度更长
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp


    @classmethod
    def get_res_list_1(cls, arr):
        if not arr:
            return

        dp = cls.find_dp_way_1(arr)
        return cls.common_compute_with_dic(arr, dp)

    # 不考虑优先输出字典序小的
    @classmethod
    def common_compute_no_dic(cls, arr, dp):
        max_len = max(dp)
        index = 0
        for ind, value in enumerate(dp):
            if value == max_len:
                index = ind
                break

        res = list()
        temp = index
        res.insert(0, arr[index])
        while temp >= 0:
            if arr[temp] < arr[index] and dp[temp] == dp[index] - 1:
                res.insert(0, arr[temp])
                index = temp
            temp -= 1

        return res

    # 优先输出字典序小的序列：因为此题是最长的递增子序列 像 12864中 124为字典序最小的 
    # 不用判断 大小 只需倒序先找到最长的就行 因为后面的数如果大于前面的数 也就不会出现长度一样的事了 例如 12899
    @classmethod
    def common_compute_with_dic(cls, arr, dp):
        max_len = 0
        index = 0
        # 倒序找到第一次出现最大值的index
        for i in range(len(dp)-1, -1, -1):
            if dp[i] > max_len:
                max_len = dp[i]
                index = i

        res = list()
        temp = index
        res.insert(0, arr[index])
        while temp>=0:
            # 依次倒序找到最先出现符合条件的值 加入结果 若再碰见 continue
            if arr[temp] < arr[index] and dp[temp] == dp[index] -1:
                res.insert(0, arr[temp])
                index = temp
            temp -= 1
        return res

    @classmethod
    # 方法二优化了方法一中的 两个循环 采用二分查找的思路建立dp
    def get_res_list_2(cls, arr):
        if not arr:
            return

        dp = cls.find_dp_way_2(arr)
        return cls.common_compute_with_dic(arr, dp)

    @classmethod
    def find_dp_way_2(cls, arr):
        dp = [0 for _ in range(len(arr))]
        # ends[b] == c 代表遍历到目前 所有长度为b+1的递增序列的最小结尾数为c
        ends = [0 for _ in range(len(arr))]
        # 初始化
        ends[0] = arr[0]
        dp[0] = 1
        # ends[0...right] 为有效区
        right = 0
        # 依次遍历
        for i in range(1, len(arr)):
            l = 0
            r = right
            # 二分查找 此时ends中大于等于arr[i]的数
            # 二分查找时 找大于等于target的数，若找到 l为当时的位置 若找不到 l为数组的最后一个数的位置+1
            #二分查找时 找小于等于target的数，若找到 r为当时的位置 若找不到 r为数组的第一个数的位置-1
            while l <= r:
                m = int((l + r)/2)
                if arr[i] > ends[m]:
                    l = m + 1
                else:
                    r = m - 1
            # 若没找到 说明都小于arr[i] 则此时ends 应该扩大1 dp[i]=ends大小 在二分查找中l会一直右移 直到l =r+1
            # 若找到了 则有效区不变 替换 找到的数 dp[i]=替换数的dp+1
            right = max([l, right])
            ends[l] = arr[i]
            dp[i] = l + 1
        return dp

    

if __name__ == '__main__':
    print(MaxSubSeq.get_res_list_1([1,2,8,6,4,4,3]))
    print(MaxSubSeq.get_res_list_2([1,2,8,6,4,4,3]))