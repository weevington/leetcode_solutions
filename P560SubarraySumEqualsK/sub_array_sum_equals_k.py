class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Brute force method to find the total number of continuous subarrays
        whose sum equals to k. Run time complexity is O(n ^ 3), where n is 
        the number of elements.
        
        Parameters
        ----------
        nums : List[int]
            List of (signed) integers
        
        k : int
            Target integer for sub-arrays to add up to.
    
        Returns
        -------
        num_sums : int
            The total number of continuous subarrays whose sum equals to k.
        """
        num_sums = 0
        
        nums_len = len(nums)
        for i in range(nums_len):
            for j in range(i + 1, nums_len + 1):
                if sum(nums[i:j]) == k:
                    num_sums += 1
        
        return num_sums


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        num_sums = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i + 1, len(nums) + 1):
                sum += nums[i]

                if sum == k:
                    num_sums += 1
        
        return num_sums