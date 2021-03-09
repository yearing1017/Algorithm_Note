'''
容器盛水问题 给定一个数组arr 代表容器 求可盛多少水
'''

class Water:
    # O(N^2) O(N)
    @classmethod
    def get_water_1(cls, arr):
        # i位置上放的水 = max{min(左最大值， 右最大值)-arr[i], 0}
        if not arr or len(arr) < 3:
            return 0
        res = 0
        # 0和n-1位置一定没有水 不尝试
        for i in range(1, len(arr)-1):
            leftmax = 0
            rightmax = 0

            for k in range(0, i):
                leftmax = max(leftmax, arr[k])

            for m in range(i+1, len(arr)):
                rightmax = max(rightmax, arr[m])

            res += max(min(leftmax,rightmax) - arr[i], 0)
        return res

    # O(N) O(N)
    @classmethod
    def get_water_2(cls, arr):
        # leftmax[i] 代表[0...i]的最大值 rightmax一样
        # i位置上放的水 = max{min(左最大值， 右最大值)-arr[i], 0}
        if not arr or len(arr) < 3:
            return 0
        res = 0

        leftmax = [0] * len(arr)
        leftmax[0] = arr[0]
        for i in range(1, len(arr)):
            leftmax[i] = max(leftmax[i-1], arr[i])
        
        rightmax = [0] * len(arr)
        rightmax[len(arr) - 1] = arr[len(arr) - 1]
        for i in range(len(arr)-2, -1, -1):
            rightmax[i] = max(rightmax[i+1], arr[i])

        for i in range(1, len(arr)-1):
            res += max(min(leftmax[i-1],rightmax[i+1]) - arr[i], 0)
        return res

    # O(N) 0(1)
    @classmethod
    def get_water_3(cls, arr):
        if not arr or len(arr) < 3:
            return 0
        res = 0
        # 由于起始和结尾位置存不住水 不考虑
        leftmax = arr[0] # L左侧的最大值
        rightmax = arr[len(arr) - 1] # R 右侧的最大值
        L = 1
        R = len(arr) - 2
        while L <= R:
            # 此时可求L位置的水
            if leftmax <= rightmax:
                res += max(0, leftmax-arr[L])
                leftmax = max(leftmax, arr[L])
                L += 1
            else:
                res += max(0, rightmax - arr[R])
                rightmax = max(rightmax, arr[R])
                R -= 1
        return res

if __name__ == '__main__':
    arr1 = [3,1,2,5,2,4]
    arr2 = [4,5,1,3,2]
    print(Water.get_water_1(arr1))
    print(Water.get_water_2(arr1))
    print(Water.get_water_3(arr1))
    print(Water.get_water_1(arr2))
    print(Water.get_water_2(arr2))
    print(Water.get_water_3(arr2))

