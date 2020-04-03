class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Parameters
        ----------
        nums : List[int]
        Input array of integers. Guaranteed to have one entry
        without duplicates. All other numbers will appear at least
        twice.

        Returns
        -------
        int
        The entry which appears only once in the array.
        """
        seen = []
        for n in nums:
            if n not in seen:
                seen.append(n)
            else:
                seen.remove(n)

        return seen[0]


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Parameters
        ----------
        nums : List[int]
        Input array of integers. Guaranteed to have one entry
        without duplicates. All other numbers will appear at least
        twice.

        Returns
        -------
        k : int
        The entry which appears only once in the array.
        """
        nums_dict = {}
        
        for n in nums:
            if nums_dict.get(n) is None:
                nums_dict[n] = 1
            else:
                nums_dict[n] += 1
        
        for k, v in nums_dict.items():
            if val == 1:
                return k


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        This function uses bitwises XOR to find the number in the input list
        with only one entry.

        Parameters
        ----------
        nums : List[int]
        Input array of integers. Guaranteed to have one entry
        without duplicates. All other numbers will appear at least
        twice.

        Returns
        -------
        count : int
        The entry which appears only once in the array.
        """
        
        count = 0
        for n in nums:
            count ^= n

        return count
