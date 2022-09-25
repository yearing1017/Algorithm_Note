class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> res(n+1, 0);
        for (int i=1; i<n+1; i++){
            if(i%2 == 1){
                res[i] = res[i-1] + 1;
            }else{
                res[i] = res[i/2];
            }
        }
        return res;
    }
};