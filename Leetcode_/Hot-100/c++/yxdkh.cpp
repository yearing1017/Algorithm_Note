// 20. 有效的括号
#include <iostream>
#include <unordered_map>
#include <stack>
using namespace std;

bool isValid(string s) {
    unordered_map<char, char> kh_map = {
        {'(', ')'},
        {'{', '}'},
        {'[', ']'}
    };

    stack<char> stk;

    for (char ch: s) {
        if (kh_map.count(ch)){
            stk.push(ch);
        } else {
            if (stk.empty() || ch != kh_map[stk.top()]) {
                return false;
            }
            stk.pop();
        }
    }
    return stk.empty();
}

int main(){
    string ss = "()";
    cout << isValid(ss) << endl;
    return 0;
}