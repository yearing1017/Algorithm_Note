"""
问题描述：给定一个字符类型的数组chas，请在单词间做逆序调整。只要做到单词顺序逆序即可，
对空格的位置没有特殊要求。

举例：
如果把chas看做字符串为"dog loves pig"，调整成"pig loves dog".
如果把chas看做字符串为"I'm a student"，调整成"student a I'm".

补充题目：
给定一个字符类型的数组chas和一个整数size，请把大小为size的左半区整体移动到右半区，右半
区整体移动到左边。

举例：
如果把chas看做字符串"ABCDE",size=3,调整为"DEABC"

要求：
如果chas长度为N，两道题都要求时间复杂度为O(N)，额外空间复杂度为O(1).
"""


class StrRotation:
    # 逆序复制
    @classmethod
    def get_rotated_chas(cls, chas):
        if not chas:
            return

        num = 0 # 左半区的空格数
        length = 0 # 记录左半区多大

        while length < len(chas) and chas[length] != 0:
            if chas[length] == ' ':
                num += 1
            length += 1
        # 扩展之后的大小
        j = length + num*2 - 1
        for i in range(length -1, -1, -1):
            if chas[i] != ' ':
                chas[j] = chas[i]
                j -= 1
            else:
                chas[j] = '0'
                j-=1
                chas[j] = '2'
                j-=1
                chas[j] = '%'
                j-=1
        return chas

    @classmethod
    def modify(cls, chas):
        if not chas:
            return
        j = len(chas) - 1
        for i in range(len(chas)-1,-1,-1):
            if chas[i] != '*':
                chas[j] = chas[i]
                j -= 1
        while j >=0:
            chas[j] = '*'
            j-=1
        return chas
if __name__ == '__main__':
    #print(StrRotation.get_rotated_chas(['d', 'o', 'g', ' ', 'l', 'o', 'v', 'e', 's', ' ', 'p', 'i', 'g']))
    #print(StrRotation.rotate_by_size(['1', '2', '3', '4', '5', 'A', 'B', 'C'], 3))
    print(StrRotation.modify(['1','2','*','*','3','4','5']))