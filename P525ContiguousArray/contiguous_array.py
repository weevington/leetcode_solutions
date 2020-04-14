class Solution:
    """
    Given an array containing digits 0 and 1 only, finds 
    the maximum length of a contiguous sub-array with an equal number of 0 and 1.

    This is a brute-force method which uses two loops to go over the array and forms
    all possible sub-arrays. If the length of the sub-array is even, check if the 
    sum of the elements of the array is half the length of the array

    Parameters
    ----------
    nums : List[int]
        List of numbers containing only 0's and 1's.

    Returns
    -------
    contiguous_len : int
        Length of the longest contiguous sub-array with an equal number
        of 0's and 1's.
    
    Examples 
    --------
    Input: [0,1]
    Output: 2

    Input: [0,0, 1, 0, 0, 0, 1, 1]
    Output: 6
    """
    def findMaxLength(self, nums: List[int]) -> int:
        contiguous_len = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                idx_diff = j - i
                if not (idx_diff % 2):
                    t_sum = sum(nums[i:j])
                    if t_sum == (idx_diff // 2):
                        contiguous_len = max(contiguous_len, idx_diff)
        
        return contiguous_len