# 根据二叉树的前序中序遍历，重建二叉树，并打印树的右视图（只打印树的最右边的结点）

class ListNode:
    def __init__(self, num):
        self.val = num
        self.left = None
        self.right = None

class Solution:
    def solve(self , xianxu , zhongxu ):
        # write code here
        
        def recur(root, left, right):
            if left > right:
                return
            node = ListNode(xianxu[root])
            i = dic[xianxu[root]]
            node.left = recur(root + 1, left, i-1)
            node.right = recur(i - left + root + 1, i + 1, right)
            return node
        def yst(head):
            stack = [head]
            res = []
            while stack:
                # 此处是打印右视图的关键
                res.append(stack[-1].val)
                cnt = len(stack)
                for _ in range(cnt):
                    cur = stack.pop(0)
                    if cur.left:
                        stack.append(cur.left)
                    if cur.right:
                        stack.append(cur.right)
            return res
        dic = dict()
        res = []
        xianxu = xianxu
        zhongxu = zhongxu
        for i in range(len(zhongxu)):
            dic[zhongxu[i]] = i
        head = recur(0, 0, len(zhongxu)-1)
        res = yst(head)
        return res