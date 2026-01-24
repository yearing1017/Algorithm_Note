class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy = -1e9;
        int sell = 0;

        for (auto p: prices) {
            buy = max(buy, 0-p);
            sell = max(sell, buy+p);
        }

        return sell;

    }
};