'''
给出两个有序的整数数组A和B，请将数组B合并到数组A中，变成一个有序的数组
注意：
可以假设A数组有足够的空间存放B数组的元素， A和B中初始的元素数目分别为m和n 
'''

def merge(self , A, m, B, n):
    a = m-1
    b = n-1
    # A的空间足够大，开辟m+n的空间，倒序比较
    for i in range(m+n-1, -1, -1):
        # 使用A的数来填的情况：B空了 或者 A没空 且A的当前值大于等于B的值
        if b <0 or (a>0 and A[a] >= B[b]):
            A[i] = A[a]
            a -= 1
        # 使用B的数来填的情况：a空了 或者 B没空 且B的当前值大于等于A的值
        else:
            A[i] = B[b]
            b -= 1
    return A
