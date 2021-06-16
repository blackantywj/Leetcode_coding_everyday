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
class Solution {
    
//{a,b} here a = if thief takes current node and b if thief doesn't take current node
public:
    pair<int,int> getans(TreeNode* a)
{
    if(a == NULL) return {0,0};
    
    pair<int,int> l = getans(a->left);
    pair<int,int> r = getans(a->right);
    
    int l1 = l.first ,l2 = l.second ,r1 = r.first,r2= r.second;   
        int t1 = 1,t2 = 1;        // To handle leaves 
        if(a->left !=NULL)t1 = a->left->val;
        if(a->right!=NULL)t2 = a->right->val;
    
    int c = max(l1-t1,l2)+max(r1-t2,r2)+a->val;  
// Max he can take from below and current node, here t1 and t2 are child of current node from which he cant take.  
    int d = max(l1,l2)+max(r1,r2);
// Max he can take from below if he doesnt take current node.
        
        
    
    return {c,d};
}
    
    int rob(TreeNode* root) 
    {
         pair<int,int> a = getans(root);
   return max(a.first,a.second);
        
    }
};