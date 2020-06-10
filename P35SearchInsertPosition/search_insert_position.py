class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Given a sorted array of integers and a target integer value, returns 
        the index if the target is found. If not, returns the index where it 
        would be if it were inserted in order.

        This assumes no duplicates exist in the array.

        Because the values of the array are sorted, this lends itself to a
        binary search problem. We start with three variables which represent
        the bounds of the array or sub-array we are searching for the target.

        Consider the example nums = [1,3,5,6], target = 5

        We have the initial pointers as:
        
                                index  0    1    2    3
                                      [1,   3,   5,   6]
                                       lo   mid       hi
        
        The mid value is obtained by mid = lo + ((hi - lo) // 2); it can also
        be obtained by (lo + hi) // 2, where // indicates integer division. 

        At each iteration we check if the target is equal to nums[mid]. In this
        case the target is 5, which is greater than nums[mid] (value of 3, 
        at index 1). If nums[mid] is less than target, we set lo to mid + 1 and
        repeat. If nums[mid] is greater than target, then we must move high 
        down. The sequence proceeds while low is less than or equal to high.

                                index  0    1    2    3
                                      [1,   3,   5,   6]
                                       lo   mid       hi

                                index  0    1    2    3
                                      [1,   3,   5,   6]
                                                lo    hi
                                                mid
                                
        The iteration stops because nums[mid] (value 5 at index 2) is equal to
        our target.

        Now consider the example nums = [1,3,5,6], target = 2. In this case, 
        the search target is not in the list at all, so we need to be able to 
        handle this case.
        
        The sequence proceeds as 
                                index  0    1    2    3
                                      [1,   3,   5,   6]
                                       lo   mid       hi

                                index  0    1    2    3
                                      [1,   3,   5,   6]
                                       lo
                                       mid
                                       hi
                                
                                index  0    1    2    3
                                      [1,   3,   5,   6]
                                            lo
                                       mid
                                       hi
        The target is not in the listIf we were to return mid in this case, we 
        would not return the correct insertion index to return. Therefore, if 
        the while condition terminates with lo > hi, then we return the index
        lo. 
        
        Parameters
        ----------

        Returns
        --------
        insert_position : int
             Index if the target is found, else returns the index where the 
             target would be if it were inserted in order.
                
        Examples
        --------
        Input: nums = [1,3,5,6], target = 5
        Output: 2

        Input: [1,3,5,6], 2
        Output: 1

        Input: [1,3,5,6], 7
        Output: 4
        """
        # Use a variable so we only need to calculate this
        # once 
        len_nums = len(nums) 
        
        # Edge cases, if the list is empty, insert it at index 0
        if not nums:
            return 0
        # If the target is less than the value at index 0, return index 0
        # and insert it at the beginning
        elif target < nums[0]:
            return 0
        # If the target is greater than the value at the last index, then 
        # return the length of the array (assuming indexing from 0).
        elif target > nums[-1]:
            return len_nums    
            
        lo = 0
        hi = len_nums - 1
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            if nums[mid] == target:
                return mid

            if target < nums[mid]:
                hi = mid - 1
            elif target > nums[mid]:
                lo = mid + 1
        
        # if we still have not found the target and the while loop terminates
        # and lo > hi and hi == mid, then just return lo
        return lo