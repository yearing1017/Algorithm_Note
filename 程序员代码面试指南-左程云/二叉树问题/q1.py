"""
问题描述：分别用递归和非递归方式实现二叉树的先序、中序、和后续遍历

思路：使用非递归的方式需要使用辅助栈代替函数栈
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 先、中、后序递归遍历二叉树
class RecursiveVisit:
    # 递归先序遍历
    @classmethod
    def visit_in_first_order(cls, head):
        if head is None:
            return
        print(head.value, end=' ')
        cls.visit_in_first_order(head.left)
        cls.visit_in_first_order(head.right)

    # 递归中序遍历
    @classmethod
    def visit_in_mid_order(cls, head):
        if head is None:
            return
        cls.visit_in_mid_order(head.left)
        print(head.value, end=' ')
        cls.visit_in_mid_order(head.right)

    # 递归后序遍历
    @classmethod
    def visit_in_last_order(cls, head):
        if head is None:
            return
        cls.visit_in_last_order(head.left)
        cls.visit_in_last_order(head.right)
        print(head.value, end=' ')

# 非递归遍历二叉树
class LoopVisit:
    #使用辅助栈先序遍历
    @classmethod
    def visit_in_first_order(cls, head):
        if head is None:
            return
        stack = list()
        stack.append(head)
        while stack:
            cur = stack.pop()
            print(cur.value, end=' ')
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
    
    #使用辅助栈中序遍历
    @classmethod
    def visit_in_mid_order(cls, head):
        if head is None:
            return
        stack = list()
        cur = head
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                print(cur.value, end=' ')
                cur = cur.right



    # 使用两个栈后序遍历二叉树
    @classmethod
    def visit_in_last_order1(cls, head):
        if head is None:
            return
        stack1 = list()
        stack2 = list()

        stack1.append(head)

        while len(stack1) > 0:
            cur = stack1.pop()
            stack2.append(cur)
            if cur.left is not None:
                stack1.append(cur.left)
            if cur.right is not None:
                stack1.append(cur.right)


        while len(stack2) > 0:
            print(stack2.pop().value, end=' ')
    

    #不使用辅助栈后序遍历二叉树
    @classmethod
    def visit_in_last_order2(cls, head):
        if head is None:
            return
        h = head # h代表最近一次弹出并打印的节点
        c = None # c代表栈当前的栈顶节点 但不弹出
        stack = list()
        stack.append(h)
        while stack:
            c = stack[-1]
            if c.left and h != c.left and h != c.right:
                stack.append(c.left)
            elif c.right and h != c.right:
                stack.append(c.right)
            else:
                print(stack.pop().value, end=' ')
                h = c

# 三种遍历方式放到一个函数中
class Solution:
    def threeOrders(self , root ):
        pre_order, in_order, post_order = [], [], []
        def find(root):
            if not root: return None
            pre_order.append(root.val)  # 先序：根左右
            find(root.left)
            in_order.append(root.val)   # 中序：左根右
            find(root.right)
            post_order.append(root.val) # 后序：左右根
        find(root)
        return [pre_order, in_order, post_order]

if __name__ == '__main__':
    head = Node(5)
    head.left = Node(3)
    head.right = Node(8)
    head.left.left = Node(2)
    head.left.right = Node(4)
    head.left.left.left = Node(1)
    head.right.left = Node(7)
    head.right.left.left = Node(6)
    head.right.right = Node(10)
    head.right.right.left = Node(9)
    head.right.right.right = Node(11)

    RecursiveVisit.visit_in_first_order(head)
    print()
    LoopVisit.visit_in_first_order(head)
    print()
    print('===========================')

    RecursiveVisit.visit_in_mid_order(head)
    print()
    LoopVisit.visit_in_mid_order(head)
    print()
    print('===========================')
    RecursiveVisit.visit_in_last_order(head)
    print()
    LoopVisit.visit_in_last_order1(head)
    print()
    LoopVisit.visit_in_last_order2(head)
    print()
    
