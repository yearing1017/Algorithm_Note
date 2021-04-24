# 判断给定的链表中是否有环。如果有环则返回true，否则返回false。
def hasCycle(self , head ):
    if not head:
        return False
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            return True
    return False