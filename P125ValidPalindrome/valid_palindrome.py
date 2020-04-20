class Solution:
    """
    Given a string possibly with multiple trailing and leading spaces, as well
    as spaces between words, determine if it is a palindrome, considering only
    alphanumeric characters and ignoring cases.

    Parameters
    ----------
    s : str
        Input string.

    Returns
    -------
    is_palindrome : bool
        True if the input string is a palindrome, else False.

    Examples
    --------
    Input: "A man, a plan, a canal: Panama"
    Output: True

    Input: "race a car"
    Output: False

    Input: "race   car"
    Output: True
    """
    def isPalindrome(self, s: str) -> bool:
        lo = 0
        hi = len(s) - 1
        s_lc = s.lower()

        while lo < hi:
            if s_lc[lo] == " " or not s_lc[lo].isalnum():
                lo += 1
                continue
            
            if s_lc[hi] == " " or not s_lc[hi].isalnum():
                hi -= 1
                continue

            if s_lc[lo] == s_lc[hi]:
                lo += 1
                hi -= 1
                continue
            
            if s_lc[lo] != s_lc[hi]:
                return False
        
        return True