'''
求给定二叉树的最大深度，
最大深度是指树的根结点到最远叶子结点的最长路径上结点的数量。
'''


class Solution:
    # 递归法
    #左子树的最大深度 和 右子树的最大深度 比大小，再加上本节点 1 的深度
    def maxDepth_1(self , root):
        # write code here
        if not root: return 0
        left_d = self.maxDepth(root.left)
        right_d = self.maxDepth(root.right)
        return max(left_d, right_d) + 1
    
    def maxDepth_2(self, root):
        queue = [root]
        cnt =  0
        while queue:
            cnt += 1
            for _ in range(len(queue)):
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return cnt