#
# return topK string
# @param strings string字符串一维数组 strings
# @param k int整型 the k
# @return string字符串二维数组
#

class HeapNode:
    def __init__(self, string, times):
        self.string = string
        self.times = times

    

class Solution:
    def topKstrings(self , strings , k ):
        # write code here
        if not strings or k < 1:
            return
        # 生成哈希表 保存词频
        word_counts = dict()
        for s in strings:
            if s in word_counts:
                word_counts[s] += 1
            else:
                word_counts[s] = 1
        
        nums = list()
        for key, value in word_counts.items():
            node = HeapNode(key,value)
            nums.append(node)
        
        heapsize = len(nums)
        self.buildHeap(nums, heapsize)
        
        for i in range(k):
            self.swap(nums, 0, heapsize-1)
            heapsize -= 1
            self.maxHeapify(nums, 0, heapsize)
        
        res = []
        for i in range(len(nums)-1, len(nums)-1-k, -1):
            res.append([str(nums[i].string), str(nums[i].times)])
        return res
    
    def maxHeapify(self, nums, index, heapsize):
        # 从以index开始的树结构 调整堆
        # 大顶堆
        max_index = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left <  heapsize and self.less(nums[left], nums[max_index]):
            max_index = left
        if right < heapsize and self.less(nums[right], nums[max_index]):
            max_index = right
        # 先找到最大的子节点 （大于父节点的）
        if max_index != index:
            self.swap(nums, index, max_index)
            # 再 递归调整这个子堆
            self.maxHeapify(nums, max_index, heapsize)    
        
    # 交换堆中的两个点
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]    
        
    # 从最后一个非叶子节点 开始建堆 一直到堆顶
    def buildHeap(self, nums, heapsize):
        for i in range(heapsize // 2, -1, -1):
            self.maxHeapify(nums, i, heapsize) 

    # 自定义比较两个结点的方法  先比较结点的次数大小 大的 排在前面 次数相等时 比较字典序 小的排在前面
    def less(self, node1, node2):
        if node1.times != node2.times:
            return node1.times > node2.times
        else:
            return node1.string < node2.string   
        
if __name__ == '__main__':
    strings = ["1", "1", "2", "3"]
    k = 2
    s = Solution()
    print(s.topKstrings(strings, k))
        
