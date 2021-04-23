# 给出一个升序排序的链表，删除链表中的所有重复出现的元素，只保留原链表中只出现一次的元素。
# 123333445   --->   125
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

def deleteDuplicates(head):
    dummy  = ListNode(-1)
    dummy.next = head

    pre = dummy
    cur = head

    while cur and cur.next:
        if cur.val == cur.next.val:
            temp = cur.next
            while temp and temp.val == temp.next.val:
                temp = temp.next
            pre.next = temp
            cur = temp
        else:
            pre = pre.next
            cur = cur.next
    return dummy.next

