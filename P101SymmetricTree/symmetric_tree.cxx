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
public:

    /**
     * @brief Recursive helper function which determines if a binary \
     *  tree is symmetric or not.
     * 
     * @param a TreeNode*
     * @param b TreeNode*
     * 
     */
    bool is_symmetric_helper(TreeNode *a, TreeNode *b)
    {
        // base case, pointers have recursed all the way down and
        // both left and right tree nodes are NULL
        if (a == nullptr && b == nullptr) {
            return true;
        }

        if ((a == nullptr && b != nullptr) || 
            (a != nullptr && b == nullptr)) {
            return false;
        }

        if (a->val == b->val) {
            return is_symmetric_helper(a->left, b->right) && 
                   is_symmetric_helper(a->right, b->left);
        } 
        
        return false;
    }

    /**
     * @brief Returns whether a binary tree is symmetric or not.
     *
     * A binary tree is symmetric if there exists a plane of symmetry when
     * a line is drawn vertically from the root through the center to the 
     * last level of the tree.
     * 
     * @param a TreeNode*
     * @param b TreeNode*
     */
    bool isSymmetric(TreeNode* root)
    {
        if (root == nullptr)
            return true;

        return is_symmetric_helper(root->left, root->right);    
    }
};