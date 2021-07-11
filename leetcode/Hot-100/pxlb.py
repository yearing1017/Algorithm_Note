"""
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 
你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？ 使用 归并排序
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or head.next:
            return head
        # 归并排序的cut阶段
        # 奇数时，slow指向左边的最后一个点；偶数时，slow指向中点
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # 保存 断开
        mid = slow.next
        slow.next = None
        # 递归cut 左部分
        left = self.sortList(head)
        # 递归cut 右部分
        right = self.sortList(mid)

        # merge 部分
        res = h = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next = left
                left = left.next
            else:
                h.next = right
                right = right.next
            h = h.next
        # 将剩余部分链接到后面
        h.next = left if left else right
        return res.next