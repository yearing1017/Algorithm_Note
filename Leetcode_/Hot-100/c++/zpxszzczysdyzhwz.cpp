class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        if (nums.size() == 0) {
            return vector<int>{-1, -1};
        }

        int left = biLeft(nums, target);
        int right = biRighft(nums, target);

        if (left<0 || left>=nums.size() || right<0 || right>=nums.size()){
            return vector<int>{-1, -1};
        } else if (nums[left] != target || nums[right] != target) {
            return vector<int>{-1, -1};
        } else {
            return vector<int>{left, right};
        }
    }

    int biLeft(vector<int>& nums, int target) {
        int i = 0;
        int j = nums.size()-1;
        while (i <= j) {
            int m = (i+j) / 2;
            if (nums[m] < target) {
                i = m + 1;
            } else {
                j = m - 1;
            }
        }
        return i;
    }

    int biRighft(vector<int>& nums, int target) {
        int i = 0;
        int j = nums.size()-1;
        while (i <= j) {
            int m = (i+j) / 2;
            if (nums[m] <= target) {
                i = m + 1;
            } else {
                j = m - 1;
            }
        }
        return j;
    }
};