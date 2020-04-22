class Solution:
    """
    This function determines if a number A strobogrammatic number is a
    number that looks the same when rotated 180 degrees (looked at upside
    down). The digits of the number are represented as a string.

    Parameters
    ----------
    num : str

    Returns
    -------
    strobogrammatic : bool

    Examples
    --------
    Input:  "69"
    Output: True

    Input:  "88"
    Output: True
    """
    def isStrobogrammatic(self, num: str) -> bool:
        if not num:
            return False

        lo = 0
        hi = len(num) - 1
        
        strobo_pairs = {'0':'0', '1':'1', '6':'9', '9':'6', '8':'8'}
        center_vals  = {'1', '8', '0'}

        while lo <= hi:
            if lo == hi:
                if num[lo] not in center_vals:
                    return False
            else:
                if strobo_pairs.get(num[lo]) is None:
                    return False
                elif strobo_pairs[num[lo]] != num[hi]:
                    return False
                
            lo += 1
            hi -= 1
                        
        return True