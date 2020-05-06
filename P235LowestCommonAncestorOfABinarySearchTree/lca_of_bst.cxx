/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    /**
     *  @brief Finds the lowest common ancestor of a binary search tree
     * 
     *  @param root Root node of binary search tree
     *  @param p First number in range of binary search tree
     *  @param q Second number in range of binary search tree  
     */
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q)
    {    
        if (root == nullptr || (p == nullptr && q == nullptr)) {
            return root;
        }
        
        if (p->val > root->val && q->val > root->val) {
            return lowestCommonAncestor(root->right, p, q);
        } else if (p->val < root->val && q->val < root->val) {
            return lowestCommonAncestor(root->left, p, q);
        } else {
            return root;
        }
    }
};