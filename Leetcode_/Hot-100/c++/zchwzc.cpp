class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();

        if(n < 2) {
            return s;
        }

        int start = 0;
        int maxLen = 1;
        int curLen = 0;
        // dp[i][j] 表示以A[i]开头和A[j]结尾的字符串是否为回文串
        vector<vector<int>> dp(n, vector<int>(n));
        
        // 初始化：所有长度为 1 的子串都是回文串
        for(int i=0; i<n; i++){
            dp[i][i] = true;
        }

        // 依次从倒数第2个往后判断
        for (int i=n-2; i>=0; i--) {
            for (int j=i+1; j<n; j++) {
                // 首尾字母是否相同 才能满足回文子串的最基本要求
                if (s[i] == s[j]) {
                    if (j-i < 3) {
                        dp[i][j] = true;
                    } else {
                        dp[i][j] = dp[i+1][j-1];
                    }
                }
                // 每次判断完dp[i][j] 都记录一下最长长度
                if (dp[i][j]) {
                    curLen = j-i+1;
                    if (curLen > maxLen) {
                        maxLen = curLen;
                        // 最长回文子串的起始字母的下标
                        start = i;
                    }
                }
            }
        }
    return s.substr(start, maxLen);
    }
};