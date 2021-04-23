'''
找出数组C中加起来等于目标值的所有组合
    1. C中的每个数字在每个组合中只能使用一次
    2. 组合的数字按非递增排序
    3. 结果中不能包含重复的组合
    4. 组合按照字典序排序
输入 [100,10,20,70,60,10,50],80
返回值 [[10,10,60],[10,20,50],[10,70],[20,60]]
'''
def combinationSum2(self , num , target ):
    size = len(num)
    if size == 0:
        return []
    path = []
    res = []
    num.sort()
    dfs(num, 0, size, path, res, target)
    return res
def dfs(num, begin, size, path, res, target):
    if target == 0:
        if path not in res:
            res.append(path)
            return 
    for i in range(begin, size):
        residul = target - num[i]
        if residul < 0:
            # 不排序的话 这里是continue 表示继续遍历下面一个点
            #continue        
            # 排序的话 这里应该是 break 表示之后的点也不再考虑了
            break
        dfs(num, i+1, size, path+[num[i]], res, residul)
