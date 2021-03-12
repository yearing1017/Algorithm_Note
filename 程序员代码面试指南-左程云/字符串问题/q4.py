"""
问题描述：给定一个字符串，返回它的统计字符串。比如，"aaabbadddffc"的统计字符串为
"a_3_b_2_a_1_d_3_f_2_c_1".

补充题目：给定一个字符串的统计字符串cstr,再给定一个整数index，返回cstr所代表的原始
字符串上的第index个字符串。例如，"a_1_b_100"所代表的原始字符串上的第0个字符串是'a',
第50个字符串是'b'.
"""


class StrStatistics:
    @classmethod
    def statistics_str(cls, str1):
        if not str1:
            return ""
        res = []
        res.append(str1[0])
        cnt = 1
        for i in range(1, len(str1)):
            if str1[i] != str1[i-1]:
                res.append('{}_{}'.format(cnt, str1[i]))
                cnt = 1
            else:
                cnt += 1
        # 将最后一个字符的数目加上
        res.append(str(cnt))
        return '_'.join(res)

    @classmethod
    def get_char(cls, cstr, k):
        if not cstr:
            return 0
        stage = True # 代表遍历到字符
        cur = 0 # 上次遇到字符阶段 的字符
        num = 0 # 上次遇到字符的数目
        total = 0 # 目前遍历到的位置相当于原字符串的什么位置
        for i in range(len(cstr)):
            if cstr[i] == '_':
                stage = not stage # 转变字符阶段 到 统计出现次数阶段
            elif stage:
                total += num
                if total > k:
                    return cur # 找到为上个阶段的字符
                num = 0
                cur = cstr[i]
            else:
                # 统计阶段 当前字符的数目
                num = num*10 + int(cstr[i])
        # 最后的字符
        if total + num > index:
            return cur
        else:
            return 0


if __name__ == '__main__':
    res = StrStatistics.statistics_str('aaabbadddffc')
    print(res)
    print(StrStatistics.get_char(res, 9))