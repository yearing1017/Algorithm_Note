'''
依据二叉树的前序遍历序列和中序遍历序列建立二叉树
1. 前序：根左右 中序：左根右
2. 根据前序中的根节点来一个一个的建立新节点
    2.1 每次建完根节点，就去建立左子树的根和右子树的根
    2.2 建立左右子树的根，依据根节点在左子树中的索引将前序序列 |根|左子树|右子树| 划分出来
    2.3 找到前序序列中 左右子树的根节点，递归建立
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def rebuild(preorder, inorder):
    
    def recur(root_index, left_index, right_index):
        if left_index > right_index: return
        head = TreeNode(preorder[root_index])
        # 找根节点在中序遍历的位置 得到  前序遍历中左右子树的根节点索引 及左右子树的边界
        i = dic[preorder[root_index]]
        # 下面的参数为 左子树根节点在前序中的位置；左子树在中序中的左右边界
        head.left = recur(root_index + 1, left_index, i-1)
        # 下面的参数为 右子树根节点在前序中的位置；右子树在中序中的左右边界
        # i- left + root + 1 为根节点索引 + 左子树长度 + 1
        head.right = recur(i - left_index + root_index + 1, i+1, right)
        return head
    dic = {}
    for i in range(len(inorder)):
        dic[inorder[i]] = i
    # 参数分别为: 前序根节点索引  当前根节点树下的左边界 右边界
    return recur(0, 0, len(inorder)-1)

