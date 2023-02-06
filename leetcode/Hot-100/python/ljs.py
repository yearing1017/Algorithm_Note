"""
给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。
提醒一下，二叉搜索树满足下列约束条件：
    节点的左子树仅包含键 小于 节点键的节点。
    节点的右子树仅包含键 大于 节点键的节点。
    左右子树也必须是二叉搜索树。
例如：
    输入：root = [1,0,2]
    输出：[3,3,2]
时间复杂度：O(n)，其中 n 是二叉搜索树的节点数。每一个节点恰好被遍历一次。
空间复杂度：O(n)，为递归过程中栈的开销，平均情况下为 O(logn)，最坏情况下树呈现链状，为 O(n) 
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        # 根据二叉搜索树中序遍历是递增序列，我们进行逆序中序遍历即可
        # 在逆序中序遍历的时候，每次遍历完右子树 将右子树到父节点的值都加和 赋值给父节点
        def dfs(root):
            # nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量
            nonlocal total
            if root:
                dfs(root.right)
                root.val += total
                root.val = total
                dfs(root.left)
        total = 0
        dfs(root)
        return root