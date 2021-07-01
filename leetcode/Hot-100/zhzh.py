"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。
例如：
    输入：candidates = [2,3,6,7], target = 7,
    所求解集为：
    [
        [7],
        [2,2,3]
    ]
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 递归函数 每次都从当前数不断重复尝试
        def dfs(candidates, begin, size, path, res, target):
            # 递归结束
            if target == 0:
                res.append(path)
                return
            # 从当前数递归遍历
            for i in range(begin, size):
                residul = target - candidates[i]
                if residul < 0:
                    # 不对数组事先排序的话 就要continue尝试下一个数 若排序了 直接break
                    continue
                dfs(candidates, i, size, path + [candidates[i]], res, residul)
        
        size = len(candidates)
        if size == 0:
            return []
        res = []
        path = []
        #candidates.sort()
        dfs(candidates, 0, size, path, res, target)
        return res