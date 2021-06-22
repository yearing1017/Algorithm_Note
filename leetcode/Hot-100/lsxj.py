# -*- coding: utf-8 -*-
"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
例如：
    输入：l1 = [2,4,3], l2 = [5,6,4]
    输出：[7,0,8]
    解释：342 + 465 = 807.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ca = 0
        n1 = 0
        n2 = 0
        n = 0

        dummy = ListNode(-1)
        pre = dummy
        node = None

        cur1 = l1
        cur2 = l2

        while cur1 or cur2:
            n1 = cur1.val if cur1 else 0
            n2 = cur2.val if cur2 else 0
            n = n1 + n2 + ca
            node = ListNode(n % 10)
            pre.next = node
            pre = node
            ca = n // 10
            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None
        
        # 最后进位的处理
        if ca == 1:
            node = ListNode(1)
            pre.next = node
        return dummy.next

