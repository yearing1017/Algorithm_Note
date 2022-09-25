class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        //原地修改 
        int n = nums.size();

        for(int& num: nums){
            int x = (num-1) % n;
            nums[x] += n;
        }
        vector<int> res;
        for(int i=0; i<n; i++){
            if(nums[i] <= n){
                res.push_back(i+1);
            }
        }
        return res;
    }
};