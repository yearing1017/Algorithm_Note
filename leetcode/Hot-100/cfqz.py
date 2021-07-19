"""
给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）

解法：使用到了前缀和的概念；每次遍历的root结点，当做起点，往下遍历时，记录到下个点的和
sumlist[]记录当前路径上的和，在如下样例中：
      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1
当DFS刚走到2时，此时sumlist[]从根节点10到2的变化过程为：
10
15 5
17 7 2
当DFS继续走到1时，此时sumlist[]从节点2到1的变化为：
18 8 3 1
因此，只需计算每一步中，sum在数组sumlist中出现的次数，然后与每一轮递归的结果相加即可
"""
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def dfs(root, sumlist):
            # 递归终止条件
            if not root: return 0
            # 计算当前结点 和 之前的前缀和 相加的和; 并将当前结点的值拼接到后面
            sumlist = [num + root.val for num in sumlist] + [root.val]
            # 计算目标sum出现的次数
            count = 0
            for num in sumlist:
                if num == sum:
                    count += 1
            # 递归计算左右子树下
            return count + dfs(root.left, sumlist) + dfs(root.right, sumlist)
        return dfs(root, [])


