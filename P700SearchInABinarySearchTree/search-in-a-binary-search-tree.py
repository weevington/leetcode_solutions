# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        Given the root node of a binary search tree (BST) and a target value to
        search for, returns the sub-tree where the root node has value equal
        to the target.

        If the target value is not found, we return None.

        Consider the example searching for the value 2 in the following tree.
                                   ->  4
                                     /   \
                                    2     7
                                   / \
                                  1   3

        Because this is a binary search tree, and the target value is less than
        the the root node value, we move to the left. 

        So root now points to the value with 2 and we return that node.

                               ->   2
                                   / \
                                  1   3

        Parameters
        ----------
        root : TreeNode
            Root node of the BST.
        val : int
            Target value to search for.

        Returns
        -------
        target_root : TreeNode
             Sub-tree of the original binary search tree where the value of the
             root node is equal to the target value.

        Examples
        --------
        Input : 

        """
        if root is None:
            return None
        
        if root.val == val:
            return root
        
        if val < root.val:
            return self.searchBST(root.left, val)
        if val > root.val:
            return self.searchBST(root.right, val)