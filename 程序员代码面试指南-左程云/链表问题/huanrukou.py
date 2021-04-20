# 找到链表中环的入口
def detectCycle(self , head ):
    if not head:
        return None
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            new_slow = head
            while new_slow != slow:
                slow = slow.next
                new_slow = new_slow.next
            return slow
    return None