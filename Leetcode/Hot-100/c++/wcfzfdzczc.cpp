class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(s.size() == 0) return 0;
        int pre = -1, length = 0, cur_len = 0;
        unordered_map<char, int> dic;

        for (int i = 0; i < s.size(); i++) {
            if (dic.find(s[i]) != dic.end()) {
                pre = max(pre, dic[s[i]]);
            }
            // 将s[i]的索引加到字典 或更新索引
            dic[s[i]] = i;
            cur_len = i - pre;
            length = max(length, cur_len);
        }
        return length;
    }
};