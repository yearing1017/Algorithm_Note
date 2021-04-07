"""
问题描述：给定一个单链表的头结点head，实现一个调整单链表的函数，使得每K个节点之间逆序，
如果最后不够k个节点一组，则不调整最后几个节点。
例如：k = 3时
链表：1->2->3->4->5->6->7->8->None
调整后:3->2->1->6->5->4->7->8->None,7、8不调整，因为不够一组

思路：
1）使用辅助栈或者队列来做n*k个节点的倒置
2）直接使用有限（四个）变量来解决该问题，left表示每k个节点的前一个，start表示每k个节点
的第一个，end表示每k个节点的最后一个，right表示每k个节点的最后一个的下一个。在翻转之前，
有关系：left.next = start  end.next = right。可利用该关系解决。注意边界条件
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class ReversePartList:
    @classmethod
    def print_list(cls, head):
        while head:
            print(head.value)
            head = head.next
    # 使用辅助栈，时间复杂度和空间复杂度都为O(N)
    @classmethod
    def reverse_use_stack(cls, head, k):
        if head is None or k < 2:
            return head
        stack = list()
        newHead = head
        cur = head
        pre = None
        next_node = None
        while cur:
            next_node = cur.next
            stack.append(cur)
            if len(stack) == k:
                pre = cls.resign1(stack, pre, next_node)
                newHead = cur if newHead == head else newHead
            cur = next_node
        return newHead
    @classmethod
    def resign1(cls, stack, left, right):
        cur = stack.pop()
        # 处理左边界
        if left:
            left.next = cur
        while stack:
            next_node = stack.pop()
            cur.next = next_node
            cur = next_node
        # 处理右边界
        cur.next = right
        return cur
        
    # 使用额外的变量 不使用栈 空间复杂度降为O(1)
    @classmethod
    def reverse_list(cls, head, k):
        if head is None or k < 2:
            return head
        
        cur = head
        start = None
        pre = None
        next_node = None
        count = 1

        while cur:
            next_node = cur.next
            if count == k:
                #左边的第一个点
                start = head if pre is None else pre.next
                #新头结点
                head = cur if pre is None else head
                #调整
                cls.resign2(pre, start, cur, next_node)
                # 调整完之后，更新pre为倒序后的原来的start
                pre = start
                count = 0
            count += 1
            cur = next_node
        return head

    @classmethod
    def resign2(cls, left, start, end, right):
        pre = start
        cur = start.next
        # 改变指针，逆序
        while cur != right:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        # 调整左边界
        if left:
            left.next = end
        # 调整右边界
        start.next = right




if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)
    k = 3
    #ReversePartList.print_list(ReversePartList.reverse_use_stack(head, k))
    ReversePartList.print_list(ReversePartList.reverse_list(head, k))