"""
问题描述：给定一个单链表的头结点head,以及两个整数from和to，在单链表上
把第from个节点到第to个节点这一部分进行反转。
例如：
1->2->3->4->5->None, from=2, to=4
调整结果为：1->4->3->2->5->None

再如：
1->2->3->None, from=1, to=3
调整结果为:
3->2->1->None

要求：
1.如果链表长度为N，时间复杂度要求为O(N)，额外空间复杂度要求为O(1)
2.如果不满足1<=from<=to<=N，则不用调整
"""
# 单链表结构
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class RevertPart:
    @classmethod
    def print_list(cls, head):
        while head is not None:
            print(head.value)
            head = head.next

    @classmethod
    def revert_part_of_linked_list(cls, head, list_from, list_to):
        # 排除特定的已知情况
        if list_from >= list_to or list_from < 1 or head is None:
            return head

        # 求from的前一点 和 to的后一点
        fpre, fnext = None, None
        length = 0
        cur  = head
        while cur:
            length += 1
            if length == list_from - 1:
                fpre = cur
            elif length == list_to + 1:
                fnext = cur
            cur = cur.next
        # 求得链表的length后，排除一种情况
        if list_to > length:
            return head

        # 分析from-to是否在链表中：若fpre空，则说明第一个反转的为头结点；反之，第一个为fpre.next
        if fpre is None:
            node1 = head
        else:
            node1 = fpre.next
        # node2为第二个要反转的点，先保存下来
        node2 = node1.next
        # 反转第一个点的next指针
        node1.next = fnext
        # 循环反转
        while node2 != fnext:
            node_next = node2.next
            node2.next = node1
            node1 = node2
            node2 = node_next
        # node1为最后一个反转的点
        # 若fpre空，不用调整fpre，说明头结点也在其中，返回新的头结点
        if fpre is None:
            return node1
        else:
            fpre.next = node1
        return head

if __name__ == '__main__':
    head = None
    head = RevertPart.revert_part_of_linked_list(head, 1, 1)
    RevertPart.print_list(head)

    head = None
    head = RevertPart.revert_part_of_linked_list(head, 1, 1)
    RevertPart.print_list(head)

    head = Node(1)
    head.next = Node(2)
    head = RevertPart.revert_part_of_linked_list(head, 1, 2)
    RevertPart.print_list(head)

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head = RevertPart.revert_part_of_linked_list(head, 1, 2)
    RevertPart.print_list(head)

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head = RevertPart.revert_part_of_linked_list(head, 2, 3)
    RevertPart.print_list(head)
