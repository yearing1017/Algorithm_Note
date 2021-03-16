'''
给定全是小写字母的字符串str，删除多余字符，使得每种字符只保留一个，最终的结构字符串字典序最小
例如：dbcacbca，删掉第一个b，第一个c，第二个c，第二个a，得到dabc，字典序最小

思路：不考虑删除，考虑怎么挑选出k个不同的字符串
'''
class Findstr:
    @classmethod
    def del_find_str(cls, s):
        # 代表26类小写字母的出现次数，-1代表不再考虑
        cipin_map = [0 for _ in range(26)]
        for i in range(len(s)):
            cipin_map[ord(s[i]) - ord('a')] += 1
        #print(cipin_map)
        res = []
        
        L = 0
        R = 0
        while(R != len(s)):
            # 如果当前字符不再考虑 或次数减一之后后面还能出现 直接跳过
            if cipin_map[ord(s[R]) - ord('a')] == -1:
                R += 1
            elif cipin_map[ord(s[R]) - ord('a')] - 1 >0:
                cipin_map[ord(s[R]) - ord('a')] -= 1
                R += 1
            else:
                # 当前字符需要考虑且不会再出现
                # 在s[L...R]上考虑所以需要考虑的字符中，找到ascii最小字符的位置
                pick = -1
                for i in range(L,R+1):
                    if cipin_map[ord(s[i]) - ord('a')] != -1 and (pick == -1 or ord(s[i])<ord(s[pick])):
                        pick = i
                # 把找到的ascii最小的字符放到结果中
                #print(pick)
                res.append(s[pick])
                #print(res)

                # 上一个for循环中 s[L...R]中每种字符的数量都减少了
                # 需要把s[pick+1...R]中每种字符出现的次数加回来
                
                for i in range(pick+1, R+1):
                    # 只增加以后需要考虑的字符
                    if cipin_map[ord(s[i]) - ord('a')] != -1:
                        cipin_map[ord(s[i]) - ord('a')] += 1
                
                #之前选出的ascii最小的 之后就不用考虑了
                cipin_map[ord(s[pick]) - ord('a')] = -1
                # 继续在s[pick+1....]上这个过程
                # 更新L与R
                L = pick + 1
                R = L
        return res



if __name__ == '__main__':
    arr1 = 'dbcacbca'
    res = Findstr.del_find_str(arr1)
    print(res)