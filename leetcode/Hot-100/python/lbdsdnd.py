"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点
一趟扫描完成
例如：
    输入：head = [1,2,3,4,5], n = 2
    输出：[1,2,3,5]
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 先找规律  倒数第n个结点 = 正数第 len-n+1 个结点
        # 例如：1 2 3 4 5 6；   6 2 5； 6 3 4； 6 5 2
        cur = head
        #pre = head
        del_node = head
        del_pre = head
        # 从头遍历到尾  n这个数字依次-1
        while cur:
            n -= 1
            cur = cur.next
        # 若n-1之后大于0 说明倒数第n个点 不存在  直接返回head
        if n > 0:
            return head
        elif n == 0:
            return head.next
        else:
            while n < 0:
                n += 1
                del_pre = del_node
                del_node = del_node.next
            del_pre.next = del_node.next
        return head

