"""
给定一个字符串str，如果str符合日常书写的整数形式，并且属于32位整数的范围，
返回str所代表的整数值，否则返回0.

举例：
str = '123'，返回123
str = '023'，返回0
str = 'A13'，返回0
str = '0'，返回0
str = '2147483647'，返回2147483647
str = '2147483648'，返回0 溢出
str = '-123'，返回-123
"""


class IntegerGenerater:
    @classmethod
    def isvalid(cls, str):
        # 检测str是否符合日常书写
        #1. 不以负号 且 不以数字开头
        if str[0] != '-' and (str[0]<'0' or str[0]>'9'):
            return False
        if str[0] == '-' and(len(str)==1 or str[1]=='0'):
            return False
        if str[0] == '0' and len(str) > 1:
            return False
        for i in range(1, len(str)):
            if str[i] <'0' or str[i] >'9':
                return False
        return True

    # int的最大值为2147483647   最小值为-2147483648 所以负数表示的范围大一些
    @classmethod
    def get_integer(cls, str1):
        if not str1:
            return 0

        if not cls.isvalid(str1):
            return 0
        if str1[0] == '-':
            flag = False
        else:
            flag = True #正数

        minq = -2147483648 // 10
        minr = -2147483648 % 10

        res = 0
        cur = 0

        if flag:
            index = 0
        else:
            index = 1
        for i in range(index, len(str1)):
            cur = 0 - int(str1[i])
            #print(cur)
            # 溢出的两种情况
            if res < minq or (res == minq and cur < minr):
                return 0 
            res = res*10 + cur
        # 转为正数溢出
        if flag and res == - 2147483648:
            return 0
        
        return -res if flag else res



if __name__ == '__main__':
    print(IntegerGenerater.get_integer('2147483647'))
    print(IntegerGenerater.get_integer('-2147483648'))
    print(IntegerGenerater.get_integer('2147483648'))
    print(IntegerGenerater.get_integer('-2147483649'))
    print(IntegerGenerater.get_integer('-123'))