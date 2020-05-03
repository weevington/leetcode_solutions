# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target_sum: int) -> List[List[int]]:
        """
        Returns 

        This function uses a helper function, dfs, to recursively evaluate
        the path sum. If the root node is not None, the algorithm recurses
        down the left child node (provided it exists) and increments the 
        path sum . The requirement is that the sum be achieved from root node
        to the leaf nodes. If the current node is a leaf node (i.e. both left
        and right child are None), check increment the path sum by the leaf
        node's current value; if the value of the path sum is equal to the
        target_sum, append a list with all node values taken to reach that 
        point.

        Parameters
        ----------
        root : TreeNode
            Root node of the binary tree.

        Returns
        -------
        path_sums : List[List[int]]
            List of integers representing the path taken to reach a given sum of 

        Examples
        --------
        Input: [5,4,8,11,null,13,4,7,2,null,null,5,1] , 22
                     5
                 /      \
                4         8 
               /        /   \
              11      13     4
             /  \           / \
            7    2         5   1
        Output: [
                 [5,4,11,2], 
                 [5,8,4,5]
                ]
        """
        if not root:
            return []

        path_sums = []

        def dfs(root, nodes: List[TreeNode], psum):
            # base case --- leaf node
            if root.left is None and root.right is None:
                if sum(nodes + [root.val]) == tsum:
                #if psum + root.val == tsum:
                    path_sums.append(nodes + [root.val])
                    return
            
            if root and root.left is not None:
                dfs(root.left, nodes + [root.val], psum + root.val)
            if root and root.right is not None:
                dfs(root.right, nodes + [root.val], psum + root.val)
                
        dfs(root, [], 0)
        return path_sums