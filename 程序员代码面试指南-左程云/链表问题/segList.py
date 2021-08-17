'''
给出一个长度为 n 的单链表和一个值 x ，单链表的每一个值为 list[i]，请返回一个链表的头结点，
要求新链表中小于 x 的节点全部在大于等于x 的节点左侧，并且两个部分之内的节点之间与原来的链表要保持相对顺序不变
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self , head , x ):
        # write code here
        # 使用两个伪节点将链表分隔开
        small = ListNode(-1)
        smallCopy = small
        big = ListNode(-1)
        bigCopy = big
        
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next
            head = head.next
        big.next = None
        small.next = bigCopy.next
        return smallCopy.next