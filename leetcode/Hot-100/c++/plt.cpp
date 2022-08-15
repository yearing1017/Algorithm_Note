#include <iostream>
class Solution {
// n超过45会超过int范围 溢出
public:
    int climbStairs1(int n) {
        int a = 1;
        int b = 1;
        int temp = 0;
        for (int i=0; i<n; i++) {
            temp = a + b;
            a = b;
            b = temp;
        }
        return a;
    }

    int climbStairs2(int n) {
        if (n < 3)
        {
            return n;
        }

        int f0 = 1;
        int f1 = 1;
        int f2 ;
        int i;
        for (i = 2; i <= n; i++)
        {
            f2 = f1 + f0;
            f0 = f1;
            f1 = f2;
        }
        return f2;
    }
};

int main() {
    Solution s;
    std::cout << s.climbStairs2(46) << std::endl;
}