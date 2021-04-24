"""
问题描述:给定String类型的数组strArr,再给定整数k,请严格按照排名顺序打印
出现次数前k名的字符串

举例:
str=['1', '2', '3', '4'], k=2
No1:1, times: 1
No2:2, times: 1
这种情况下，所有字符串出现一样多，随便打印任何两个字符串都可以

str=['1', '1', '2', '3']
输出:
No1:1, times: 2
No2:2, times: 1
或者:
No1:1, times: 2
No2:3, times: 1

要求:
如果strArr长度为N,时间复杂度请达到O(Nlogk)
"""
# 保存每个字符串和其词频  保存到node结构中
class HeapNode:
    def __init__(self, string, times):
        self.string = string
        self.times = times


class TOKTimesPrinter:
    @classmethod
    def print_top_k(cls, str_arr, k):
        if not str_arr or k < 1:
            return
        # 生成哈希表 保存词频
        word_counts = dict()
        for s in str_arr:
            if s in word_counts:
                word_counts[s] += 1
            else:
                word_counts[s] = 1
        # 特殊情况
        k = min([len(word_counts), k])

        # 遍历哈希表 根据信息决定是否进堆
        heap = [None for _ in range(k)]
        index = 0
        for key, value in word_counts.items():
            # 堆没满k个
            node = HeapNode(key,value)
            if index < k:
                heap[index] = node
                # 直接进堆 并调整
                cls.heap_insert(heap, index)
                index += 1
            else:
                # 此时堆已经够k个了，判断堆顶元素和要插入的元素大小
                if value > heap[0].times:
                    heap[0] = node
                    cls.heapify(heap, 0, k)
        # 此时是个小根堆，将堆的所有元素从大到小排序，即堆顶和队尾交换 并排序
        for i in range(len(heap)-1,-1,-1):
            heap[0], heap[i] = heap[i], heap[0]
            cls.heapify(heap, 0, i)
        
        print('TOP:')
        res = []
        for node in heap:
            temp = [node.string, str(node.times)]
            #print('Str:{} Times:{}'.format(node.string, node.times)) 
            res.append(temp)
        print(res)
    # 堆未满 插入元素并调整为小跟堆的关系
    @classmethod
    def heap_insert(cls, heap, index):
        while index >0:
            parent = (index-1) // 2
            if heap[index].times < heap[parent].times:
                heap[index], heap[parent] = heap[parent], heap[index]
                index = parent
            else:
                break
    # 堆满了 比较堆顶元素和它的大小关系 插入并从上到下进行调整
    @classmethod
    def heapify(cls, heap, index, size):
        left = index *2 +1
        right = index *2 + 2
        smallest = index
        while left < size:
            if heap[left].times < heap[index].times:
                smallest = left
            if right < size and heap[right].times < heap[smallest].times:
                smallest = right
            if smallest != index:
                heap[index], heap[smallest] = heap[smallest], heap[index]
            else:
                break
            # 继续向下调整
            index = smallest
            left = index * 2 +1
            right = index *2 +2

# import heapq
# class Solution:
#     def topKstrings(self , strings , k ):
#         n = len(strings)
#         dic = {}
#         for i in range(n):
#             if strings[i] in dic:
#                 dic[strings[i]] += 1
#             else:
#                 dic[strings[i]] = 1
#         heap = []
#         for num in set(strings):
#             if len(heap) >= k:
#                 if int(heap[0][0]) < dic[num]:
#                     heapq.heapreplace(heap, (num, dic[num]))
#             else:
#                 heapq.heappush(heap, (num, dic[num]))
#         return [[item[0], item[1]] for item in heap]

import heapq
class Solution:
    def topKstrings(self , strings , k ):
        # write code here
        counter = {}
        for ss in strings:
            if ss not in counter:
                counter[ss] = 1
            else:
                counter[ss] += 1
        li = [(-val,key) for key,val in counter.items()]
        print(li)
        heapq.heapify(li)
        print(li)
        ans = []
        for _ in range(k):
            item = heapq.heappop(li)
            ans.append([item[1],-item[0]])
        return ans
if __name__ == '__main__':
    strs = ['1', '1', '2', '3']
    TOKTimesPrinter.print_top_k(strs, 2)
    solve = Solution()
    res = solve.topKstrings(strs, 2)
    print(res)
