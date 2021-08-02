# -*- coding: utf-8 -*-
"""
问题描述：假设链表中每个节点的值都在[0,9]之间，那么链表整体就可以代表一个整数，
例如：9->3->7,可以代表整数937.给定两个这种链表的头结点head1和head2，请生
成代表两个整数相加值的结果链表。例如：链表1为9->3->7，链表2为6->3,最后生成
新的结果链表为1->0->0->0.

思路：
1）如果将链表先转化为整数相加，再转成链表，可能会出现溢出
2）可以使用逆序栈将链表节点压入栈，再进行操作
3）利用链表的逆序求解，这样不会占用额外空间复杂度
"""

# 单链表结构
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class ListAddTool:
    @classmethod
    def print_list(cls, head):
        '''
        node = head.next
        print(head.value)
        while node != head:
            print(node.value)
            node = node.next
        '''
        while head:
            print(head.value, end='\t')
            head = head.next

    @classmethod
    def add_list_2(cls, head1, head2):
        s1 = list()
        s2 = list()
        # 先压入栈
        while head1:
            s1.append(head1.value)
            head1 = head1.next
        while head2:
            s2.append(head2.value)
            head2 = head2.next
        ca = 0 # 进位
        n1 = 0
        n2 = 0
        n = 0
        cur = None
        pre = None
        while s1 or s2:
            if s1:
                n1 = s1.pop()
            else:
                n1 = 0
            if s2:
                n2 = s2.pop()
            else:
                n2 = 0
            n = n1 + n2 + ca
            pre = cur
            cur = Node(n % 10)
            cur.next = pre
            if n/10 >= 1:
                ca = 1
            else:
                ca = 0

        # 当都遍历完之后，根据进位ca是否为1来决定
        if ca == 1:
            pre = cur
            cur = Node(1)
            cur.next = pre
        return cur

    @staticmethod
    def revert_linked_list(head):
        pre = None
        while head is not None:
            next_node = head.next
            head.next = pre
            pre = head
            head = next_node

        return pre

    @classmethod
    def add_list_3(cls, head1, head2):
        if head1 is None:
            return head2

        if head2 is None:
            return head1
        # 先逆序，得到高低位，节省栈空间
        reversed_list1 = ListAddTool.revert_linked_list(head1)
        reversed_list2 = ListAddTool.revert_linked_list(head2)

        new_head = None
        new_list = None
        flag = 0

        while reversed_list1 is not None or reversed_list2 is not None:
            if reversed_list1 is None:
                value1 = 0
            else:
                value1 = reversed_list1.value

            if reversed_list2 is None:
                value2 = 0
            else:
                value2 = reversed_list2.value

            temp = value1 + value2 + flag
            if temp/10 >= 1:
                flag = 1
                if new_list is None:
                    new_head = Node(temp % 10)
                    new_list = new_head
                else:
                    new_list.next = Node(temp % 10)
                    new_list = new_list.next
            else:
                flag = 0
                if new_list is None:
                    new_head = Node(temp)
                    new_list = new_head
                else:
                    new_list.next = Node(temp)
                    new_list = new_list.next

            if reversed_list1 is not None:
                reversed_list1 = reversed_list1.next
            if reversed_list2 is not None:
                reversed_list2 = reversed_list2.next

        if flag == 1:
            new_list.next = Node(1)
        reversed_new_head = ListAddTool.revert_linked_list(new_head)
        return reversed_new_head

    @classmethod
    def add_list_4(cls, head1, head2):
        # write code here
        head1 = cls.revert_linked_list(head1)
        head2 = cls.revert_linked_list(head2)
        
        ca = 0
        n1 = 0
        n2 = 0
        n = 0
        
        pre = None
        node = None
        cur1 = head1
        cur2 = head2
        while cur1 or cur2:
            n1 = cur1.value if cur1 else 0
            n2 = cur2.value if cur2 else 0
            n = n1 + n2 + ca
            node = Node(n % 10)
            node.next = pre
            pre = node
            ca = n // 10
            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None
        if ca == 1:
            pre = node
            node = Node(1)
            node.next = pre
        cls.revert_linked_list(head1)
        cls.revert_linked_list(head2)
        
        return node

    # 若两个链表都是倒序存放 例如输入：(7 -> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295  输出：2 -> 1 -> 9，即912
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1 = l1
        cur2 = l2
        n1 = 0
        n2 = 0
        n = 0
        ca = 0
        pre = cur = ListNode(-1)
        while cur1 or cur2:
            n1 = cur1.val if cur1 else 0
            n2 = cur2.val if cur2 else 0

            n = n1 + n2 + ca

            node = ListNode(n % 10)
            cur.next = node
            cur = node

            ca = n // 10

            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None
        
        if ca:
            cur.next = ListNode(1)
        
        return pre.next

if __name__ == '__main__':
    node1 = Node(9)
    node1.next = Node(9)
    node1.next.next = Node(9)

    node2 = Node(1)

    #ListAddTool.print_list(ListAddTool.add_list_2(node1, node2))
    #print()
    #ListAddTool.print_list(ListAddTool.add_list_3(node1, node2))
    #print()
    ListAddTool.print_list(ListAddTool.add_list_4(node1, node2))
    print()


