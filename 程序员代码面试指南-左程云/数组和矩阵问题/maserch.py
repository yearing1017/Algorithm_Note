'''
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
解题思路：
    若将矩阵每一行拼接在上一行的末尾，则会得到一个升序数组，我们可以在该数组上二分找到目标元素。
    代码实现时，可以二分升序数组的下标，将其映射到原矩阵的行和列上。
    行坐标 mid // 每行元素个数；列坐标 mid % 每行元素个数
'''
def searchMatrix(self, matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    l = 0
    r = n*m -1
    while l <=r:
        mid = (l+r) // 2
        # 行坐标 mid // 每行元素个数；列坐标 mid % 每行元素个数
        cur = matrix[mid//n][mid%n]
        if cur == target:
            return True
        elif cur < target:
            l = mid + 1
        else:
            r = mid - 1
    return False