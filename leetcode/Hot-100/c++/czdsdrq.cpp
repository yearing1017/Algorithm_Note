class Solution {
public:
    int maxArea(vector<int>& height) {
        int i = 0;
        int j = height.size()-1;

        int res = 0;

        while (i < j) {
            if (height[i] < height[j]) {
                res = max(res, height[i] * (j-i));
                i++;
            } else {
                res = max(res, height[j] * (j-i));
                j--;
            }
        }
        return res;
    }
};