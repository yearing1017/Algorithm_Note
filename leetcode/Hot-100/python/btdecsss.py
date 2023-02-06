"""
给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。
思路：
    一个有序序列1...n，为了构造出二叉搜索树，可以遍历每个数字i，以该数字作为树根，左边的序列1...i-1作为左子树；右边的序列i+1...n作为右子树；
    接着安照相同的方法进行递归构建左子树和右子树；在构建过程中，由于根的不同，可以保证二叉搜索树是唯一的。
动态规划公式推导：https://leetcode-cn.com/problems/unique-binary-search-trees/solution/bu-tong-de-er-cha-sou-suo-shu-by-leetcode-solution/
"""
class Solution:
    def numTrees(self, n):
        G = [0] * (n+1)
        G[0] = G[1] = 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]
        return G[n]