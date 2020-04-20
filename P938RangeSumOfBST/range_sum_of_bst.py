# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    Given the root node of a binary search tree, returns the sum of values
    of all nodes with value between L and R, inclusive.
     
    The binary search tree is guaranteed to have unique values.

    This method is a recursive approach.

    Parameters
    ----------
    root : TreeNode
        Root node of the tree.
    
    Returns
    -------
    bst_range_sum : int

    Examples
    --------
    Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
    Output: 32
    """
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root is None:
            return 0
        
        bst_rangE_sum = self.rangeSumBST(root.left, L, R) +\
            self.rangeSumBST(root.right, L, R)
        if L <= root.val <= R:
            bst_range_sum += root.val
            
        return bst_range_sum 