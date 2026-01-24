/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int ca = 0, n1 = 0, n2 = 0, n = 0;
        ListNode *dummy = new ListNode(-1), *pre = dummy, *node = nullptr;
        ListNode *cur1 = l1, *cur2 = l2;

        while (cur1 || cur2) {
            n1 = cur1 ? cur1->val: 0;
            n2 = cur2 ? cur2->val: 0;
            n = n1 + n2 + ca;
            node = new ListNode(n % 10);
            pre->next = node;
            pre = node;
            ca = n / 10;
            cur1 = cur1 ? cur1->next : nullptr;
            cur2 = cur2 ? cur2->next : nullptr;
        }

        if (ca == 1) {
            node = new ListNode(1);
            pre->next = node;
        }

        return dummy->next;

    }
};