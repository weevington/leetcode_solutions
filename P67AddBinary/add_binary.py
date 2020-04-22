class Solution:
    """
    Returns the sum of two strings representing binary numbers. The result is
    also a binary number.

    The input strings are both non-empty and contains only characters 1 or 0.

    Parameters
    ----------
    a : str
    b : str

    Returns
    -------
    binary_sum :str
        String representing the sum of the two numbers a, and b in binary format.
        Least significant digit is at the right-most position.

    Examples
    --------
    Input: a = "11", b = "1"
    Output: "100"

    Input: a = "1010", b = "1011"
    Output: "10101"
    """
    def addBinary(self, a: str, b: str) -> str:
        a_len = len(a)
        b_len = len(b)

        max_len = max(a_len, b_len)
        
        # be explicit about types, since we a re mixing strings and integers
        # resulting digit of two digits added at a position
        rdig   = int(0)
        # carry digit of resulting addition between two binary digits
        rcarry = int(0)
        res    = ""
        
        for j in range(max_len):
            offset = j + 1
            a_dig = 0
            b_dig = 0
            
            a_idx = a_len - offset
            if a_idx >= 0:
                a_dig = int(a[a_idx])
    
            b_idx = b_len - offset
            if b_idx >= 0:
                b_dig = int(b[b_idx])
                
            rsum   = a_dig + b_dig + rcarry
            rdig   =  rsum % 2
            rcarry =  rsum // 2
            res += str(rdig) 

        if rcarry:
            res += str(rcarry)
            #res = str(rcarry) + res
            
        return res[::-1]