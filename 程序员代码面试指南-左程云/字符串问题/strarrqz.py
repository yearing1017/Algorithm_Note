def longestCommonPrefix(self , strs ):
    if not strs:
        return ''
    pre = strs[0]
    for i in range(1, len(strs)):
        # 迭代查找
        pre = lcp(pre, strs[i])
        if not pre:
            break
    return pre

def lcp(self, str1, str2):
    min_len = min(len(str1), len(str2))
    index = 0
    while index < min_len and str1[index] == str2[index]:
        index += 1
    return str1[:index]