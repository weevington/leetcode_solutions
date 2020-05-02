# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    """
    Returns whether a binary tree is symmetric or not.

    A binary tree is symmetric if there exists a plane of symmetry when
    a line is drawn vertically from the root through the center to the 
    last level of the tree.

    Parameters
    ----------
    root : TreeNode
        Root node of the binary tree.

    Returns
    -------
    is_symmetric : bool
        Whether the binary tree is symmetric or not.

    Examples
    --------
    Input : [1,2,2,3,4,4,3]
              1
             / \
            2   2
           / \ / \
          3  4 4  3
    Output : True
 
    Input : [1,2,2,null,3,null,3]
              1
             / \
            2   2
             \   \
             3    3
    Output : True
    
    Input : [1,17,17,5,null,null,5]
              1
             / \
           17   17
           /     \
          5       5
    Output : True
    """
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def is_symmetric_helper(node_a, node_b) -> bool:
            if node_a is None and node_b is None:
                return True
            elif node_a is not None and node_b is None: 
                return False
            elif node_b is not None and node_a is None:
                return False

            if node_a.val == node_b.val:
                return is_symmetric_helper(node_a.left,  node_b.right) and \
                       is_symmetric_helper(node_a.right, node_b.left)

            return False

        return is_symmetric_helper(root.left, root.right)