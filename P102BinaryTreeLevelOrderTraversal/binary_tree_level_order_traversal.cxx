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
     * @brief Returns values of a binary tree in a level-order traversal 
     * 
     * @param root TreeNode* 
     *     Root node of binary Tree
     * 
     * @return traversal std::vector<std::vector> >*
     *     Vector of vectors containing node values in level-order
     */ 
    std::vector<std::vector<int> > levelOrder(TreeNode *root) {
        std::vector<std::vector<int> > traversal;
        
        if (root == nullptr)
            return traversal;

        std::queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            size_t level_size = q.size();
            std::vector<int> level_values;
            
            while (level_size) {
                const TreeNode *node = q.front();
                q.pop();
                
                if (node->left != nullptr)
                    q.push(node->left);

                if (node->right != nullptr)
                    q.push(node->right);

                --level_size; 
                level_values.push_back(node->val);
            }
            traversal.push_back(level_values);
        }

        return traversal;
    }
};