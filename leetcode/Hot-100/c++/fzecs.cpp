/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
 #include<stack>
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (root == nullptr){
            return root;
        }
        stack<TreeNode*> s;
        s.push(root);
        while(!s.empty()){
            int s_size = s.size();
            for(int i=0; i<s_size; i++){
               TreeNode* cur = s.top();
               s.pop();
               if (cur->left) s.push(cur->left);
               if (cur->right) s.push(cur->right);
               TreeNode* temp = cur->left;
               cur->left = cur->right;
               cur->right = temp;
            }
        }
        return root;

    }
};