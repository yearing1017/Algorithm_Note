class Solution:
    def solve(self , nums ):
        # write code here   
        #冒泡法
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1], nums[j]
        return nums

if __name__ == "__main__":
    s = Solution()
    nums = [2,5,3,6,8,1,7,4]
    print(s.solve(nums))