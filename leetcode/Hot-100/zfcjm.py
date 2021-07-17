"""
给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的
此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
例如：
    输入：s = "3[a]2[bc]"
    输出："aaabcbc"
    输入：s = "3[a2[c]]"
    输出："accaccacc"
"""
class Solution:
    def decodeString(self, s: str) -> str:
        # 分别考虑 数字 [ ] 字母 四种情况  
        stack = []
        # 每次遇到的新数字
        multi = 0
        res = ''
        # 分解因式  每段每段的运算
        for i in s:
            # 左括号：说明遇到了新的一个字母序列  先保存上一个运算好的序列 再需要重置res为空 以保存新的这个序列
            if i == '[':
                # multi 表示当前最新的数字 res表示 该数字之前的运算结果
                stack.append(multi, res)
                res = ''
                multi = 0
            # 右括号：说明这段运算需要结束 提取之前保存的上段的结果 加上这段的新的 multi * res
            elif i == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif i >= '0' and i <= '9':
                # 遇到数字 要考虑是否是多位的数字
                multi = multi*10 + int(i)
            else:
                # 遇到字母 链接到res
                res += i
        return res


