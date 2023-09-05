class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        int len = nums.size();
        if (len < 3) {
            return res;
        }
        // 先排序  之后遍历遇到正数即可停止
        sort(nums.begin(), nums.end());
        for (int i = 0; i < len; i++) {
            if (nums[i] > 0) {
                break;
            }
            // 去重
            if (i > 0 && nums[i] == nums[i-1]) {
                continue;
            }
            // 定住第一个数的同时  从右边开始两边向中间缩
            int left = i + 1;
            int right = len - 1;
            while (left < right) {
                if (nums[i] + nums[left] + nums[right] == 0) {
                    res.push_back({nums[i], nums[left], nums[right]});
                    // 去重
                    while (left < right && nums[left] == nums[left+1]) {
                        left += 1;
                    }
                    while (left < right && nums[right] == nums[right-1]) {
                        right -= 1;
                    }
                    // 去重完还要移动一次
                    left += 1;
                    right -= 1;
                } else if (nums[i] + nums[left] + nums[right] < 0) {
                    left += 1;
                } else {
                    right -= 1;
                }
            }
        }
        return res;
    }
};