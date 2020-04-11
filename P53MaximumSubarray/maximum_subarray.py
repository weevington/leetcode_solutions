

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Parameters
        ----------
        nums: List[int]
            Input array of integers.

        Returns
        -------
        max_subsum : int
            Maxiumum sub value of all sub-arrays contained in nums. 
        """
        if len(nums) == 0:
            return 0 
        if len(nums) ==1 :
            return nums[0]
        
        
        test_max = nums[0]
        max_subsum = nums[0]

        for i in range(1, len(nums)): 
            test_max = max(nums[i], test_max + nums[i])
            max_subsum = max(test_max, max_subsum) 
            
        return max_subsum