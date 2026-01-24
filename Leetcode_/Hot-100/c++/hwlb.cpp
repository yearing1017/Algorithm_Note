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
    bool isPalindrome(ListNode* head) {
        ListNode* fast = head;
        ListNode* slow = head;
        while(fast->next != nullptr && fast->next->next != nullptr){
            slow = slow->next;
            fast = fast->next->next;
        }

        // 奇数 找到中点  偶数 找到 后半部分的起点
        ListNode* second_head = slow->next;
        slow->next = nullptr;
        ListNode* new_second_head = reverseList(second_head);

        while(head != nullptr && new_second_head != nullptr){
            if (head->val != new_second_head->val){
                return false;
            }
            head = head->next;
            new_second_head = new_second_head->next;
        }
        return true;

    }

    ListNode* reverseList(ListNode* head){
        ListNode* pre = nullptr;
        ListNode* cur = head;
        while(cur != nullptr){
            ListNode* next_node = cur->next;
            cur->next = pre;
            pre = cur;
            cur = next_node;
        }
        return pre;
    }


};