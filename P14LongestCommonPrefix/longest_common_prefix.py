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

    Consider the example ["flower","flow","flight"]

    The longest the prefix could be is the length of the shortest string, in
    this case len("flow") = 4. This is the outer loop of our function. In this
    case i goes from 0 to 3. 
    
    i = 0:
    "flower"
     i
    "flow"
     k = 0
    "flight"
     k = 1

    The letters are common at the current position of i (0). We check the 
    second and third strings at position i = 0, and since they are all equal
    to f, we increment the length of the longest common prefix.

    For i = 1, we have:
    i = 1:
    "flower"
      i
    "flow"
      k = 0
    "flight"
      k = 1
    
    Looping over the remaining strings, we see that the character at position
    i in the first string "l" is equal to the characters at position i in the
    second and third strings, we increment the longest common prefix.
    
    i = 2:
    "flower"
       i
    "flow"
       k
    "flight"
       k
    
    Now the character in the first string at position i = 2 is 'o'. While this
    is equal to the character at position i = 2 in the second string ('o' in 
    "flow"), this is not equal to the character at position i = 2 in the third
    string. Therefore, we do not increment the longest common prefix and we
    break from the loop, since the prefix must be continuous and cannot have
    breaks or gaps in the letters which make up the word.

    The time complexity is O(l * n), where l is the length of the shortest word
    in the list, and n is the number of words. 

    Space complexity is O(l), where l is the length of the shortest word. The
    longest common prefix cannot be longer than the shortest word in the list.

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
    Input : ["flower","flow","flight"]
    Output : "fl"

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