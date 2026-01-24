class Solution {
public:
    vector<string> generateParenthesis(int n) {
       vector<string> res;
       string temp;
       dfs(temp, n, n, res);
       return res; 
    }

    void dfs(string& temp, int left, int right, vector<string>& res) {
        if (left == 0 && right == 0) {
            res.push_back(temp);
            return;
        }

        if (right < left) {
            return;
        }

        if (left > 0) {
            string cur_temp = temp + '(';
            dfs(cur_temp, left-1, right, res);
        }
        if (right > 0) {
            string cur_temp = temp + ')';
            dfs(cur_temp, left, right-1, res);
        }
    }
};