"""
问题描述：一个环形单链表从头结点head开始不降序，同时由最后的节点指回头结点。给定这样一个
环形单链表的头结点head和一个整数num,请生成节点值为num的新节点，并插入到这个环形链表中，
保证调整后的链表依然有序。
"""

# 单链表结构
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class InsertTool:
    @classmethod
    def print_list(cls, head):
        #pre = head
        print(head.value)
        cur = head.next
        while cur != head:
            print(cur.value)
            cur = cur.next
    
    @classmethod
    def insert_node_by_order(cls, head, num):
        node = Node(num)
        if head is None:
            node.next = node
            return node

        pre = head
        cur = head.next
        while cur != head:
            if pre.value <= num and cur.value >= num:
                break
            pre = cur 
            cur = cur.next
        
        pre.next = node
        node.next = cur
        return head if head.value < num else node

if __name__ == '__main__':
    head = None
    head = InsertTool.insert_node_by_order(head, 2)
    head = InsertTool.insert_node_by_order(head, 1)
    head = InsertTool.insert_node_by_order(head, 4)
    head = InsertTool.insert_node_by_order(head, 3)
    head = InsertTool.insert_node_by_order(head, 5)
    head = InsertTool.insert_node_by_order(head, 0)
    InsertTool.print_list(head)