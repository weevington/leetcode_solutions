class Solution:
    """
    Determines whether one string is an anagram of another string.

    This method uses two dictionaries to determine if one string is an anagram
    of another. Loop over the characters in each string and store each letter 
    as the key in a hash map increment the count of each key every time

    Loop over the keys of the dictionary for the first string. If the value 
    count of each letter for the second string does not equal the value count
    of same letter for the first string, return false. If the value counts of
    each letter for both strings is the same, return True.

    Parameters:
    s : str

    t : str

    Returns
    -------
    is_anagram : bool 
        Whether or not one second string is an anagram of the first.

    """
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}
        
        for i, c in enumerate(s):
            if not c in s_dict.keys():
                s_dict[c] = 1
            else:
                s_dict[c] += 1
            
        for i, c in enumerate(t):
            if not c in t_dict.keys():
                t_dict[c] = 1
            else:
                t_dict[c] += 1
        
        for skey in s_dict.keys():
            if t_dict.get(skey) is None:
                return False
            elif s_dict[skey] != t_dict[skey]:
                return False
        
        return True