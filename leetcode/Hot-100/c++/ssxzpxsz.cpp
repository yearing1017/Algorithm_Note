class Solution {
public:
    int search(vector<int>& nums, int target) {
        int length = nums.size();
        int l = 0;
        int r = length - 1;
        int mid;
        while (l <= r) {
            mid = (l + r) / 2;
            if (nums[mid] == target) {
                return mid;
            }

            // 左半区
            if (nums[mid] > nums[r]) {
                // 左半区左
                if (target >= nums[l] and target <= nums[mid]) {
                    r = mid - 1;
                } else {
                    l = mid + 1;
                }
            } else {
                // 右半区右
                if (target >= nums[mid] and target <= nums[r]) {
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            }
        }
        return -1;
    }
};