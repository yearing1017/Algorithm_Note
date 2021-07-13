'''
 O(n) 时间复杂度和 O(1) 空间复杂度 判断回文链表
'''
# 单链表结构
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def isPalindrome(self, head: Node) -> bool:
        # 快慢指针找到中点  ==>  只对后半部分翻转  ==>  依次判断是否和前半部分相同
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # 奇数 找到中点  偶数 找到 后半部分的起点
        hou_head = slow.next
        slow.next = None
        new_hou_head = self.reverseList(hou_head)
        while head and new_hou_head:
            if head.value != new_hou_head.value:
                return False
            head = head.next
            new_hou_head = new_hou_head.next
        return True

    
    def reverseList(self, head: Node):
        pre = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        return pre