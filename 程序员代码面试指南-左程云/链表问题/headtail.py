'''
给定一个单链表 L 的头节点 head ，单链表 L 表示为：

L0 → L1 → … → Ln-1 → Ln 
请将其重新排列后变为：

L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

思路：1. 找到后半部分链表，偶数就是后一半，奇数就是中间结点后的部分
     2. 将后半部分逆置
     3. 将逆转后的链表逐元素 链接到 前半部分链表的 后面
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 快慢指针找到中点
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        headlist = head
        taillist = slow.next
        slow.next = None
        # 对后半部分逆转
        reverse_taillist = self.reverse(taillist)
        # 逆转后的链表 逐元素 插入到 前半部分的链表
        self.insert(headlist, reverse_taillist)
    
    def reverse(self, head):
        pre = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        return pre
    
    def insert(self, head1, head2):
        h1 = head1
        h2 = head2
        while h1 and h2:
            h1next = h1.next
            h2next = h2.next
            h1.next = h2
            h2.next = h1next
            h1 = h1next
            h2 = h2next