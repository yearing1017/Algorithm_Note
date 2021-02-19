"""
问题描述：给定一个无序单链表的头结点head，删除其中值重复出现的节点。
例如：1->2->3->3->4->4->2->1->1->None，删除值重复的节点之后为
1->2->3->4_None.
要求：分别按以下要求实现两种方法
1)如果链表长度为N，时间复杂度为O(N)
2)额外空间复杂度为O(1)

思路：
1）使用hashmap辅助:时间复杂度和空间复杂度都为O(N)
2）类似选择排序的方式，时间复杂度为O(N^2),空间复杂度为O(1)
"""
# 单链表结构
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class DuplicatedNodeRemove:
    @classmethod
    def print_list(cls, head):
        while head:
            print(head.value)
            head = head.next
    
    @classmethod
    def remove_duplicate_node(cls, head):
        if head is None or head.next is None:
            return head
        node_set = set()
        pre = head
        cur = head.next
        node_set.add(head.value)
        while cur is not None:
            if cur.value in node_set:
                pre.next = cur.next
            else:
                node_set.add(cur.value)
                pre = cur
            cur = cur.next
        return head

    @classmethod
    def remove_duplicate_node2(cls, head):
        cur = head
        pre = None
        next_node = None
        while cur:
            pre = cur
            next_node = cur.next
            while next_node:
                if cur.value == next_node.value:
                    pre.next = next_node.next
                else:
                    pre = next_node
                next_node = next_node.next
            cur = cur.next
        return head

if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(4)
    head.next.next.next.next.next = Node(4)
    head.next.next.next.next.next.next = Node(2)
    head.next.next.next.next.next.next.next = Node(1)
    head.next.next.next.next.next.next.next.next = Node(1)
    DuplicatedNodeRemove.print_list(DuplicatedNodeRemove.remove_duplicate_node(head))
    DuplicatedNodeRemove.print_list(DuplicatedNodeRemove.remove_duplicate_node2(head))