# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Adds two numbers represented as linked lists where digits are stored 
        in reverse order and each of their nodes contain a single digit.

        This assumes numbers do not contain any leading zero, except the
        number 0 itself.

        The sum is formed by adding the values of the node values of the 
        pointers to l1 and l2. If l2 is None and l1 is not None, then the
        value of l1 is taken. A sum is computed at each stage as the result
        of the digits for each node. The digit in the resulting list is
        the sum modulo 10, while the carry is the sum divided by 10. The
        carry is maintained through the iteration of both lists. If the 
        carry is non-zero after the two lists have been iterated over, 
        an additional digit with the carry is appended to the lists. 

        Parameters
        ----------
        l1 : ListNode
            Head node of the first list
        l2 : ListNode
            Head node of the second list

        Returns
        -------
        result : ListNode
            Head node of the return

        Examples
        --------
        Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
        Output: 7 -> 0 -> 8
        Explanation: 342 + 465 = 807.

        Input: (2 -> 1 -> 1) + (9 -> 9)
        Output: 1 -> 2 -> 2
        Explanation: 112 + 99 = 211.
        """
        head = ListNode(0)
        dummy_head = head
        
        total = 0
        carry = 0
        while l1 or l2 or carry:
            total = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            carry = total // 10
            digit = total % 10
            
            head.next = ListNode(digit)
            head = head.next
            
            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next

        return dummy_head.next