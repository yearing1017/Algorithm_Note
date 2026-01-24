"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
例如：
    输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    输出：true
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # i, j  代表当前的元素的左标 k代表遍历到了第几个
        def dfs(i, j, k):
            # 判断当前i,j是否跨界 当前字符是否和word[k]相同
            if not  0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1: return True
            # 标记访问过
            board[i][j] = ''
            # 四条路 只要满足一个就行
            res = dfs(i+1, j, k+1) or dfs(i, j+1, k+1) or dfs(i-1, j, k+1) or dfs(i, j-1, k+1)
            # 当前字符不满足 回溯
            board[i][j] = word[k]
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0): return True
        
        return False