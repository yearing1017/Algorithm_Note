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

    int getLength(ListNode* head) {
        int len = 0;
        while(head) {
            ++len;
            head = head->next;
        }
        return len;
    }
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // 伪头结点
        ListNode* dummy = new ListNode(0, head);
        int len = getLength(head);
        ListNode* cur = dummy;

        // len-n+1；cur 1 2 3 4 5 6 倒数第2集正数第5；从dummy移动，找到前一个点
        for (int i = 1; i < len - n +1; i++) {
            cur = cur->next;
        }

        cur->next = cur->next->next;
        ListNode* res = dummy->next;
        delete dummy;
        return res;

    }
};