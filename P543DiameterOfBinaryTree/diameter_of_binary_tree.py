

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    Helper function to find the "height" of a tree. The height is defined to 
    be the longest path from the top-most node, the root, to any leaf node in
    the tree.
    
    This height definition is node count based, such that the height is the 
    largest number of nodes number of nodes from the root 

    """
    def height(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        return 1 + max(self.height(root.left), self.height(root.right))

    """
    Find the "diameter" of the binary tree, where the diameter is defined
    to be the maximum number of edges between any

    """
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
    
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        
        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)
        
        return max(left_height + right_height, max(left_diameter, right_diameter))
        