# 判断链表中是否存在环
'''
方法一：哈希表(时间空间都为O(N))
最容易想到的方法是遍历所有节点，每次遍历到一个节点时，判断该节点此前是否被访问过。
具体地，我们可以使用哈希表来存储所有已经访问过的节点。
每次我们到达一个节点，如果该节点已经存在于哈希表中，则说明该链表是环形链表，否则就将该节点加入哈希表中。
重复这一过程，直到我们遍历完整个链表即可。

方法二：快慢指针(时间O(N)空间O(1))

本方法需要读者对「Floyd 判圈算法」（又称龟兔赛跑算法）有所了解。
假想「乌龟」和「兔子」在链表上移动，「兔子」跑得快，「乌龟」跑得慢。当「乌龟」和「兔子」从链表上的同一个节点开始移动时，
如果该链表中没有环，那么「兔子」将一直处于「乌龟」的前方；
如果该链表中有环，那么「兔子」会先于「乌龟」进入环，并且一直在环内移动。
等到「乌龟」进入环时，由于「兔子」的速度快，它一定会在某个时刻与乌龟相遇，即套了「乌龟」若干圈。
我们可以根据上述思路来解决本题。
具体地，我们定义两个指针，一快一满。慢指针每次只移动一步，而快指针每次移动两步。
初始时，慢指针在位置 head，而快指针在位置 head.next。
这样一来，如果在移动的过程中，快指针反过来追上慢指针，就说明该链表为环形链表。否则快指针将到达链表尾部，该链表不为环形链表。

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast and fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True