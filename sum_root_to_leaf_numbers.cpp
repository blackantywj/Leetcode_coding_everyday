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
// class Solution {
// public:
//     void cal(TreeNode*root,int &ans, string s)
//     {
//         if(!root->left && !root->right)
//         {   
//             cout<<s+to_string(root->val)<<endl;
//             ans=ans+stoi(s+to_string(root->val));
//             return;
//         }
        
//         if(root->left)
//         cal(root->left,ans,s+to_string(root->val));
        
//         if(root->right)
//         cal(root->right,ans,s+to_string(root->val));
//         return;
//     }
//     int sumNumbers(TreeNode* root) {
        
//         if(!root)
//             return 0;
//         int ans=0;
//         string s="";
        
//         cal(root,ans,s);
//         return ans;
//     }
// };


class Solution {
public:
    int sumNumbers(TreeNode* root) {
       int sum = 0;
        if(!root){ return sum; }
        dfs(root, "", sum);
        return sum;
    }
    void dfs(TreeNode* root, string path, int &sum)
    {
        path += to_string(root->val);
        if(!root->left && !root->right)
        {
            sum += stoi(path);
            return;
        }
        if(root->left) { dfs(root->left, path, sum); }
        if(root->right) { dfs(root->right, path, sum); }
        
    }
};