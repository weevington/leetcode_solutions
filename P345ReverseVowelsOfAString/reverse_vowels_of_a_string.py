class Solution:
    """
    Reverses the vowels of a string.

    This method uses two pointers, one starting from the beginning of the
    array, and one starting from the end of the array. While the index of 
    the beginning pointer is less than the index of the end pointer, the 
    string contents at that index are checked; the beginning pointer is
    advanced and the end pointer is decremented. If the characters at both 
    indices are vowels, the elements are swapped.

    Parameters
    ----------
    s : str
        Input string.

    Returns
    -------
    t : str
        Input string with vowels reversed. If the string contains no vowels,
        the original string is returned.

    """
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        
        t = list(s)
        lo = 0
        hi = len(s) - 1
        
        while lo < hi:
            if t[lo] not in vowels:
                lo += 1

            if t[hi] not in vowels:
                hi -= 1
            
            if t[lo] in vowels and t[hi] in vowels:
                t[lo], t[hi] = t[hi], t[lo]
                lo += 1
                hi -= 1

        return "".join (t)