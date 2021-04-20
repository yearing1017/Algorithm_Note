"""
问题描述：给定一个二叉树的头结点head，已知其中没有重复值的节点，实现两个函数分别判断这棵二叉树是否是
搜索二叉树和完全二叉树。
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class JudgeTool:
    # 中序遍历，搜索二叉树的中序遍历是递增的 若找到当前结点值小于pre，则返回false
    # pre表示每次遍历的结点的前一个结点
    #pre = None
    @classmethod
    def is_bst_tree(cls, head):
        cls.pre = None
        def isBST(root):
            if not root:
                return True
            if not isBST(root.left):
                return False
            if cls.pre and cls.pre.value >= root.value:
                return False
            cls.pre = root
            #print(root.val)
            return isBST(root.right)
        return isBST(head)
    
    @classmethod
    def is_bst_tree2(cls, head):
        stack = []
        pre = float('-inf')
        cur = head
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            if node.value <= pre:
                return False
            pre = node.value
            cur = node.right
        return True

    @classmethod
    def is_bst_tree3(cls, head):
        stack = []
        pre = float('-inf')
        cur = head
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                node = stack.pop()
                if node.value <= pre:
                    return False
                pre = node.value
                cur = node.right
        return True


    @classmethod
    def is_complete_tree(cls, head):
        if head is None:
            return True
        queue = list()
        to_leaf = False
        queue.append(head)
        while queue:
            node = queue.pop(0)
            if node.left and node.right:
                # 该标志代表此处的node该为叶子，所以不该有左右孩子
                if to_leaf:
                    return False
                queue.append(node.left)
                queue.append(node.right)
            elif node.left and not node.right:
                if to_leaf:
                    return False
                #如果某结点只有左孩子 无右孩子 则说明剩下的结点都为叶子结点
                to_leaf = True
                queue.append(node.left)
            # 此情况 表示该树不是完全二叉树
            elif not node.left and node.right:
                return False
            # 左右都为空，说明此处的结点为叶子，剩下的也为叶子
            else:
                if not to_leaf:
                    to_leaf = True
        return True




if __name__ == '__main__':
    head = Node(5)
    head.left = Node(3)
    head.right = Node(6)
    #head.right.left = Node(3)
    head.left.right = Node(4)
    #head.right.left = Node(6)

    print(JudgeTool.is_bst_tree(head))
    print(JudgeTool.is_bst_tree2(head))
    print(JudgeTool.is_bst_tree3(head))
    print(JudgeTool.is_complete_tree(head))