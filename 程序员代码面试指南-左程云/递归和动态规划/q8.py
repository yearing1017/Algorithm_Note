# 信封嵌套问题

'''
给n个信封的长度和宽度。如果信封A的长和宽都小于信封B，那么信封A可以放到信封B里，请求出信封最多可以嵌套多少层。
例如：[[3,4],[2,3],[4,5],[1,3],[2,2],[3,6],[1,2],[3,2],[2,4]] 返回 4
从里到外分别是{1，2}，{2，3}，{3，4}，{4，5}。

思路：
# 将信封的长度按从小到大顺序、当长度相等时，宽度安照从大到小的顺序排列
接下来此问题 可忽略长度 只看宽度数组，找到宽度的最长递增子序列即可
假设信封x位于排序后的某个位置，求出必须以x作为最外面信封的情况下，最多套几层
1. x之后的信封肯定不行，长度都大
2. x之前的 长度大于等于：
    2.1 若 x之前的信封长度小于x。那么只要前面的宽度也小于x即可 即：以x的宽度作为最后一个数，宽度数组的最长递增子序列
    2.2 若 x之前的信封长度等于x。长度相等的安照宽度从大到小排列，所以这些信封的宽度一定大于等于x的宽度，这样就不可能是当x的宽度作为最后一个数，宽度数组的最长递增子序列的一部分
所以：只需求x的宽度作为最后一个数的情况下，宽度数组的最长递增子序列
'''


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param letters int二维数组 
# @return int
#
class Solution:
    def maxLetters(self , letters ):
        # write code here
        # x表示letters中的元组，x[0]表示安照元组里的第一个元素升序排序，-x[1]当第一个元素相等时按照第二个元素降序 
        letters.sort(key=lambda x:(x[0],-x[1]))
        ends = [1 for _ in range(len(letters))]
        ends[0] = letters[0][1]
        right = 0
        l = 0
        r = 0
        m = 0
        # 基于二分查找 找到宽度数组的最长递增子序列的长度
        for i in range(1,len(letters)):
            l = 0
            r = right
            while l<=r:
                m = (l+r)//2
                if letters[i][1] > ends[m]:
                    l = m+1
                else:
                    r = m-1
            right = max(right, l)
            ends[l] = letters[i][1]
        return right + 1

    # 超时
    def maxEnvelopes(self, arr: List[List[int]]) -> int:
        n = len(arr)
        arr.sort(key=lambda x: (x[0], -x[1]))
        nums = [i[1] for i in arr]
        dp = [1] * n
        res = 0
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        return res