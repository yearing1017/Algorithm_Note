# 找出数组中所有相加和为0的三元组，不能重复，元组中数据按递增顺序
def threeSum(num):
    res = []
    length = len(num)
    if not num or length <3:
        return res
    num.sort()

    for i in range(length):
        # 当前大于0 不需要再考虑之后的
        if num[i] > 0: break
        # 和前一个一样的 去重
        if i > 0 and num[i] == num[i-1]:
            continue
        # 每轮以i位置的数字为基准，遍历后面的数字组合
        L = i+1
        R = length-1

        while L < R:
            ans = num[i] + num[L] + num[R]
            if ans == 0:
                res.append(list(num[i], num[L], num[R]))
                # 去重
                while L<R and num[L]==num[L+1]: L+=1
                while L<R and num[R]==num[R-1]: R-=1
                L += 1
                R -= 1
            elif ans<0:
                L+=1
            else:
                R-=1
        return res
