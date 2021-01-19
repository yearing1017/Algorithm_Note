"""
问题描述：构造一个特殊的栈，要求
1）使之pop()、push()和getMin() (求最小值) 的操作的时间复杂度都为O(1)
2）可以使用现成的栈类型
"""

# 思路1：使用两个栈，一个用来保存当前栈的元素，功能与正常栈一样；另一个栈用于保存每一步的最小值；针对弹出时规则设定

class MyStack:
    def __init__(self):
        self.stackData = list()
        self.stackMin = list()
    def push(self, value):
        length = len(self.stackMin)
        if length == 0:
            self.stackMin.append(value)
        elif value <= self.getMin():
            self.stackMin.append(value)
        self.stackData.append(value)
    def pop(self):
        if len(self.stackData) == 0:
            print('stack is empty!')
        value = self.stackData.pop()
        if value == self.getMin():
            self.stackMin.pop()
        return value
    def getMin(self):
        if len(self.stackMin) == 0:
            print('stack is empty!')
        return self.stackMin[-1]

if __name__ == '__main__':
    stack = MyStack()
    stack.push(3)
    print(stack.getMin())
    stack.push(4)
    print(stack.getMin())
    stack.push(1)
    print(stack.getMin())
    stack.pop()
    print(stack.getMin())
