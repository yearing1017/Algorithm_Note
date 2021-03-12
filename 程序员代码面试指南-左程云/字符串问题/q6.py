"""
问题描述：给定一个字符串数组strs[],在strs中有些位置为None，但在不为None的位置上，
其字符串是按照字典顺序由小到大依次出现的。再给定一个字符串str，请返回str在strs中出
现的最左的位置。

举例：
strs=[None, 'a', None, 'a', None, 'b', None, 'c']，str='a'，返回1.
strs=[None, 'a', None, 'a', None, 'b', None, 'c'], str=None,返回-1
strs=[None, 'a', None, 'a', None, 'b', None, 'c'], str='d',返回-1
"""

# 二分查找
class CharFinder:
    @classmethod
    def get_the_leftest_post(cls, strs, char):
        if not strs or char == None:
            return -1
        res = -1
        left = 0
        right = len(strs) - 1
        mid = 0
        i = 0
        while left <= right:
            mid = (left + right) //2
            # 1.中间值不空 and 等于str 先保存下来 再去找左边的
            if strs[mid] and strs[mid] == char:
                res = mid
                right = mid - 1
            # 2. 不空单不等于
            elif strs[mid]:
                if strs[mid] < char:
                    left = mid + 1
                else:
                    right = mid - 1
            # 3. 为空
            else:
                i = mid
                i -= 1
                while strs[i] is None and i>=left:
                    i -= 1
                if i < left or strs[i] < char:
                    left = mid + 1
                else:
                    if strs[i] == char:
                        res = i
                    right = i -1
        return res

if __name__ == '__main__':
    arr = [None, "a", None, "a", None, "b", None,
           None, None, "b", None, "c", None, "c", None, None, "d", None,
           None, None, None, None, "d", None, "e", None, None, "e", None,
           None, None, "f", None, "f", None]
    str1 = 'a'
    print(CharFinder.get_the_leftest_post(arr, str1))
    str2 = 'b'
    print(CharFinder.get_the_leftest_post(arr, str2))