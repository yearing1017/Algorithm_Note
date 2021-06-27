"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
例如：
    输入：digits = "23"
    输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
    输入：digits = ""
    输出：[]
    输入：digits = "2"
    输出：["a","b","c"]
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        # 存下数字对应的字母
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        temp = []
        # 递归函数 index代表当前遍历到第几个数字了
        def bs(index):
            if index == len(digits):
                # 当前结果可加入到最终结果中  转为字符串
                res.append(''.join(temp))
            else:
                num = digits[index]
                for s in phoneMap[num]:
                    temp.append(s)
                    # 递归遍历下一个数字对应的字母组合
                    bs(index+1)
                    # 回溯 弹出当前的数字对应的尾部字母 
                    temp.pop()
        bs(0)
        return res

