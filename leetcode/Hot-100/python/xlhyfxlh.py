"""
二叉树的序列化：层次遍历存储
反序列化：读取存储的反建二叉树
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''
        queue = [root]
        res = []
        while queue:
            cur = queue.pop(0)
            if cur:
                res.append(str(cur.val))
                queue.append(cur.left)
                queue.append(cur.right)
            else:
                res.append("None")
        return '[' + ','.join(res) + ']'

    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data: return []
        # 去掉两段的[]
        data_list = data[1:-1].split(',')
        # 根节点
        root = TreeNode(int(data_list[0]))
        index = 1
        queue = [root]
        while queue:
            cur = queue.pop(0)
            if data_list[index] != 'None':
                # 构建根节点的左子树
                cur.left = TreeNode(int(data_list[index]))
                queue.append(cur.left)
            index += 1
            if data_list[index] != 'None':
                # 构建根节点的右子树
                cur.right = TreeNode(int(data_list[index]))
                queue.append(cur.right)
            index += 1
        return root
            
