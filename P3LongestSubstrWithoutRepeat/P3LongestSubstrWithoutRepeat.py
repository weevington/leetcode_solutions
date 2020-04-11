class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Return the length of the longest substring without repeating characters
        contained within a given string. This method uses a set to store "seen"
        characters in the string.
        
        Two pointers are used in this method, one leading pointer, and one 
        trailing pointer. While the lead pointer is less than the length of 
        the string, check if the character at the leading pointer 
        index is already contained in the set. If it is, remove the character
        at the trailing index. 

        Parameters
        ----------
        s : str
            Input string

        Returns
        -------
        lls : int
            Length of the longest substring without repeating characters

        Examples
        --------
        Input: "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.
        """
        lls = 0 # length of longest substring
        charset = set()
        lead_idx = 0
        trail_idx = 0
        while lead_idx < len(s):
            if not s[lead_idx] in charset:
                charset.add(s[lead_idx])
                lead_idx += 1
                lls = max(lls, len(charset))
            else:
                charset.remove(s[trail_idx])
                trail_idx += 1
                
        return lls


class Solution:
        """
        Return the length of the longest substring without repeating characters
        contained within a given string. This method uses a set to store "seen"
        characters in the string.
        
        This method uses a dictionary (hashmap) as opposed to a set (hashset). 
        A for loop goes over each character in the string. If that character
        exists as a key in the dictionary, calculate a new index 1 after the 
        occurrence of that character and set that as the new start index only
        if that new index is greater than the current start index of the 
        longest substring. For each iteration, calculate a length to evaluate
        the longest substring by using the max function of the current length
        of the longest substring (lls) and the new sequence length.

        Parameters
        ----------
        s : str
            Input string

        Returns
        -------
        lls : int
            Length of the longest substring without repeating characters

        Examples
        --------
        Input: "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.

        Input: "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3. Alternatively,
            "kew" would also be an acceptable answer. 
        """
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chardict = {}
        lls = 0 # length of longest substring
        start_idx = 0
        
        for i, c in enumerate(s):
            if c in chardict:
                rpt_idx = chardict[c] + 1
                if rpt_idx > start_idx:
                    start_idx = rpt_idx
            test_len = i - start_idx + 1
            lls = max(test_len, lls)
            chardict[c] = i

        return lls