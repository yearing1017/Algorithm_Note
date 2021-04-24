'''
山峰元素是指其值大于或等于左右相邻值的元素。
给定一个输入数组nums，任意两个相邻元素值不相等，数组可能包含多个山峰。找到索引最大的那个山峰元素并返回其索引。
假设 nums[-1] = nums[n] = -∞。
'''
class Solution:
    def solve(self , a):
        # 倒序先看尾部
        for i in range(len(a)-1, -1, -1):
            if i == len(a)-1 and a[i] > a[i-1]:
                return i
            elif i == 0 and a[i] > a[i+1]:
                return i
            else:
                if a[i-1] < a[i] and a[i]> a[i+1]:
                    return i
        return -1
