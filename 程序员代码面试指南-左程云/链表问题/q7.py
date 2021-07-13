"""
问题描述：给定一个链表的头结点，请判断该链表是否为回文结构，例如：
1->2->1,返回true
1->2->2->1,返回true
15->6->15,返回true
1->2->3,返回false

进阶：
如果链表长度为N，时间复杂度达到O(N)，额外空间复杂度达到O(1)

思路：进阶问题的关键是将链表的右半部分反转，然后再进行比较，注意把
改变的状态变回来
"""

# 单链表结构
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class HuiWen:
    # 方法1：利用栈的先进后出，判断是否逆序之后一致；空间复杂度为O(N)
    @classmethod
    def is_huiwen(cls, head):
        stack = list()
        cur = head
        while cur:
            stack.append(cur.value)
            cur = cur.next
        while head:
            if head.value != stack.pop():
                return False
            head = head.next
        return True

    # 优化方法1，只利用栈结构压入右半部分
    @classmethod
    def is_huiwen_2(cls, head):
        if head is None or head.next is None:
            return True
        cur = head
        right = head.next
        # cur结点右移两步，right右移一步，可找到右半部分的第一个结点
        while cur.next and cur.next.next:
            right = right.next
            cur = cur.next.next
        stack = list()
        while right:
            stack.append(right.value)
            right = right.next
        while stack:
            if head.value != stack.pop():
                return False
            head = head.next
        return True

    # 方法3：只利用变量，节省空间；反转右半部分判断
    @classmethod
    def is_huiwen_3(cls, head):
        if head is None or head.next is None:
            return True
        n1 = head
        n2 = head
        # 查找中间结点
        while n2.next and n2.next.next:
            n1 = n1.next
            n2 = n2.next.next
        n2 = n1.next # 右半部分第一个结点
        n1.next = None # 调整mid.next == Null
        # 右半部分反转
        n3 = None
        while n2:
            n3 = n2.next #保存下一个结点
            n2.next = n1
            n1 = n2
            n2 = n3
        n3 = n1 # 保存最后一个结点
        n2 = head # 左边第一个结点
        # 检查回文
        while n1 and n2:
            if n1.value != n2.value:
                return False
                break
            n1 = n1.next
            n2 = n2.next
        # 恢复列表
        n1 = n3.next # 倒数第二个结点
        n3.next = None # 最后一个点
        while n1:
            n2 = n1.next
            n1.next = n3
            n3 = n1
            n1 = n2
        return True

    @classmethod
    def is_huiwen_4(cls, head):
        if not head or not head.next:
            return True
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        houhead = slow.next
        slow.next = None
        rev_houhead = cls.reverselist(houhead)
        while head and rev_houhead:
            if head.value != rev_houhead.value:
                return False
            head = head.next
            rev_houhead = rev_houhead.next
        return True
    
    @classmethod
    def reverselist(cls, head):
        pre = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        return pre


if __name__ == '__main__':
    node = Node(1)
    node.next = Node(2)
    node.next.next = Node(3)
    node.next.next.next = Node(2)
    node.next.next.next.next = Node(1)
    #print(HuiWen.is_huibwen_by_reverse_right(node))
    print(HuiWen.is_huiwen(node))
    print(HuiWen.is_huiwen_2(node))
    print(HuiWen.is_huiwen_3(node))
    print(HuiWen.is_huiwen_4(node))