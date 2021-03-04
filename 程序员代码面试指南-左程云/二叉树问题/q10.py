"""
问题描述：一棵二叉树原本是搜索二叉树，但是其中有两个节点调换了位置，使得这棵二叉树不再是搜索二叉树，
请找到这两个节点并返回。已知二叉树所有节点的值都不一样，给定二叉树的头结点head,返回一个长度为2的
二叉树节点类型的数组errs。errs[0]表示一个错误节点，errs[1]表示一个错误节点。
进阶：如果在原问题中得到了这两个错误节点，我们当然可以通过交换两个节点值的方式让整棵二叉树重新成为
搜索二叉树，但现在要求不能这么做，而是在结构上完全交换两个节点的位置，请实现调整的函数。
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BSTChecker:
    @classmethod
    def get_wrong_node(cls, head):
        res = [None for i in range(2)]
        if not head:
            return res
        stack = list()
        pre = None
        while stack or head:
            if head:
                stack.append(head)
                head = head.left
            else:
                head = stack.pop()
                if pre and pre.value > head.value:
                    # 第一个错误点是 左边较大的所以是pre 第二个错误点是 右边较小的 所以是head
                    if res[0] is None:
                        res[0] = pre
                    res[1] = head
                pre = head
                head = head.right
        return res
            
if __name__ == '__main__':
    head14 = Node(5)
    head14.left = Node(3)
    head14.right = Node(7)
    head14.left.left = Node(2)
    head14.left.right = Node(8)
    head14.right.left = Node(6)
    head14.right.right = Node(4)
    head14.left.left.left = Node(1)

    res = BSTChecker.get_wrong_node(head14)
    for node in res:
        print(node.value)