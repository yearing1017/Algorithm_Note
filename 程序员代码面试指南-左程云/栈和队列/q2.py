"""
问题描述：编写一个类，用两个栈实现一个队列，要求:
支持队列的基本操作，add、poll和peek

思路：使用两个栈模拟队列操作
"""

class MyQuene:
    def __init__(self):
        self.stack_in = list()
        self.stack_out = list()

    def pushToPop(self):
        if len(self.stack_out) == 0:
            while len(self.stack_in) > 0:
                self.stack_out.append(self.stack_in.pop())

    def add(self, value):
        self.stack_in.append(value)
        self.pushToPop()

    def poll(self):
        if len(self.stack_out) == 0 and len(self.stack_in) == 0:
            print('quene is empty!')
        self.pushToPop()
        return self.stack_out.pop()
    
    def peek(self):
        if len(self.stack_out) == 0 and len(self.stack_in) == 0:
            print('quene is empty!')
        self.pushToPop()
        return self.stack_out[-1]

'''
# 剑指offer中的一个简单版本
class CQueue:

    def __init__(self):
        self.stack_in = list()
        self.stack_out = list()

    def appendTail(self, value: int) -> None:
        self.stack_in.append(value)

    def deleteHead(self) -> int:
        if self.stack_out: return self.stack_out.pop()
        elif not self.stack_in: return -1
        else:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()
'''

if __name__ == '__main__':
    queue = MyQuene()
    queue.add(1)
    queue.add(2)
    queue.add(3)
    print(queue.peek())
    print(queue.poll())
    print(queue.peek())
    print(queue.poll())
    print(queue.peek())
    print(queue.poll())