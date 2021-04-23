# 找出数组中所有相加和为0的三元组，不能重复，元组中数据按递增顺序
def threeSum(num):
    res = []
    length = len(num)
    if not num or length <3:
        return res
    num.sort()

    for i in range(length):
        
        if num[i] > 0: break

        if i > 0 and num[i] == num[i-1]:
            continue

        num.sort()
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
