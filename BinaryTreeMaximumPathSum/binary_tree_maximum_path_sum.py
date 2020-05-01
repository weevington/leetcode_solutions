# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxPathSum(self, root: TreeNode) -> int:
        """
        Returns the maximum path sum between any sequence of nodes in a binary
        tree.

        For this problem, a path is defined as any sequence of nodes from some 
        starting node to any node in the tree along the parent-child 
        connections. The path must contain at least one node and does not need
        to go through the root.

        Parameters
        ----------
        root : TreeNode
            Root node of a non-empty binary tree
        
        Returns
        -------
        max_path_sum : int
            Maximum sum between any two nodes in the binary tree.
        
        Examples
        --------
        Input: [1, 2, 3]
              1
             / \
            2   3
        Output: 6

        Input: [-10,9,20,null,null,15,7]
               -10
               /  \
              9   20
                 /  \
                15   7
        Output: 42
        """
        max_path_sum = float("-inf")
        def max_sum_helper(root) -> int:
            nonlocal max_path_sum
            if root is None:
                return 0

            left_sum  = max(max_sum_helper(root.left), 0)
            right_sum = max(max_sum_helper(root.right), 0)

            current_sum = root.val + left_sum + right_sum
            
            test_sum = max(root.val + left_sum, root.val + right_sum)
                        
            max_path_sum = max(max_path_sum, current_sum)
            
            return test_sum
        # end nested function

        max_sum_helper(root)
 
        return max_path_sum