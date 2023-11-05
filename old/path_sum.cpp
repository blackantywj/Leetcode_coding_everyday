class Solution {
public:
    bool checkSumPath(TreeNode* root,int leafSumPath, int &targetSum){
        if(root==NULL){
            return false;
        }
        leafSumPath+=root->val;
        if(root->left==NULL && root->right==NULL){
            if(leafSumPath==targetSum)
                return true;
            return false;
        }
        
        return checkSumPath(root->left,leafSumPath,targetSum) || checkSumPath(root->right,leafSumPath,targetSum);
        
    }
    
    bool hasPathSum(TreeNode* root, int targetSum) {
        int leafSumPath=0;
        return checkSumPath(root,leafSumPath,targetSum);
    }
};