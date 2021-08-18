'''
给定一个 包含括号的字符串  计算 有效括号数 和 最大嵌套深度
'''
kh_str = '(()(()))'

stack = []
valid_num = 0
max_depth = 0
cur_depth = 0

for s in kh_str:
    if s == '(':
        max_depth = max(max_depth, cur_depth)
        cur_depth = 0
        stack.append(s)
    if s == ')':
        if not stack:
            continue
        else:
            stack.pop()
            valid_num += 1
            cur_depth += 1
# 应对 '(())((()))'
max_depth = max(max_depth, cur_depth)

print(valid_num)
print(max_depth)
