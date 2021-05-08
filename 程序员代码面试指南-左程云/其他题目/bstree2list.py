'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
解法：
    1. 拿到二叉搜索树的中序遍历结果
    2. 根据中序遍历结果，将right视作双向链表中的next指针，left视为双向链表中的last指针
'''
class Solution:
    def Convert(self , pRootOfTree):
        if not pRootOfTree:
            return pRootOfTree
        
        queue = list()
        self.visit_mid_order(pRootOfTree, queue)

        head = queue.pop(0)
        pre = head
        while queue:
            cur = queue.pop(0)
            pre.right = cur
            cur.left = pre
            pre = cur
        pre.right = None
        return head



    def visit_mid_order(self, pRootOfTree, queue):
        if pRootOfTree.left:
            self.visit_mid_order(pRootOfTree.left, queue)
        queue.append(pRootOfTree)
        if pRootOfTree.right:
            self.visit_mid_order(pRootOfTree.right, queue)
