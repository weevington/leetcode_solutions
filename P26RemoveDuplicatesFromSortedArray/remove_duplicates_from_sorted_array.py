class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates in a sorted array of integers in place (i.e. the 
        original array is modified). All entries up to a particular length of 
        the array are sorted in increasing order and are not duplicated. Beyond
        that length, it does not matter what is stored in the array.

        This version uses two while loops to determine the breaking condition

        Parameters
        ----------
        nums : List[int]

        Returns
        -------
        length of array up to which the numbers are not duplicated

        Examples
        --------
        Input: [0,0,1,1,1,2,2,3,3,4]
        Output: 5
        """
        lead  = 0
        trail = 0
        
        nums_len = len(nums)

        while lead < nums_len - 1:
            while nums[lead] <= nums[trail]:
                lead += 1
                if lead >= nums_len:
                    break
            else:
                trail += 1
                nums[trail] = nums[lead]

        return trail + 1


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates in a sorted array of integers in place (i.e. the 
        original array is modified). All entries up to a particular length of 
        the array are sorted in increasing order and are not duplicated. Beyond
        that length, it does not matter what is stored in the array.

        A much shorter version using a for loop.

        Parameters
        ----------
        nums : List[int]

        Returns
        -------
        length of array up to which the numbers are not duplicated

        Examples
        --------
        Input: [0,0,1,1,1,2,2,3,3,4]
        Output: 5
        """
        trail = 0
        
        for i, n in enumerate(nums):
            if nums[trail] != nums[i]:
                trail += 1
                nums[trail] = nums[i]

        return trail + 1