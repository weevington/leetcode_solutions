class Solution:
    """
    Convert a Roman numeral to a decimal (base 10) integer.

    This method uses two dictionaries to store the decimal representations of
    Roman numerals. An index is held to for the current index that loops 
    through the string. The Roman numeral is read left to right and the answer
    is incremented by the amount corresponding to the character found at the
    current index.
    
    The index is checked as to whether it is less than the string length minus
    two. If the next two characters fall into the special or "extended" set of 
    characters, i.e. "CM", "CD", "XC", "XL", "IX", etc. then increase the index 
    by two, else, just find the character key in the digit map dictionary, add 
    the value answer, and increase the index by one.

    Parameters
    ----------
    s : str
       A string representing a Roman numeral.

    Returns
    -------
    decimal_int : int
        The numeral in decimal (base 10) representation.
    """
    def romanToInt(self, s: str) -> int:
        digit_map = {"M"  : 1000,
                     "D"  :  500,
                     "C"  :  100,
                     "L"  :   50,
                     "X"  :   10,
                     "V"  :    5,
                     "I"  :    1}
        
        extended_map = {"CM" : 900,
                        "CD" : 400,
                        "XC" :  90,
                        "XL" :  40,
                        "IX" :   9,
                        "IV" :   4}

        decimal_int = 0
        s_len = len(s)
        i = 0
        while i < s_len:
            if i + 1 < s_len:
                if str(s[i] + s[i + 1]) in extended_map:
                    decimal_int += extended_map[s[i] + s[i + 1]]
                    i += 2
                else:
                    decimal_int += digit_map[s[i]]
                    i += 1
            else:
                decimal_int += digit_map[s[i]]
                i += 1
        
        return decimal_int