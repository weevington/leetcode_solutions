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
     * @brief Returns "vertical order" traversal binary tree nodes' values. 
     *
     * @param root Root node of the input binary tree
     * @return vertical_order vector of vectors containing the node values
     *    visited in "vertical order"
     *
     * This function returns a vector of vector of integers representing the 
     * "vertical order" traversal of a binary tree. The vertical order 
     * traversal groups all nodes that are vertically at the same level. The
     * root node is defined to have level zero. Any nodes left of the root 
     * one level will be grouped as level -1, while any nodes right of the 
     * root one level will be grouped as level 1.
     * 
     * Note that If two nodes are in the same row and column, the order should be from
     * left to right.
     * 
     * The algorithm uses a breadth-first search technique. If the root node 
     * is not none, then add it to a que as a pair with level zero. While the
     * queue is not empty, keep popping off elements of the queue. For each 
     * tree node, if the left child is not null, decrement the left child's 
     * level by one and add to the queue; if the right child is not null 
     * incremenmt the level by one.
     * 
     * A std::map between an integer and a vector of integers is used to keep 
     * track of the nodes at every level. After an element is popped off the 
     * queue, if the level does not appear in the map, a vector is created and
     * the node's value at that level is added to that vector, else, the the
     * node's value is pushed back to the vector.
     * 
     * The map is processed in order since the keys are sorted numerically, 
     * and the vectors corresponding to each key are pushed back to the vector 
     * of vectors that is returned as the result.
     * 
     * Examples:
     * Input: [3,9,20,null,null,15,7]
     * 
     *                 3
     *                / \
     *               /   \
     *              9     20
     *                    /\
     *                   /  \
     *                  /    \
     *                 15     7 
     *
     * Output: [ 
     *           [9],
     *           [3,15],
     *           [20],
     *           [7]
     *         ]
     * Explanation : Node with value 9 is in it's own column. There are no 
     *     nodes above or below it. Node 3 is the first, node at vertical level
     *     zero. The node with value 15 is in the same column as the root node
     *     with value 3, so the second entry in the array representing level 
     *     zero is 15. The node with value 20 is in its own column (nothing is
     *     directly over or under it), so it is in an array by itself. The 
     *     node with value seven is also in its own column, so it is in an
     *     array by itself.
     */
    std::vector<vector<int> > verticalOrder(TreeNode *root) {
        std::vector<std::vector<int> > vertical_order; // return value
        if (root == nullptr) {
            return vertical_order;
        }
        
        // map from vertical "level" to nodes
        std::map<int, std::vector<int> >  vmap; 
        
        std::queue<std::pair<TreeNode*, int> > q;
        // root node is guaranteed to be non-null at this point
        // add it to the queue
        q.push(std::pair<TreeNode*, int>(root, 0));
        
        while (!q.empty()) {
            size_t num_nodes = q.size();
            for (size_t i = 0; i < num_nodes; ++i) {
                // get the pair at the front of the queue
                std::pair<TreeNode*, int> item = q.front();
                TreeNode* curr_node = item.first;
                int curr_level = item.second;
                // pop returns void, do not assign it
                // or there will be errors during compilation
                q.pop();
                
                // if the key does not already exist, make the 
                // corresponding key map to 
                if (vmap.find(curr_level) == vmap.end()) {
                    vmap[curr_level] = std::vector<int>(1, curr_node->val);
                } else {
                    // else if the key alreay exists, just
                    // push it back to the end of the vector
                    vmap[curr_level].push_back(curr_node->val);
                }
                
                // if the left or right child of the current node
                // is not null, then add it to the queue 
                if (curr_node->left != nullptr) {
                    q.push(std::pair<TreeNode*, int>
                        (curr_node->left, curr_level - 1));
                }
                if (curr_node->right != nullptr) {
                    q.push(std::pair<TreeNode*, int>
                        (curr_node->right, curr_level + 1));
                }
            }
        }
      
        std::map<int, std::vector<int> >::const_iterator vmap_iter = vmap.begin();
        const std::map<int, std::vector<int> >::const_iterator vmap_end = vmap.end();
        
        for (; vmap_iter != vmap_end; ++vmap_iter) {
            vertical_order.push_back(vmap_iter->second);
        }
        
        return vertical_order;
    }
};