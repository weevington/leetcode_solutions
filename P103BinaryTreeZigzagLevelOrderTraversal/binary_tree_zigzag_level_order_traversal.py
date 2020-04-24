# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    Returns the zigzag level order traversal of the nodes' values given a 
    binary tree. The tree is traversed from left to right at top level, 
    then then right to left for the next level, alternating in between.

    Parameters
    ----------
    root : TreeNode
        Root node of the input binary tree.

    Examples
    --------
    Input: [3,9,20,null,null,15,7], which represents the binary tree 
                3
               / \
              9  20
                /  \
               15   7
    Output:
       [
        [3],
        [20,9],
        [15,7]
       ]
    """
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        traversal = []
        q = collections.deque()
        q.append(root)
        depth = 0
        
        while q:
            level = []
            num_nodes_in_level = len(q)
            while num_nodes_in_level > 0:
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

                level.append(node.val)
                num_nodes_in_level -= 1

            if level and not depth % 2:
                traversal.append(level)
            else:
                traversal.append(level[::-1])
            depth += 1
        
        return traversal