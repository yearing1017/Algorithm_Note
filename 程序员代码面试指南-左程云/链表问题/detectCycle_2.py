# 对于一个给定的链表，返回环的入口节点，如果没有环，返回null
'''
# f = 2s 且 f = s + nb(a表示表头到环的入口 b表示环的长度) ==》推出 f = 2nb s = nb
# 也就是相遇时两者走了2nb nb步数  
# 如果让指针从头走，走a+nb才能走到环的入口，现在s已经走了nb了 再走a步即可
# 但是不知道a的值，所以设一个新指针slow2 从表头出发，每次走一步，走到入口即a步 slow同样
'''
def detectCycle(self , head ):
    if not head:
        return None
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            new_slow = head
            while new_slow != slow:
                new_slow = new_slow.next
                slow = slow.next
            return slow
    return None