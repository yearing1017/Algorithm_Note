"""
问题描述：给定一个字符串数组strs，再给定两个字符串str1和str2,返回在strs中
str1与str2的最小距离，如果str1或者str2为null，或不在strs中，返回-1.

举例：
strs=['1', '3', '3'， '3'， '2'， '3'， '1'],str1='1'，str2='2'，返回2
strs=['CD'],str1='CD',str2='AB'，返回-1

进阶题目：
如果查询发生的次数有很多，如何把每次查询的时间复杂度降为O(1)
"""


import sys


class ShortestDistance:
    @classmethod
    def find_short_distance(cls, strs, str1, str2):
        if not strs or not str1 or not str2 or str1 not in strs or str2 not in strs:
            return -1

        if str1 == str2:
            return 0

        last_index1 = -1 # str1最近一次出现的位置
        last_index2 = -1 # str2最近一次出现的位置
        min_value = sys.maxsize

        index = 0
        while index < len(strs):
            if strs[index] == str1:
                if last_index2 == -1:
                    pass
                else:
                    # i- last2的值时当前的str1和它左边离它最近的str2的距离
                    min_value = min([index - last_index2, min_value])
                last_index1 = index

            if strs[index] == str2:
                if last_index1 == -1:
                    pass
                else:
                    #- last1的值时当前的str2和它左边离它最近的str1的距离
                    min_value = min([index - last_index1, min_value])
                last_index2 = index
            index += 1

        return min_value if min_value != sys.maxsize else -1

    # 进阶问题
    