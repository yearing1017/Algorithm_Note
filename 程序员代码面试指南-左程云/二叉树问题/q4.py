"""
问题描述：二叉树被记录成文件的过程叫做二叉树的序列化，通过文件内容重建原来二叉树的过程
叫做二叉树的反序列化。给定一棵二叉树的头结点head，并已知二叉树节点值的类型为32位整型，
请设计一种二叉树序列化和反序列化的方案

思路：
1）可以使用先序遍历来做，每个节点用'!'隔开，空节点用'#'表示
2）可以使用层序遍历来做，层序遍历需要结合队列使用
"""
from q3 import PrintTree


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class SerializedTree:
    # 先序遍历-序列化树
    @classmethod
    def serialized_tree(cls, head, res):
        if head is None:
            return '#!'
        res = str(head.value) + '!'
        res += cls.serialized_tree(head.left, res)
        res += cls.serialized_tree(head.right, res)
        return res
    # 先序遍历 反序列化
    @classmethod
    def unserialized_tree(cls, serialized_str):
        if serialized_str.strip() == '' or serialized_str.startswith('#'):
            return None
        res = serialized_str.split('!')
        #print(res)
        queue = list()
        # 将序列化结果加入队列中
        for s in res:
            queue.append(s)
        return cls.recon_pre_order(queue)
    # 通过先序遍历的结果 重建二叉树
    @classmethod
    def recon_pre_order(cls, queue):
        cur = queue.pop(0)
        if cur == '#':
            return None
        cur_node = Node(int(cur))
        cur_node.left = cls.recon_pre_order(queue)
        cur_node.right = cls.recon_pre_order(queue)
        return cur_node
    
    # 层次遍历序列化
    @classmethod
    def serialized_tree_by_level(cls, head, res):
        if head is None:
            return '#!'
        res = str(head.value) + '!'
        queue = list()
        queue.append(head) 
        while queue:
            cur = queue.pop(0)
            if cur.left:
                res += str(cur.left.value) + '!'
                queue.append(cur.left)
            else:
                res += '#!'
            if cur.right:
                res += str(cur.right.value) + '!'
                queue.append(cur.right)
            else:
                res += '#!'
        return res
    
    # 层次遍历反序列化
    @classmethod
    def unserialized_tree2(cls, serialized_str):
        if serialized_str.strip() == '' or serialized_str.startswith('#'):
            return None
        res = serialized_str.split('!')
        return cls.unserialized_tree_by_level(res)
    
    @classmethod
    def unserialized_tree_by_level(cls, res):
        index = 0
        head = cls.generate_node(res[index])
        index += 1
        queue = list()
        if head:
            queue.append(head)
        while queue:
            node = queue.pop(0)
            node.left = cls.generate_node(res[index])
            index += 1
            node.right = cls.generate_node(res[index])
            index += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return head


    @classmethod
    def generate_node(cls, value):
        if value == '#':
            return None
        return Node(value)
            

if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.right.right = Node(5)
    PrintTree.print_tree(head)

    pre = SerializedTree.serialized_tree(head, '')
    print('serialized tree str is ', pre)
    head = SerializedTree.unserialized_tree(pre)
    PrintTree.print_tree(head)

    level = SerializedTree.serialized_tree_by_level(head, '')
    print('serialized2 tree str is ', level)
    head = SerializedTree.unserialized_tree2(level)
    PrintTree.print_tree(head)