class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        //左指针左边均为非零数
        //右指针左边直到左指针处均为零
        int n = nums.size(), left = 0, right = 0;
        while(right < n){
            if(nums[right] != 0){
                swap(nums[left], nums[right]);
                left++;
            }
            right++;
        }
    }
};