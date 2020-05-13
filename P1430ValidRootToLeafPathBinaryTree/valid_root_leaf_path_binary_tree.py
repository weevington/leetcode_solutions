# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        """
        Determines if an array of characters with values '0' or '1' matches
        a valid root-to-leaf path of a given binary tree.

        Parameters
        ----------
        root : TreeNode
            Root node of the binary tree

        Returns
        -------
        is_valid : bool
            True if the 

        Examples
        --------
        Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
           
                             0
                          /     \ 
                         /       \
                        /         \
                      1             0
                   /     \        /
                 0         1     0
                   \      /  \
                    1    0    0
        Output: True
        Explanation:
        The root-to-leaf path 0 -> 1 -> 0 -> 1 is a valid sequence.
        Other valid sequences for this particular binary tree are: 
        0 -> 1 -> 1 -> 0 
        0 -> 0 -> 0

        Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,0,1]
        Output: False 
        Explanation: The root-to-leaf path 0 -> 0 -> 1 does not exist, therefore 
        the sequence in the array is not valid.
        """
        def dfs(root: TreeNode, arr: List[int], k: int, list_len: int) -> bool:
            """
            Helper function to determine if a strin

            """
            # base case to handle being passed in an empty array
            if not root:
                return list_len == 0
            
            # case to handle when  the index k is equal to the last 
            # element of the binary
            if (k == list_len - 1) and\
               (not root.left and not root.right) and\
               (root.val == arr[k]):
                return True

            if k < list_len and root.val == arr[k]:
                return dfs(root.left, arr, k + 1, list_len) or\
                       dfs(root.right, arr, k + 1, list_len)

            return False

        return dfs(root, arr, 0, len(arr))