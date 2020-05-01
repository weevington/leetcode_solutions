# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None
        elif l2 is None:
            return l1
        elif l1 is None:
            return l2

        dummy_res = ListNode()
        dummy_res.next = None
        res = dummy_res

        if l1.val <= l2.val:
            res = l1
            l1 = l1.next
        else:
            res = l2
            l2 = l2.next

        dummy_res.next = res

        while l1 or l2:
            if l1 is None and l2 is not None:
                res.next = l2
                l2 = l2.next
                res = res.next
            elif l2 is None and l1 is not None:
                res.next = l1
                l1 = l1.next
                res = res.next
            else:
                if l1.val <= l2.val:
                    res.next = l1
                    l1 = l1.next
                    res = res.next
                else:
                    res.next = l2
                    l2 = l2.next
                    res = res.next

        return dummy_res.next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Merges two sorted linked lists into a single sorted list.

        This is a shorter solution than the above. It uses an iterative 
        approach (as opposed to a recursive approach). If either of the lists
        is None, return the pointer to that list. Create a dummy node which 
        serves as a handle to the first node of the resulting list. Set the 
        dummy node's next pointer to the current head of the first list if the 
        value of the head node of the first list is less than or equal to the
        value of the second list. Advanced the pointer to the current node 
        of the first list and advance the pointer to the current node of the
        resulting list.

        Parameters
        ----------
        l1 : ListNode
            Head node of the first list to be merged.
        l2 :
            Head node of the second list to be merged.
        
        Returns
        -------
        res : ListNode
            Pointer to the head of the resulting linked list after merging.
        
        Examples
        --------
        Input : l1 = [1,2,3,4,5,6,7,8,9,10]
                l2 = [1,3,4]
        Output : [1,1,2,3,3,4,4,5,6,7,8,9,10]

        Input : l1 = [1,2,7,9]
                l2 = []
        Output : [1,2,7,9]

        Input : l1 = [1,3,5,7] 
                l2 = [2,4,6]
        Output :[1,2,3,4,5,6,7]
        """
        if not l1:
            return l2
        elif not l2:
            return l1

        # this is slightly bad style to use a list Node with
        # a sentinel value 
        dummy_head = ListNode(-1) 
        dummy_head.next = l1 if l1.val <= l2.val else l2
        res = dummy_head

        while l1 and l2:
            if l1.val <= l2.val:
                res.next = l1
                l1 = l1.next
            else:
                res.next = l2
                l2 = l2.next
                
            res = res.next
                    
        if not l1:
            res.next = l2
        elif not l2:
            res.next = l1
            
        return dummy_head.next