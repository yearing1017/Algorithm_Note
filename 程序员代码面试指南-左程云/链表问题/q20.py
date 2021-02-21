"""
问题描述：给定一个单链表的头部节点head，链表长度为N，如果N为偶数，那么前N/2个节点算作左
半区，后N/2个节点算作右半区；如果N为奇数，那么前N/2个节点算作左半区，后N/2+1个节点算作
是右半区。左半区从左到右依次记作L1->L2->...,右半区从左到右依次记作R1->R2->...，请将
单链表调整成L1->R1->L2->R2...的形式
例如：
1->None,调整为1->None
1->2->None,调整为1->2->None
1->2->3->None,调整为1->2->3->None
1->2->3->4->None,调整为1->3->2->4->None
1->2->3->4->5->None,调整为1->3->2->4->5->None
1->2->3->4->5->6->None,调整为1->4->2->5->3->6->None
"""
# 单链表结构
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class RefactorList:
    @classmethod
    def print_list(cls, head):
        while head:
            print(head.value)
            head = head.next
    
    @classmethod
    def refactor(cls, head):
        # 若为空或长度为1 直接返回不用调整
        if head is None or head.next is None:
            return head
        # 根据规律：长度每+2，mid后移一步，mid是左半部分的最后一个点，right是右半部分的第一个结点
        mid = head
        right = head.next
        while right.next and right.next.next:
            mid = mid.next
            right = right.next.next
        right = mid.next
        # 左右部分分离
        mid.next = None
        cls.merge_lr(head, right)
        return head

    @classmethod
    def merge_lr(cls, left, right):
        next_node = None
        while left.next:
            next_node = right.next
            right.next = left.next
            left.next = right
            # 后移left和right
            left = right.next
            right = next_node
        left.next = right

if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    RefactorList.print_list(RefactorList.refactor(head))

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    RefactorList.print_list(RefactorList.refactor(head))

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    RefactorList.print_list(RefactorList.refactor(head))

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    RefactorList.print_list(RefactorList.refactor(head))