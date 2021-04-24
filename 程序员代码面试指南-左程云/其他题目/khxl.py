'''
给出一个仅包含字符'(',')','{','}','['和']',的字符串，判断给出的字符串是否是合法的括号序列
括号必须以正确的顺序关闭，"()"和"()[]{}"都是合法的括号序列，但"(]"和"([)]"不合法。
'''
def isValid(self , s):
    dic = {")":"(", "}":"{", "]":"["}
    stack = []
    for i in s:
        if i in dic.values():
            stack.append(i)
        else:
            if not stack or stack.pop() != dic[i]:
                return False
    return len(stack) == 0
