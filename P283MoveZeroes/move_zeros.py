class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Given an array of integers move all 0's to the end of it 
        while maintaining the relative order of the non-zero elements.
        
        Parameters
        ----------
        nums : List[int]
            Array containing natural numbers
        
        Examples
        --------
        Input: [0,1,0,3,12]
        Output: [1,3,12,0,0]

        Input: [0, 0]
        Output: [0, 0]
        """
        def find_non_zero(a: List[int], k: int, nl: int) -> int:
            non_zero_index = -1 
            for j in range(k, nl):
                if a[j] != 0:
                    non_zero_index = j
                    break

            return non_zero_index
        
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        for i in range(nums_len):
            if nums[i] == 0:
                nzi = find_non_zero(nums, i, nums_len)
                if nzi != -1:
                    nums[nzi], nums[i] = nums[i], nums[nzi]


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        

        """
        pos = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1

