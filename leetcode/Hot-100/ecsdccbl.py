"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
例如：
     3
   / \
  9  20
    /  \
   15   7
结果：[[3],[9,20],[15,7]]
"""
class Solution:
    def levelOrder(self, root):   
        res = []
        if not root:
            return res
        queue = [root]
        while queue:
            temp = []
            for _ in range(len(queue)):    
                cur = queue.pop(0)
                temp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(temp)
        return res