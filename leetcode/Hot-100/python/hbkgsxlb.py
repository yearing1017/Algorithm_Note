"""
给你一个链表数组，每个链表都已经按升序排列
请你将所有链表合并到一个升序链表中，返回合并后的链表
例如：
    输入：lists = [[1,4,5],[1,3,4],[2,6]]
    输出：[1,1,2,3,4,4,5,6]
    解释：链表数组如下：
    [
    1->4->5,
    1->3->4,
    2->6
    ]
    将它们合并到一个有序链表中得到。
    1->1->2->3->4->4->5->6
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return
        n = len(lists)
        return self.merge(lists, 0, n-1)
    
    def merge(self, lists, left, right):
        # 二分 将k个链表不断分成两个表
        # 递归结束
        if left == right:
            return lists[left]
        mid = (left + right) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid+1, right)
        return self.merge2list(l1, l2)
        
    def merge2list(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        head = dummy = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        head.next = l1 if l1 else l2
        return dummy.next

        