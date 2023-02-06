"""
你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 
在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 
例如：
    输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
    输出：false
    解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的
思路：
    拓扑排序判断图结构是否为有向无环图；每次将入度为0的点删除，最后判断是否这些点都删除
    pre代表先修课程，cur代表课程结点；统计cur的入度 + 保存pre的邻接矩阵
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 入度表
        indegree = [0 for _ in range(numCourses)]
        # 邻接表
        adj = [[] for _ in range(numCourses)]

        queue = list()
        # 入度表 邻接表的构建
        for cur, pre in prerequisites:
            indegree[cur] += 1
            adj[pre].append(cur)
        # 将入度为0的结点 先进队列
        for i in range(len(indegree)):
            if not indegree[i]: queue.append(i)

        # 遍历队列
        while queue:
            pre = queue.pop(0)
            # 每次遍历完一个入度为0的点 课程数-1
            numCourses -=1
            # 每次删除一个入度的为0的点，对邻接表中该点的邻点入度-1
            for cur in adj[pre]:
                indegree[cur] -= 1
                # 新的入度为0的点加入队列
                if not indegree[cur]:
                    queue.append(cur)
        # 若为有向无环表 则最终的全部的点都会减完
        return not numCourses


    '''
    # 深度优先搜索  O(M+N) O(M+N) 节点数量和临边数量；
    # flag = 0: 未被访问
    # flag = -1: 被其他结点的DFS访问了
    # flag = 1:  被自身结点的DFS访问了
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i, adjacency, flags):
            if flags[i] == -1: return True
            if flags[i] == 1: return False
            flags[i] = 1
            for j in adjacency[i]:
                if not dfs(j, adjacency, flags): return False
            flags[i] = -1
            return True

        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, adjacency, flags): return False
        return True
    '''