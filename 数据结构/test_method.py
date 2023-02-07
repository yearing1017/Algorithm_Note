class TestMethod:
    def __init__(self, value):
        self.num = value

    def printNum(self):
        print('我是一个普通的类内函数：',self.num)
        

    @classmethod
    def classprintNum(cls):
        print('我是@classmethod类内函数：',cls(8).num)

    @staticmethod
    def staticprintNum(value):
        print('我是@staticmethod类内函数：',value)

if __name__ == '__main__':
    # 普通函数的调用
    test = TestMethod(7)
    test.printNum()
    print('===============')
    # classmethod的使用
    test.classprintNum()
    TestMethod.classprintNum()
    print('===============')
    # staticmethod的使用
    test.staticprintNum(test.num)
    TestMethod.staticprintNum(9)
    #TestMethod.staticprintNum()
