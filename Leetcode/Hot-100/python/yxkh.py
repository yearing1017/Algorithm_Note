"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
例如：
    输入：s = "()[]{}"
    输出：true
    输入：s = "([)]"
    输出：false
"""
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(', ']':'[', '}':'{'}
        stack = []
        for i in s:
            # 左括号 则加入栈
            if i in dic.values():
                stack.append(i)
            else:
                # 右括号 则去匹配栈顶是否匹配
                if not stack or stack.pop() != dic[i]:
                    return False
        # 遍历完剩下元素 也不符合
        return len(stack) == 0
