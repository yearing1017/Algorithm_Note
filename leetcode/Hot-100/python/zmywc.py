"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
例如：
    输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
    输出:
    [
        ["ate","eat","tea"],
        ["nat","tan"],
        ["bat"]
    ]
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 将字典的value设置为list形式
        #mp = collections.defaultdict(list)
        mp = dict()
        # 找字母异位词的相同点 即 排序之后 都一样 当做key value就是所求的列表
        for s in strs:
            key = ''.join(sorted(s))
            if key not in mp:
                mp[key] = []
                mp[key].append(s)
            else:
                mp[key].append(s)
        return list(mp.values())