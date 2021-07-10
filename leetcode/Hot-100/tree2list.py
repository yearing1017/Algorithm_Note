"""
给你二叉树的根结点 root ，请你将它展开为一个单链表：
展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。
例如：
    输入：root = [1,2,5,3,4,null,6]
    输出：[1,null,2,null,3,null,4,null,5,null,6]
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 思路：先找到当前结点左子树的最右结点  将 当前结点的右子树接到 这个最右节点的 右子树上
        cur = root
        while cur:
            #若有左子树 则找最右节点 因为满足先序遍历
            if cur.left:
                # 保存一下该点
                pre = nex = cur.left
                while pre.right:
                    pre = pre.right
                # 左子树若有右孩子  此时的pre就是左子树的最右节点 若没有 则是 当前左子树根节点
                # 将cur的右子树 挪到 pre的右边
                pre.right = cur.right
                # 左子树置空 题目要求
                cur.left = None
                # 将cur的整个左边挪到 右边 
                cur.right = nex 
            # 继续遍历已调整的右子树的根节点
            cur = cur.right
