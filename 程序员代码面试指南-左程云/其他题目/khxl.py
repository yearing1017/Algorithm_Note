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


def isValid(self , s ):
        # write code here
        dic = {'{':'}', '[':']', '(':')'}
        stack = []
        for a in s:
            # 遇到左括号 添加到栈中
            if a in dic:
                stack.append(a)
            else:
                #  遇到右括号 检测 栈顶是否与该右括号匹配
                if not stack or a!= dic[stack.pop()]:
                    return False
        return len(stack) == 0