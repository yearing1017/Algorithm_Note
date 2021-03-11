"""
问题描述:给定一个整型数组arr和一个大于１的整数k。已知arr中只有１个数出现了１次，
其它的数都出现了k次，请返回只出现了１次的数。

要求:
时间复杂度为O(N)，额外空间复杂度为O(1).

思路：
k个k进制的数，无进位相加。比如２个相同的二进制的数，无进位相加，结果一定为0
"""
class KGetter:
    @classmethod
    def once_num(cls,arr, k):
        e0 = [0 for _ in range(32)]
        for i in arr:
            # 依次转为32位的k进制数 并进行无进位相加 得到唯一出现1次的数
            cls.execute(e0, i, k)
        # 将k进制数转为10进制数
        print(e0)
        res = cls.ksys2num(e0, k)

        return res
    
    @classmethod
    def execute(cls, e0, value, k):
        cur_ksys = cls.num2ksys(value, k)
        # 无进位相加时每一位的结果
        for i in range(len(e0)):
            e0[i] = (e0[i] + cur_ksys[i]) % k

    @classmethod
    def num2ksys(cls, num, k):
        res = [0 for _ in range(32)]
        i = 0
        while num!=0:
            res[i] = num%k
            num = num // k
            i += 1
        return res # 是k进制的倒序  但无影响 对于无进位相加

    @classmethod
    def ksys2num(cls, e0, k):
        res = 0
        '''
        # k进制转为10进制的方法1 不好理解
        for i in range(len(e0)-1, -1, -1):
            res = res * k + e0[i]
            print(res, end=' ')
        '''
        for i in range(len(e0)):
            res += e0[i] * pow(k, i)
        return res

if __name__ == '__main__':
    arr = [1, 1, 1, 2, 6, 6, 2, 2, 10, 10, 10, 12, 12, 12, 6, 9]
    print(KGetter.once_num(arr, 3))