# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        """
        Returns the middle node of a non-empty, singly linked list, return the middle node.

        If there are two middle nodes (i.e. the number of nodes in the linked list is even), 
        the second middle node is returned (i.e. the node at index floor(n / 2) + 1). 

        Parameters
        ----------
        head : ListNode
            Head node of the linked list.

        Returns
        -------
        slow : ListNode
            Middle node of the linked list.
        
        Examples
        --------
        Input: [1,2,3,4,5]
                1 -> 2 -> 3 -> 4 -> 5 -> None
        Output: Node with value 3

        Input: [1,2,3,4,5,6]
                1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
         Output: Node with value 4
        """
        fast = head
        slow = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow