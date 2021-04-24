'''
现在有一个没有重复元素的整数集合S，求S的所有子集
注意：
你给出的子集中的元素必须按升序排列
给出的解集中不能出现重复的元素
'''
class Solution:
    def subsets(self , A ):
        temp = []
        res = []
        def dfs(cur, A):
            if cur == len(A):
                res.append(list(temp))
                return
            # 考虑当前位置
            temp.append(A[cur])
            dfs(cur+1, A)
            temp.pop() # 回溯
            # 不考虑当前位置
            dfs(cur+1, A)
        A.sort()
        dfs(0, A)
        return res