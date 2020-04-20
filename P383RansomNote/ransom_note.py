class Solution:
    """
    Given an arbitrary ransom note string and another string containing
    letters from all the magazines, return True if the ransom note can be 
    constructed from the magazines, otherwise, it will return false.

    This method uses a dictionary to store the counts of each letter in the
    magazime. The ransom note can only be constructed if there is at least
    the same number of each letter in the magazine as there are in the planned
    ransom note. If the number of occurrences of a given letter in the planned
    ransom note is greater than that of the count in the magazine, return
    False.

    Parameters
    ----------
    ransomNote : str
        The ransom note to be constructed.

    magazine : str
        Magazine with letters to construct the ransom note.

    Returns
    -------
    can_construct : bool
        Whether or not the ransom note can be constructed from the
        magazine.

    Examples
    --------
    Input: "a", "b"
    Output: False

    Input: "aa", "ab" 
    Output: False
    """
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m_dict = {}
        for l in magazine:
            if m_dict.get(l) is None:
                m_dict[l] = 1
            else:
                m_dict[l] += 1
        
        for l in ransomNote:
            if m_dict.get(l) is None:
                return False
            else:
                m_dict[l] -= 1
        
        return len([q for q in m_dict.values() if q < 0]) == 0