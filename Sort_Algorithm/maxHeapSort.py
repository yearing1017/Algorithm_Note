class Solution(object):
    def maxHeapify(self, nums, index, heapsize):
        # 从以index开始的树结构 调整堆
        # 大顶堆
        max_index = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left <  heapsize and nums[left] > nums[max_index]:
            max_index = left
        if right < heapsize and nums[right] > nums[max_index]:
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

    def findKthLargest(self, nums, k):
        # 利用堆排序 大顶堆 寻找第k大的数
        # 第一步 初始化堆
        heapsize = len(nums)
        self.buildHeap(nums, heapsize)
        # 第二步 大顶堆只需调整k次 即找到了第k大的数
        for i in range(k-1):
            # 将前k-1大的数 pop出去后 堆顶即为第k大的数
            self.swap(nums, 0, heapsize-1)
            heapsize -= 1
            # 自上而下 调整堆
            self.maxHeapify(nums, 0, heapsize)
        return nums[0]

    def findKLargest(self, nums, k):
        heapsize = len(nums)
        self.buildHeap(nums, heapsize)
        for i in range(k):
            self.swap(nums, 0, heapsize-1)
            heapsize -= 1
            self.maxHeapify(nums, 0, heapsize)
        return nums[-1:-(k+1):-1]

    def heapSort(self, nums):
        # 完整的堆排序
        # 初始化堆
        heapsize = len(nums)
        self.buildHeap(nums, heapsize)
        # 交换堆顶 与 堆尾元素 并调整
        for i in range(heapsize):
            self.swap(nums, 0, heapsize-1)
            heapsize -= 1
            self.maxHeapify(nums, 0, heapsize)
        return nums

if __name__ == "__main__":
    slove = Solution()
    nums = [2,5,3,6,8,1,7,4]
    # 大顶堆 升序
    #print(slove.heapSort(nums))
    # 大顶堆 查找第k大的元素
    #print(slove.findKthLargest(nums, 4))
    print(slove.findKLargest(nums, 4))
