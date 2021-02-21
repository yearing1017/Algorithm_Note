"""
问题描述：给定两个有序单链表的头结点head1和head2，请合并两个有序链表，合并后的链表依然
有序，并返回合并后链表的头结点。
例如：
0->2->3->7->None
1->3->5->7->9->None
合并后的链表为：0->1->2->3->3->5->7->7->9->None
"""
# 单链表结构
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MergeListTool:
    @classmethod
    def print_list(cls, head):
        while head:
            print(head.value)
            head = head.next
    
    # 法1
    @classmethod
    def merge1(cls, head1, head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        
        cur1 = head1
        cur2 = head2

        while cur1 and cur2:
            while cur1 and cur1.value <= cur2.value:
                pre = cur1
                cur1 = cur1.next
            pre.next = cur2

            if cur1 is None:
                break

            while cur2 and cur1.value > cur2.value:
                pre = cur2
                cur2 = cur2.next
            pre.next = cur1

            if cur2 is None:
                break

        return head1 if head1.value < head2.value else head2

    # 法2
    @classmethod
    def merge2(cls, head1, head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head1

        head = head1 if head1.value < head2.value else head2
        cur1 = head1 if head == head1 else head2
        cur2 = head2 if head == head1 else head1
        pre = None
        next_node = None

        while cur1 and cur2:
            if cur1.value <= cur2.value:
                pre = cur1
                cur1 = cur1.next
            else:
                next_node = cur2.next
                pre.next = cur2
                cur2.next = cur1
                pre = cur2
                cur2 = next_node
        
        # 若两个有一个遍历完 另一个直接连到后面
        pre.next = cur1 if cur2 is None else cur2
        return head



if __name__ == '__main__':
    head1 = Node(0)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(7)

    head2 = Node(1)
    head2.next = Node(3)
    head2.next.next = Node(5)
    head2.next.next.next = Node(7)
    head2.next.next.next.next = Node(9)

    new_head = MergeListTool.merge1(head1, head2)
    MergeListTool.print_list(new_head)

    new_head2 = MergeListTool.merge2(head1, head2)
    MergeListTool.print_list(new_head2)