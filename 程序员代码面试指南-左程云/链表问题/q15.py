"""
问题描述：对于二叉树的节点来说，其本身的值域，有指向左孩子和右孩子的两个指针：对双向
链表的节点来说，其本身的值域，有指向上一个节点和下一个节点的指针。在结构上，两种结构
有相似性，对于每个节点来说，原来的right指针等价于转换后的next指针，原来的left指针
等价于转换后的last指针。现在有一颗搜索二叉树，请将其转换一个有序的双向链表，并且返回
转换后的双向链表头结点。
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeToList:
    @staticmethod
    def print_list(head):
        while head is not None:
            print(head.value, end=' ')
            head = head.right
        print()

    @classmethod
    def visit_in_mid_order(cls, tree_head, queue):
        if tree_head.left:
            cls.visit_in_mid_order(tree_head.left, queue)
        queue.append(tree_head)
        if tree_head.right:
            cls.visit_in_mid_order(tree_head.right, queue)

    @classmethod
    def revert1(cls, tree_head):
        if tree_head is None:
            return tree_head
        # 题目要求有序结果，且二叉搜索树中序结果是有序的，所以将中序遍历结果存进队列
        queue = list()
        cls.visit_in_mid_order(tree_head, queue)

        head = queue.pop(0)
        pre = head
        while queue:
            cur = queue.pop(0)
            pre.right = cur
            cur.left = pre
            pre = cur
        # 最后一个点的next必为空
        pre.right = None
        return head

if __name__ == '__main__':
    head = Node(5)
    head.left = Node(2)
    head.right = Node(9)
    head.left.left = Node(1)
    head.left.right = Node(3)
    head.left.right.right = Node(4)
    head.right.left = Node(7)
    head.right.right = Node(10)
    head.right.left.left = Node(6)
    head.right.left.right = Node(8)

    # double_list = TreeToList.revert(head)
    # TreeToList.print_list(double_list)

    double_list = TreeToList.revert1(head)
    TreeToList.print_list(double_list)