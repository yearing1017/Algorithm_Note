'''
有选手集合`P={A1,A2,...}`，每个选手有一个或多个技能，所有技能的集合`S={a,b,c,d,e,f,...}`。问题：如何选择最少的选手集合C覆盖所有的技能
思路：贪心法
1. 每次先找技能最多的人  在P中去掉该人  S中去掉该人的技能
2. 重复 上一步 直到S中技能为0
'''

def slove(p, s):
    # p: [[p1,s1], [p2,s2]...[pi,si]]
    # s: [a,b,c...]
    
    p_res = []
    while s:
        for people,skill in p:
            temp_max = 0
            people_del = 0
            if len(skill) > temp_max:
                temp_max = len(skill)
                skill_del = skill
                people_del = people
        p.remove([people_del, skill_del])
        p_res.append(people_del)

    return p_res