'''
给定一个单链表，请设定一个函数，将链表的奇数位节点和偶数位节点分别放在一起，重排后输出。
注意是节点的编号而非节点的数值
'''

class Solution:
    def oddEvenList(self , head ):
        if not head or not head.next:
            return head
        
        odd = head
        oddHead = head
        even = head
        evenHead = head

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = evenHead

        return oddHead