"""
问题描述：41个人排成一个圈，由第一个人开始报数，报数到3的人就自杀，
然后再由下一个人重新报1，报数到3的人再自杀，这样依次下去，直到剩下
最后一个人时，他可以自由选择自己的命运。这就是著名的约瑟夫问题，现在
请用单向环形链表描述该结构并呈现整个自杀过程

要求：输入一个环形单向链表的头结点head和报数的值m，返回最后生存的节
点，该节点自己组成一个单向环形链表，其他节点都删掉
进阶：
如果链表头结点数为N,想在时间复杂度为O(N)时完成原问题的要求，如何实现

思路：参见https://blog.oldj.net/2010/05/27/joseph-ring/
"""

# 单链表结构
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class JosephusCircle:
    @classmethod
    def print_list(cls, head):
        node = head.next
        print(head.value)
        while node != head:
            print(node.value)
            node = node.next

    @classmethod
    def kill_1(cls, head, m):
        if head is None or head.next is head or m < 1:
            return head
        count = 1
        pre = head
        node = head.next
        while node != pre:
            count += 1
            if count < m:
                pre = node
            else:
                pre.next = node.next
                count = 0
            node = node.next
        return node

    @classmethod
    def kill_1_1(cls, head, m):
        if head is None or head.next is head or m < 1:
            return head
        node = head
        # 找尾结点
        while node.next != head:
            node = node.next
        # 以尾结点node和头结点head往下遍历，每次两个结点移动一步，遍历到m时，改变链接，直到还有一个点
        count = 0
        while head != node:
            count += 1
            if count == m:
                node.next = head.next
                count = 0
            else:
                node = node.next
            head = node.next
        return head



if __name__ == '__main__':
    cur_node = Node(1)
    cur_node.next = Node(2)
    cur_node.next.next = Node(3)
    cur_node.next.next.next = Node(4)
    cur_node.next.next.next.next = Node(5)
    cur_node.next.next.next.next.next = cur_node

    cur_node = JosephusCircle.kill_1_1(cur_node, 3)
    JosephusCircle.print_list(cur_node)
    print(cur_node.value)