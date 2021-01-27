"""
问题描述：给定链表的头结点head,实现删除链表的中间节点的函数，例如：
不删除任何节点；
1->2,删除节点1；
1->2->3,删除节点2；
1->2->3->4，删除节点2；
1->2->3->4->5，删除节点3；
进阶：
给定链表头节点head、整数a和b，实现删除位于a/b节点处的函数，例如：
链表1->2->3->4->5,假设a/b的值为r。
如果r等于0，不删除任何节点；
如果r在区间(0, 1/5]之间，删除节点1；
如果r在区间(1/5, 2/5]之间，删除节点2；
如果r在区间(2/5, 3/5]之间，删除节点3；
如果r在区间(3/5, 4/5]之间，删除节点4；
如果r在区间(4/5, 1]之间，删除节点5；
如果r大于1，不删除任何节点。
"""
import math

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class RemoveNode:

    @classmethod
    def print_list(cls, head):
        while head is not None:
            print(head.value)
            head = head.next

    @classmethod
    def remove_mid_node(cls, head):
        # 无节点或只有一个节点
        if head is None or head.next is None:
            return head
        # 只有两个节点
        if head.next.next is None:
            return head.next
        # 以三个节点为起始
        pre = head
        cur = head.next.next
        # 判断增长了几个2的长度，只要增加一个2，删除的点就后移一个
        while cur.next and cur.next.next:
            pre = pre.next
            cur = cur.next.next
        # 修改待删除的点的前一个点的连接
        pre.next = pre.next.next
        return head

    @classmethod
    def remove_k_node(cls, head, a, b):
        if b == 0:
            raise RuntimeError('b can"t be 0')
        if a < 1 or a > b or head is None:
            return head
        # 求链表的长度
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        # 向上取整求该删除第edge个节点
        edge = math.ceil(a/b*n)

        if edge == 1:
            head = head.next
        elif edge > 1:
            pre = None
            cur = head
            while edge > 1:
                pre = cur
                cur = cur.next
                edge -= 1
            pre.next = cur.next
        return head
        

if __name__ == '__main__':
    node = Node(1)
    node.next = Node(2)
    node.next.next = Node(3)
    node.next.next.next = Node(4)
    node.next.next.next.next = Node(5)
    node.next.next.next.next.next = Node(6)

    RemoveNode.remove_mid_node(node)
    RemoveNode.remove_k_node(node, 2, 5)
    RemoveNode.print_list(node)