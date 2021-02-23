"""
问题描述：一种特殊的链表节点类描述如下：
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.rand = None

Node类中的value是节点值，next指针和正常单链表中next指针的意义一样，都指向下一个节点，rand
指针是Node类中新增的指针，这个指针可能指向链表中任意一个节点，也可能指向None.

给定一个由Node节点类型组成的无环单链表的头结点head，请实现一个函数完成这个链表中所有结构的复
制，并返回复制的新链表的头结点。例如：链表 1->2->3->None,假设1的rand指针指向3，2的rand指
针指向None,3的rand指针指向1。复制后的链表应该也是这种结构，比如,1'->2'->3'->None,1'的
rand指针指向3',2'的rand指针指向None，3'的rand指针指向1',最后返回1'

进阶：不使用额外的数据结构，只用有限几个变量，且在时间复杂度为O(N)内完成原问题要实现的函数。

思路：
1）如果不考虑空间复杂度，可使用hashmap求解
2）由于复制的链表和原链表具有操作一致性，所以可以直接在原链表中每个元素后插入一个和前一个一样的
元素，两两元素的取node.rand操作必定是一致的
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.rand = None

    # 时间复杂度和空间复杂度都为O(N)    
    @classmethod
    def copy_list_use_map(cls, head):
        if head is None:
            return None
        
        temp_map = {}
        cur = head
        # 复制对应单纯的结点到map中
        while cur:
            temp_map.setdefault(cur, Node(cur.value))
            cur = cur.next
        # 将真实结点的指针复制到copy结点
        node = head
        while node:
            temp_map.get(node).next = temp_map.get(node.next)
            temp_map.get(node).rand = temp_map.get(node.rand)
            node = node.next
        return temp_map.get(head)

    #时间复杂度O(N)空间复杂度都为O(1) 
    @classmethod
    def copy_list(cls, head):
        if head is None:
            return None
        
        # 复制每个节点并链接到相应节点的后面
        cur = head
        next_node = None
        while cur:
            next_node = cur.next
            cur.next = Node(cur.value)
            cur.next.next = next_node
            cur = next_node
        
        # 设置复制节点的rand指针
        cur = head
        curCopy = None
        while cur:
            next_node = cur.next.next
            curCopy = cur.next
            curCopy.rand = cur.rand.next if cur.rand else None
            cur = next_node
        # 拆分
        res = head.next
        cur = head
        while cur:
            next_node = cur.next.next
            curCopy = cur.next
            cur.next = next_node
            curCopy.next = next_node.next if next_node else None
            cur = next_node
        return res