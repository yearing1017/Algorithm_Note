# 求类似“NNYYYYYNNYY”中最长的连续Y的序列的长度

def calDPDScore(dpdInfo) :
    # write code here
    max_len = 0
    cur_max = 0
    l = 0
    start = False
    while l < len(dpdInfo):
        if dpdInfo[l] == 'Y':
            start = True
            while l < len(dpdInfo) and dpdInfo[l] == 'Y' and start:
                cur_max += 1
                l += 1
        else:
            start = False
            if cur_max > max_len:
                max_len = cur_max
            cur_max = 0
            l += 1
        
    
    max_len = max(cur_max, max_len)
    
    if  max_len == 0:
        return 0
    elif 0 < max_len <= 3: 
        return -10
    elif  3 < max_len <= 7:
        return -15
    else:
        return -25

s = "NNYYYYYNNYY"
print(calDPDScore(s))
