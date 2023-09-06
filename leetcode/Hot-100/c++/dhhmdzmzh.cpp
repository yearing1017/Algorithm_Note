class Solution {
public:
    vector<string> res;
    unordered_map<char, string> phoneMap{
            {'2', "abc"},
            {'3', "def"},
            {'4', "ghi"},
            {'5', "jkl"},
            {'6', "mno"},
            {'7', "pqrs"},
            {'8', "tuv"},
            {'9', "wxyz"}
        };
    string temp;
    
    void DFS(int pos, string digits){
        if (pos == digits.size()){
            res.push_back(temp);
            //return;
        } else {
            char digit = digits[pos];
            for (const char& letter: phoneMap[digit]) {
                temp.push_back(letter);
                DFS(pos+1, digits);
                temp.pop_back();
            }
        }

    }
    vector<string> letterCombinations(string digits) {
        
        if (digits.size() == 0) {
            return res;
        }
        DFS(0, digits);
        return res;

    }

    
};