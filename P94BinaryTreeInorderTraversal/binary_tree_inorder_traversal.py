# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        Returns the in-order traversal of a binary tree as an array.

        In-order traversal is defined as evaluating the left node first (if 
        the left node is not None), evaluating the root node, then evaluating
        the right node (if the right node is not None).

        This uses a recursive solution. If the root node is not none, check
        the root's left child by recursively calling the function. Once the 
        root node becomes None, return. Evaluate the current root node and 
        evaluate it and recursively call the function on the current root's 
        right child.

        Parameters
        ----------
        root : TreeNode
            Root node of the binary tree.

        Returns
        -------
        traversal : List[int]
            In-order traversal of the binary tree
        
        Examples
        --------
        Input : [1,null,2,3]
                 1
                  \
                   2
                  /
                 3
        Output : [1,3,2]
        """
        traversal  = []
        def in_order_dfs(root):
            if root is None:
                return

            in_order_dfs(root.left)
            traversal.append(root.val)
            in_order_dfs(root.right)
    
        in_order_dfs(root)
        
        return traversal