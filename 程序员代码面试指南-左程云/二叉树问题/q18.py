"""
问题描述：给定一棵二叉树的的头结点head，以及这棵树中的两个节点o1和o2，
请返回o1和o2的最近公共祖先节点。
"""
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class AncestorFinder:
    @classmethod
    def find_ancestor_by_recurise(cls, head, node1, node2):
        if not head or head == node1 or head == node2:
            return head
        left = cls.find_ancestor_by_recurise(head.left, node1, node2)
        right = cls.find_ancestor_by_recurise(head.right, node1, node2)
        if left and right:
            return head
        elif left and not right:
            return left  
        elif not left and right: 
            return right
        else:
            return None

    @classmethod
    def find_ancestor_by_val(cls, root, o1, o2):
        # @param root TreeNode类 
        # @param o1 int整型 
        # @param o2 int整型 
        # @return int整型
        if not root or root.val == o1 or root.val == o2:
            return root.val if root else None
        left = cls.lowestCommonAncestor(root.left, o1, o2)
        right = cls.lowestCommonAncestor(root.right, o1, o2)
        if left and right:
            return root.val
        elif not left and right:
            return right
        elif not right and left:
            return left
        else:
            return None

    @classmethod
    def find_ancestor_by_hash(cls, head, node1, node2):
        hash_table = dict()
        if head:
            hash_table[head] = None
        cls.construct_hash_table(head, hash_table)
        node_list = list()
        parent1 = hash_table[node1]
        # 将node1的本身和到头结点的所有父节点找到
        while parent1:
            node_list.append(parent1)
            parent1 = hash_table[parent1]
        
        while node2:
            if node2 in node_list:
                return node2
            node2 = hash_table[node2]


    @classmethod
    def construct_hash_table(cls, head, hash_table):
        #hash_table = dict()
        if not head:
            return
        if head.left:
            hash_table[head.left] = head
        if head.right:
            hash_table[head.right] = head
        cls.construct_hash_table(head.left, hash_table)
        cls.construct_hash_table(head.right, hash_table)

if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.left.right = Node(5)
    head.right.left = Node(6)
    head.right.right = Node(7)
    head.right.right.left = Node(8)

    o1 = head.right.right.left
    o2 = head.right.left

    print("o1 : " + str(o1.value))
    print("o2 : " + str(o2.value))
    print("ancestor : " + str(AncestorFinder.find_ancestor_by_recurise(head, o1, o2).value))
    print("ancestor : " + str(AncestorFinder.find_ancestor_by_hash(head, o1, o2).value))
    print("===============")