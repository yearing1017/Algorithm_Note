"""
问题描述：给定一个链表的头结点head和一个整数num,请实现函数将值为num的节点
全部删除。例如，链表为
1->2->3->4->None,num=3 链表调整后为1->2->4->None
"""

# 单链表结构
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class RemoveAssignedNode:
    @classmethod
    def print_list(cls, head):
        while head:
            print(head.value)
            head = head.next
    
    # 时间复杂度和空间复杂度都为O(N)
    @classmethod
    def remove_node1(cls, head, num):
        # 将不等于num的值存进栈中
        stack = list()
        while head:
            if head.value != num:
                stack.append(head)
            head = head.next
        # 重新连接栈内元素
        while stack:
            stack[-1].next = head
            head = stack.pop()
        return head

    # 时间复杂度O(N) 空间复杂度O(1)
    @classmethod
    def remove_node2(cls, head, num):
        while head:
            if head.value != num:
                break
            else:
                head = head.next
        pre = head
        cur = head.next
        while cur:
            if cur.value == num:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return head


if __name__ == '__main__':
    node = Node(2)
    node.next = Node(2)
    node.next.next = Node(3)
    node.next.next.next = Node(2)
    node.next.next.next.next = Node(4)

    RemoveAssignedNode.print_list(RemoveAssignedNode.remove_node1(node, 2))
    RemoveAssignedNode.print_list(RemoveAssignedNode.remove_node2(node, 2))