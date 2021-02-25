"""
问题描述，给定一棵二叉树的头结点head,按照如下两种标准分别实现二叉树
边界节点的逆时针打印。
标准一：
1.头结点为边界节点。
2.叶节点为边界节点。
3.如果节点在其所在的层中是最左或者最右的，那么也是边界节点
标准二：
1.头结点为边界节点
2.叶节点为边界节点
3.树左边界延伸下去的路径为边界节点
4.树右边界延伸下去的路径为边界节点

要求：
1）如果节点数为N,两种标准实现的时间复杂度要求为O(N)，额外空间复杂度
要求为O(h),h为树的高度
2）两种标准都要求逆时针顺序且不重复打印所有的边界节点
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class PrintEdgeNode:
    # 求二叉树高度的方法
    @classmethod
    def get_height(cls, head, start):
        if head is None:
            return start
        return max(cls.get_height(head.left, start+1), cls.get_height(head.right, start+1))

    # 层序遍历，求每一层最左及最右对应的元素
    @classmethod
    def set_edge_map(cls, head, level, edgemap):
        if head is None:
            return
        if edgemap[level][0] is None:
            edgemap[level][0] = head
        else:
            edgemap[level][0] = edgemap[level][0]
        edgemap[level][1] = head
        cls.set_edge_map(head.left, level+1, edgemap)
        cls.set_edge_map(head.right, level+1, edgemap)

    # 打印既不是左边界又不是右边界的叶子节点
    @classmethod
    def print_leaf_not_in_map(cls, head, level, edgemap):
        if head is None:
            return

        if head.left is None and head.right is None and head != edgemap[level][0] and head != edgemap[level][1]:
            print(head.value, end=' ')

        cls.print_leaf_not_in_map(head.left, level + 1, edgemap)
        cls.print_leaf_not_in_map(head.right, level + 1, edgemap)

    @classmethod
    def print_way1(cls, head):
        if head is None:
            return
        height = cls.get_height(head, 0)
        edgemap = [[None for _ in range(2)] for _ in range(height)]
        cls.set_edge_map(head, 0, edgemap)
        # 从上到下打印左边界
        for i in range(height):
            print(edgemap[i][0].value, end=' ')
        # 打印既不是左边界又不是右边界的叶子节点
        cls.print_leaf_not_in_map(head, 0, edgemap)
        #从下往上打印右边界（但不是左边界）的结点
        cur = height-1
        while cur>=0:
            if edgemap[cur][0] != edgemap[cur][1]:
                print(edgemap[cur][1].value, end=' ')
            cur -= 1

    # 以标准二打印
    @classmethod
    def print_way2(cls, head):
        if head is None:
            return
        print(head.value, end=' ')

        if head.left and head.right:
            cls.print_left_edge(head.left, True)
            cls.print_right_edge(head.right, True)
        else:
            if head.left:
                cls.print_way2(head.left)
            else:
                cls.print_way2(head.right)
    # 从上到下打印左边界及叶子节点
    @classmethod
    def print_left_edge(cls, head, is_print):
        if head is None:
            return
        #前面的is_print用于判断是否为左边界，后面的判断是否为叶子
        if is_print or (head.left is None and head.right is None):
            print(head.value, end=' ')
        #向左去遍历
        cls.print_left_edge(head.left, is_print)
        #向右遍历打印的情况
        if head.left is None and is_print:
            sec_print = True
        else:
            sec_print = False
        cls.print_left_edge(head.right, sec_print)
    # 从下到上打印右边界及叶子节点
    @classmethod
    def print_right_edge(cls, head, is_print):
        if head is None:
            return
        if head.left is None and is_print:
            sec_print = True
        else:
            sec_print = False
        cls.print_right_edge(head.left, sec_print)

        cls.print_right_edge(head.right, is_print)
        if is_print or (head.left is None and head.right is None):
            print(head.value, end=' ')
    
    




if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.right = Node(4)
    head.right.left = Node(5)
    head.right.right = Node(6)
    head.left.right.left = Node(7)
    head.left.right.right = Node(8)
    head.right.left.left = Node(9)
    head.right.left.right = Node(10)
    head.left.right.right.right = Node(11)
    head.right.left.left.left = Node(12)
    head.left.right.right.right.left = Node(13)
    head.left.right.right.right.right = Node(14)
    head.right.left.left.left.left = Node(15)
    head.right.left.left.left.right = Node(16)
    PrintEdgeNode.print_way1(head)
    print()
    PrintEdgeNode.print_way2(head)