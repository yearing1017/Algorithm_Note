"""
问题描述：给定一个无序单链表的头结点head，实现单链表的选择排序
要求：额外空间复杂度为O(1)

思路：选择排序是从未排序的部分找到最小值，放到排好序部分的末尾
(区分选择和冒泡排序，冒泡是比较并交换，而选择是移动指针，每次指
针都是指向最小值，一趟过程后把当前指针指向的值放到排好序的尾部)
"""
# 单链表结构
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SortList:
    @classmethod
    def print_list(cls, head):
        while head:
            print(head.value)
            head = head.next

    # 找到最小结点的前一个结点的位置
    @classmethod
    def get_small_pre_node(cls, head):
        smallPre = None
        small = head
        pre = head
        cur = head.next
        while cur:
            if cur.value < small.value:
                smallPre = pre
                small = cur
            pre = cur
            cur = cur.next
        return smallPre

    # 每找到一个最小结点就删除 并排序
    @classmethod
    def sort_list(cls, head):
        tail = None # 排序尾部
        cur = head # 未排序头部
        smallPre = None
        small = None

        while cur:
            small = cur
            smallPre = cls.get_small_pre_node(cur)
            # 若找到，删除最小的结点
            if smallPre:
                small = smallPre.next
                smallPre.next = small.next
            # 下一步该遍历的cur
            cur = cur.next if cur == small else cur
            # 排序部分
            if tail is None:
                head = small
            else:
                tail.next = small
            tail = small
        return head

if __name__ == '__main__':
    head = Node(3)
    head.next = Node(1)
    head.next.next = Node(2)
    head = SortList.sort_list(head)
    #SortList.sort_list(head)
    SortList.print_list(head)

    head = Node(3)
    head.next = Node(1)
    head.next.next = Node(4)
    head.next.next.next = Node(2)
    head = SortList.sort_list(head)
    SortList.print_list(head)
