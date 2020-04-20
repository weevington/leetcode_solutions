class Solution:
    """
    Given a list of strings, finds the longest common prefix string amongst an
    array of strings. If there is no common prefix, return an empty string "".

    This method first finds the length of the smallest string in the list, as 
    this determines the longest common prefix. A loop over the range of this 
    minimum length serves as the outer loop. Then a loop over all strings in
    the list is performed. If each string contains the same character at a 
    given index, a flag is set to add to the longest common prefix. If not
    the loop breaks and an empty string is returned.

    Parameters
    ----------
    strs : List[str]
       A string representing a Roman numeral.

    Returns
    -------
    common_prefix : str
        The longest common prefix among the strings in the input list. If no 
        common prefix can be found, an empty string is returned.
    
    Examples
    --------
    Input: ["flower","flow","flight"]
    Output: "fl"

    Input: ["dog","racecar","car"]
    Output: ""
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        min_len = min([len(q) for q in strs]) if len(strs) else 0
        
        common_prefix = ""
        for j in range(min_len):
            common_letter = True
            for k in range(len(strs)):
                if k > 0 and strs[k][j] != strs[0][j]:
                    common_letter = False
            if common_letter:
                common_prefix += strs[0][j]
            else:
                break

        return common_prefix