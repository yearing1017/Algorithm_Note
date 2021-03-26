# -*- coding:utf-8 -*-

def HeadAdjust(input_list, parent, length):
    '''
		函数说明:堆调整，调整为最大堆,每次只针对以parent为顶的堆
		Parameters:
			input_list - 待排序列表
			parent - 堆的父结点
			length - 数组长度
		Returns:
			无
    '''
    temp = input_list[parent]
    child = (2 * parent)+1
    while child < length:
    # 如果有右孩子，并且右孩子结点的值大于左孩子结点，则选取右孩子结点
        if child + 1 < length and input_list[child] < input_list[child+1]:
            child += 1
    # 比较父节点和孩子的大小，如果不用交换，则退出循环
        if temp >= input_list[child]:
            break
        # 如果需要交换，则交换孩子中大的那个
        input_list[parent], input_list[child]= input_list[child], input_list[parent]
        # 选取孩子结点的左孩子结点,继续向下筛选
        parent = child
        child = 2 * parent + 1
def HeadSort(input_list):
	'''
	函数说明:堆排序（升序）
	Parameters:
		input_list - 待排序列表
	Returns:
		sorted_list - 升序排序好的列表
	'''
	
	if len(input_list) == 0:
		return []
	sorted_list = input_list
	length = len(sorted_list)
    # 这里代表从下往上调整
	for i in range(0, length // 2)[::-1]:
		HeadAdjust(sorted_list, i, length)

	for j in range(1, length)[::-1]:
		temp = sorted_list[j]
		sorted_list[j] = sorted_list[0]
		sorted_list[0] = temp

		HeadAdjust(sorted_list, 0, j)
		print('第%d趟排序:' % (length - j), end = '')
		print(sorted_list)

	return sorted_list

if __name__ == '__main__':
	input_list = [6, 4, 8, 9, 2, 3, 1]
	print('排序前:', input_list)
	sorted_list = HeadSort(input_list)
	print('排序后:', sorted_list)