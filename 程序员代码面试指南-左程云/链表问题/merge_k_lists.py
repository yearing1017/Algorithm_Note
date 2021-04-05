# 合并k个已排序的链表并将其作为一个已排序的链表返回。

# Node结构
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Solution:
    # 方法1：直接将k个链表的元素全都放到一个list中，再排序，再进行结点的连接
    def mergeKLists_1(self, lists):
        res = []
        for li in lists:
            while li:
                res.append(li.val)
                li = li.next
        res.sort()
        dummy = Node(0)
        for num in res:
            node = Node(num)
            dummy.next = node
            dummy = node
        return dummy.next

    # 方法二：递归将lists分割成两两形式，进行2个链表的连接
    def mergeKLists_2(self, lists):
        if not lists:
            return
        length = len(lists)
        return self.merge(lists, 0, length-1)

    def merge(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = (left + right)//2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid+1, right)
        return self.merge2list(l1, l2)
    
    def merge2list(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        
        dummy = head = Node(0)
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        head.next = l1 if l1 else l2
        return dummy.next
