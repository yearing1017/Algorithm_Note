'''
单调栈系列总结
原问题：给定一个不含有重复值的数组arr，找到每个i位置左边和右边离i位置最近且值比arr[i]小的位置；
进阶问题：在原问题基础上修改为“含有重复值”

解法1：最原始的遍历方法，时间复杂度O(N^2)
解法2and3：单调栈解法，时间复杂度O(N)

注：list.append(object) 向列表中添加一个对象object
list.extend(sequence) 把一个序列seq的内容添加到列表中
'''

class DanDiaoStack:
    @classmethod
    def print_method(cls, res):
        h = len(res)
        l = len(res[0])
        for i in range(h):
            for j in range(l):
                print(res[i][j])
    # 最原始的O(N^2)遍历方法
    @classmethod
    def left_right_way(cls, arr):
        length = len(arr)
        res = [[None for i in range(2)] for j in range(length)]
        # 依次遍历每个位置，得到相应的结果
        for i in range(length):
            leftLessIndex = -1
            rightLessIndex = -1
            # 找左边的值
            cur = i - 1
            while cur >= 0:
                if arr[cur] < arr[i]:
                    leftLessIndex = cur
                    break
                cur -= 1
            # 找右边的值
            cur = i + 1
            while cur < length:
                if arr[cur] < arr[i]:
                    rightLessIndex = cur
                    break
                cur += 1
            res[i][0] = leftLessIndex
            res[i][1] = rightLessIndex
        return res

    # 单调栈1：只处理不含重复值的数组
    @classmethod
    def left_right_stack_1(cls, arr):
        length = len(arr)
        res = [[None for i in range(2)] for j in range(length)]
        DDStack = list()
        for i in range(length):
            while DDStack and arr[DDStack[-1]] > arr[i]:
                popIndex = DDStack.pop()
                leftLessIndex = DDStack[-1] if DDStack else -1
                res[popIndex][0] = leftLessIndex
                res[popIndex][1] = i
            DDStack.append(i)
        #遍历完成之后，最后的清算阶段，剩余的位置的rightLessIndex都为-1
        while DDStack:
            popIndex = DDStack.pop()
            leftLessIndex = DDStack[-1] if DDStack else -1
            res[popIndex][0] = leftLessIndex
            res[popIndex][1] = -1
        return res

    # 单调栈2：处理含重复值的数组;
    @classmethod
    def left_right_stack_3(cls, arr):
        length = len(arr)
        res = [[None for i in range(2)] for j in range(length)]
        DDStack = list()
        for i in range(length):
            # 栈顶元素大于当前位置元素
            while DDStack and arr[DDStack[len(DDStack)-1][0]] > arr[i]:
                # 存的链表
                popIs = DDStack.pop()
                leftLessIndex = DDStack[len(DDStack)-1][len(DDStack[len(DDStack)-1])-1] if DDStack else -1
                for popi in popIs:
                    res[popi][0] = leftLessIndex
                    res[popi][1] = i
            # 栈顶元素等于当前位置元素
            if DDStack and arr[DDStack[len(DDStack)-1][0]] == arr[i]:
                DDStack[-1].append(i)
            else:
                temp = list()
                temp.append(i)
                DDStack.append(temp)
        # 清算阶段
        while DDStack:
            popIs = DDStack.pop()
            leftLessIndex = DDStack[len(DDStack)-1][len(DDStack[len(DDStack)-1])-1] if DDStack else -1
            for popi in popIs:
                res[popi][0] = leftLessIndex
                res[popi][1] = -1
        
        return res

 


           
if __name__ == '__main__':
    
    arr = [3,4,1,5,6,2,7]
    res = DanDiaoStack.left_right_way(arr)
    DanDiaoStack.print_method(res)
    print('========')
    res1 = DanDiaoStack.left_right_stack_1(arr)
    DanDiaoStack.print_method(res1)
    print('========')
    arr_1 = [3,1,3,4,3,5,3,2,2]
    res = DanDiaoStack.left_right_stack_3(arr_1)
    DanDiaoStack.print_method(res)
    '''
    #res = [[None for i in range(7)] for j in range(2)]
    #print(len(res))
    #print(len(res[0]))
    res = list()
    tem = [1,2,3]
    res.append(0)
    res.append(tem)
    print(res)
    '''