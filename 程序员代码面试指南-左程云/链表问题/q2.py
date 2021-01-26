"""
问题描述：分别实现两个函数，一个可以删除单链表中倒数第K个节点，另一个
可以删除双链表中倒数第K个节点

要求：如果链表长度为N，时间复杂度达到O(N),额外空间复杂度达到O(1)
"""

# 单链表结构
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# 双链表
class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.pre = None

class RemoveTool:

    @classmethod
    def print_list(cls, head):
        while head is not None:
            print(head.value)
            head = head.next
        

    @classmethod
    def remove_last_k_node(cls, head, k):
        if head is None or k < 1:
            return head
        
        # k为一个正常的大于1的数
        cur = head
        while cur:
            k -= 1
            cur = cur.next

        # k>0 说明找不到倒数第k点
        if k > 0:
            return head
        # k=0 数目倒数第k个点就是头结点，所以删除之后，返回第二个结点
        elif k == 0:
            return head.next
        # k<0 需要找到第N-k个点，即需要删除的第k点的前一点
        else:
            pre = None
            cur = head
            while k<0:
                # 因为这里不能使用++k，找到倒数第k个点
                k += 1
                # 第N-k个点
                pre = cur
                # 第倒数k个点
                cur = cur.next
            pre.next = cur.next
        return head

    @classmethod
    def remove_last_k_node_from_double(cls, head, k):
        if head is None or k < 1:
            return head

        node = head
        while node is not None:
            k -= 1
            node = node.next

        if k > 0:
            return head
        elif k == 0:
            head.next.pre = None
            return head.next
        else:
            cur = head
            while k<0:
                k += 1
                cur = cur.next
            # 此时的cur为需要删除的点
            cur.next.pre = cur.pre
            cur.pre.next = cur.next
        return head
        

if __name__ == '__main__':
    node1 = Node(1)
    node1.next = Node(2)
    node1.next.next = Node(3)
    node1.next.next.next = Node(4)
    node1.next.next.next.next = Node(5)
    node1.next.next.next.next.next = Node(6)
    cnode = RemoveTool.remove_last_k_node(node1, 5)
    RemoveTool.print_list(cnode)

    node2 = DoubleNode(1)
    node2.next = DoubleNode(2)
    node2.next.pre = node2
    node2.next.next = DoubleNode(3)
    node2.next.next.pre = node2.next
    node2.next.next.next = DoubleNode(4)
    node2.next.next.next.pre = node2.next.next
    node2.next.next.next.next = DoubleNode(5)
    node2.next.next.next.next.pre = node2.next.next.next
    node2.next.next.next.next.next = DoubleNode(6)
    node2.next.next.next.next.next.pre = node2.next.next.next
    dcnode = RemoveTool.remove_last_k_node_from_double(node2, 5)
    RemoveTool.print_list(dcnode)