# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        Returns kth smallest element in a binary search tree (BST), where
        k is a positive integer no more than the number of valid non-null
        nodes in a tree.

        The approach is based on an in-order traversal. An in-order traversal
        of a binary search tree will yield the node values in sorted order.

        One way to do this is to have an array which stores the nodes as the
        tree is traversed. After the nodes are appended to the array, check
        the (k - 1)th element from the start, i.e. if k = 2, then return the
        1st element in the array . This approach incurs O(N) extra space, 
        where N is the number of nodes in the array.

        In order to remove the O(N) space complexity, a counter and a flag
        which indicates if/when you have found the kth smallest element

        Parameters
        ----------
        root : TreeNode
            root node of the BST
        
        k : int 
            index (1-based) of the value of the kth smallest node in the binary
            search tree

        Returns
        -------
        kth_smallest : int
            kth smallest node value in the binary tree

        Examples
        --------
        Input : root = [3,1,4,null,2], k = 1
                   3
                /     \
              1         4
                \
                  2
        Output : 1
        Explanation : The in-order traversal gives [1, 2, 3, 4]. The 1st
            smallest element is at index 0, which gives 1.
        
        Input : root = [5,3,6,2,4,null,null,1], k = 3
                    5
                 /     \
                3       6
               /  \
              2    4
             /
            1
        Output : 3
        Explanation : The in-order traversal gives [1, 2, 3, 4, 5, 6]. The 3rd
            smallest element is at index 2, which gives 3.
  
        """

        def in_order(root: TreeNode) -> int:
            """
            The in-order traversal first looks at the root node's left child
            node, then the root node, then the root node's right child node.
            The function descends down even if the left child node is None,
            but the count is not incremented. The count is incremented between
            calls to visit the left and right children.

            There is no reason to visit the right child if the kth smallest
            node is found, so only call the in-order traversal if the flag
            which indicates the kth smallest node has been found is not set.
            If the flag is set, just return the value from the traversal of
            the left hand side.
            """

            # because these are integers, variable values will not persist
            # across recursive function calls. In order to allow for state
            # persistence, we make these variables "nonlocal". Another way
            # could be to make these variables member variables of a class
            nonlocal found_smallest
            nonlocal node_count

            if root is None:
                # Ideally this should be -int_max or a sentinel value
                # indicating that you have not encountered the kth element
                # One bad thing associated with just returning zero is that
                # if you allow for negative numbers in the binary tree, and
                # there is actually an element with value zero, it could give
                # false positives if 0 actually is the kth smallest element.
                return 0 
            
            left = in_order(root.left)
            node_count += 1

            if node_count == k:
                # if you have found the kth smallest value, set the flag to True
                # There is no need to pursue other
                found_smallest = True
                return root.val
            
            if found_smallest:
                return left
            else:
                return in_order(root.right)

        # ensure that we are only looking at strictly positive values of k
        assert(k > 0)

        node_count = 0
        found_smallest = False
        
        return in_order(root)