"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。

说明：
所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
例如：
    输入: candidates = [10,1,2,7,6,1,5], target = 8,
    所求解集为:
    [
        [1, 7],
        [1, 2, 5],
        [2, 6],
        [1, 1, 6]
    ]
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, begin, size, path, res, target):
            if target == 0:
                #  判断是否有重复的
                if path not in res:
                    res.append(path)
                    return
            for i in range(begin, size):
                residul = target - candidates[i]
                if residul < 0:
                    # 不排序的话 这里是continue 表示继续遍历下面一个点
                    #continue
                    break
                    # 排序的话 这里应该是 break 表示之后的点也不再考虑了
                # i+1 表示当前数字不能使用多次
                dfs(candidates, i+1, size, path + [candidates[i]], res, residul)
        
        size = len(candidates)
        if size == 0:
            return []
        path = []
        res = []
        candidates.sort()
        dfs(candidates, 0, size, path, res, target)
        return res