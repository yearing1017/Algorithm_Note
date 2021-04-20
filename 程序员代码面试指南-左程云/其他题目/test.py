import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl
import numpy as np

df = pd.read_excel('/Users/yearing1017/IdeaProjects/jupyter/job_key_status.xlsx', engine='openpyxl')
group_result = df.loc[df.click != 0].loc[:,['push_date', 'expName', 'delivered', 'click']]
# 给group_result计算一遍CTR
group_result['CTR'] = (group_result['click'] / group_result['delivered']) * 100

# 取最近7天
date = group_result['push_date'].unique()[-7:]
# 取最近7天的实验
all_7_exp = set()
for d in date:
    group_result_1 = group_result.loc[group_result['push_date'] == d]
    for exp in list(group_result_1['expName'].unique()):
        all_7_exp.add(exp)
all_7_exp = list(all_7_exp)
# print(all_7_exp)
# print(len(all_7_exp))
# print(group_result)
exp_ctr_dic = {}
for exp in all_7_exp:
    exp_ctr_dic[exp] = []
#print(exp_ctr_dic)
for i in range(len(date)):
    temp_df = group_result[group_result['push_date'].isin([(date[i])])]
    for j in range(len(temp_df)):
        exp_ctr_dic[str(temp_df.iloc[j]['expName'])].append(temp_df.iloc[j]['CTR'])
    #判断是否需要补0
    for k in range(len(all_7_exp)):
        if len(exp_ctr_dic[str(all_7_exp[k])]) == i+1:
            continue
        else:
            exp_ctr_dic[str(all_7_exp[k])].append(0)
for exp in all_7_exp:
    print(exp)
    print(exp_ctr_dic[0:2])