"""
问题描述：给定两个有序链表的头指针head1和head2,打印两个
链表的公共部分(即链表节点的值相同的部分)

思路：由于链表有序，所以可以比较head1和head2的值进行判断
"""

# Node结构
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class PublicPart:
    @classmethod
    def get_public_part(cls, head1, head2):
        if head1 is None or head2 is None:
            return None
        while head1 and head2:
            if head1.value < head2.value:
                head1 = head1.next
            elif head2.value < head1.value:
                head2 = head2.next
            else:
                print(head1.value)
                head1 = head1.next
                head2 = head2.next

if __name__ == '__main__':
    cur_head1 = Node(2)
    cur_head1.next = Node(3)
    cur_head1.next.next = Node(5)
    cur_head1.next.next.next = Node(6)

    cur_head2 = Node(1)
    cur_head2.next = Node(2)
    cur_head2.next.next = Node(5)
    cur_head2.next.next.next = Node(7)
    cur_head2.next.next.next.next = Node(8)

    PublicPart.get_public_part(cur_head1, cur_head2) 
        