class Solution {
public:
    int hammingDistance(int x, int y) {
        // x 和 y 先进行异或操作 然后不断右移一位，计算1的个数
        int s = x ^ y, ret = 0;
        while (s) {
            // 按为与操作 1&0=0 1&1=1
            ret += s & 1;
            // 右移一位  最左补0
            s >>= 1;
        }
        return ret;
    }
};