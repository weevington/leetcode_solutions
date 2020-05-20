
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        Finds an element whose value occurs only once in a given
        array with all other values duplicated.

        A binary search approach is used here

        Parameters
        ----------
        nums : List[int]
            Sorted array of integers. All numbers occur twice except for
            one element value, which occurs only once. The lenth of nums
            is therefore an odd number (i.e. len(nums) % 2 != 0)
        
        Returns
        -------
        non_duplicate : int
            The element whose value occurs only once in the array 
 
        Examples
        --------
        Input : nums = [1,1,2,3,3,4,4,8,8]
        Output : 2
        Explanation : The element 2 at index 2 (counting from 0)
            occurs once.
        
        Input : nums = [3,3,7,7,10,11,11]
        Output : 10
        Explanation : The element 10 at index 4 (counting from 0)
            occurs once.
        """
        lo = 0
        hi = len(nums) - 1
        
        # Do some basic checks before entering the while loop
        # If the array consists of only one element, then return that
        # element.
        if hi == lo:
            return nums[lo]
        # If the value at index 0 is not equal to its neighbor, then 
        # return the first
        if nums[lo] != nums[lo + 1]:
            return nums[lo]
        # If the value at the end of the array is not equal to its 
        # neighbor, then return the value at the end of the array
        if nums[hi] != nums[hi - 1]:
            return nums[hi]
    
        # The stopping condition is when lo is not equal to hi.
        # The equals condition is for the case when lo = mid = hi
        while lo <= hi:
            
            mid = lo + ((hi - lo) // 2)
            
            # check if the value at the index mid is not equal to 
            # the value at the index above mid and is not equal to
            # the value at the index below mid. If the values are not 
            # equal, then the value at the mid index is the value that 
            # occurs only once in the array
            if nums[mid] != nums[mid+1] and nums[mid]!=nums[mid-1]:
                return nums[mid]
            
            # check whether to look left or look right. The array is counted
            # from zero, so pairs of numbers should finish on *odd* indices.
            # If the index pointed to by mid is an even number, it is the first
            # number of what should be a pair. If the value at the mid index is
            # equal to the value at mid index + 1, then the value which 
            # occurs once is between mid and the end of the array.

            # If mid is on an odd index, it should be the second occurrence in 
            # a pair of numbers. If the value at the mid index 
            # is equal to the value at mid index - 1, then the unique value
            # is between mid and the end of the array.
            if (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or\
               (mid % 2 == 1 and nums[mid] == nums[mid - 1]):
                lo = mid + 1
            else:
                hi = mid - 1
        
        return nums[mid]
