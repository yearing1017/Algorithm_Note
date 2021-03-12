
"""
问题描述：给定一个字符类型的数组chas[],chas右半区全是空字符，左半区不含空字符。
现在想将左半区中所有的空格字符替换成"%20",假设chas右半区足够大，可以满足替换所
需要的空间，请完成替换函数。

举例：
如果把chas的左半区看做字符串，为"a b  c"，假设chas的右半区足够大。替换后，chas
的左半区为"a%20%b%20%20c"

要求：
替换函数时间复杂度为O(N),额外空间复杂度为O(1)

补充题目：
给定一个字符类型的数组chas[],其中只含有数字字符和"*"。现在想把所有的"*"字符挪到
chas的左边，数字字符挪到chas的右边，请完成调整函数。

举例：
如果把chas看做字符串，为"12**345"，调整后chas为"**12345"

要求：
1.调整函数的时间复杂度为O(N)，额外空间复杂度为O(1)。
2.不得改变数字字符从左到右出现的顺序。
"""

class StrRotation:
    # 逆序复制
    @classmethod
    def get_rotated_chas(cls, chas):
        if not chas:
            return

        num = 0 # 左半区的空格数
        length = 0 # 记录左半区多大

        while length < len(chas) and chas[length] != '':
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
    print(StrRotation.get_rotated_chas(['a', ' ', 'b', ' ', ' ', 'c', '', '', '', '', '', '', '', '']))
    #print(StrRotation.rotate_by_size(['1', '2', '3', '4', '5', 'A', 'B', 'C'], 3))
    print(StrRotation.modify(['1','2','*','*','3','4','5']))