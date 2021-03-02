# 单链表的归并排序

class Solution:
    def sortInList(self , head ):
        # write code here
        # 为空或只有一个节点，不需再分割
        if not head or not head.next:
            return head
        # 快慢指针找到链表的中间结点
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #偶数时 slow为左半部分最后一个 奇数时slow为中间结点
        mid = slow.next # mid为分割的右部分的第一个点
        slow.next = None #分割
        # 递归分割 与 递归排序归并
        left = self.sortInList(head)
        right = self.sortInList(mid)
        h = res = ListNode(0)
        # 左右都存在时 不断合并
        while left and right:
            if left.val < right.val:
                h.next = left
                left = left.next
            else:
                h.next = right
                right = right.next
            h = h.next
        h.next = left if left else right
        return res.next