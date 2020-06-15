class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Given a non-empty string s, returns whether the given string can be 
        made into a palindrome with the removal of up to 1 character.

        Conider the example "aba". This string is a palindrome, so there is
        nothing to remove.

        Now consider the example "racebcar". Normally, "racecar" is a classic 
        example of a palindrome, bue the presence of the "b" in the string 
        prevents it from being a palindrome. However, if we remove the single
        character 'b', then we recover "racecar".

        We can use two pointers, one from the end of the string, and one from
        the start of the string. 

                                       "racebcar"
                                        ^      ^
                                       lo      hi

        If s[lo] is equal to s[hi], then we proceed to increment lo and
        decrement hi.

                                       "racebcar"
                                         ^    ^
                                        lo    hi


                                       "racebcar"
                                          ^  ^
                                         lo  hi


                                       "racebcar"
                                           ^^
                                          lohi

        Here, we have the condition s[lo] is not equal to s[hi]. We can remove
        up to one character, but we don't know if the offending character is 
        s[lo] or s[hi]. We can rebuild the string, excluding s[lo], and we can
        rebuild a different string, excluding s[hi]. If we exclude s[lo], we
        obtain "racbcar", which is a palindrome. If we were to remove s[hi], we
        obtain "racecar", which is also a palindrome. In this particular 
        example, it turns out that we can achieve a palindrome by removing 
        either s[lo] or s[hi], but that is not the general case. Therefore, in
        general, if s[lo] is not equal to s[hi], we build the two different 
        substrings strings out of the original string, one without s[lo] and 
        one without s[hi]. We test each of these new substrings to see if 
        either one is a palindrome, in which case we return True, otherwise
        we return False.

        Parameters
        ----------
        s : str

        Returns
        -------
        valid_palindrome : bool
            True if the string can be converted into a valid palindrome, else 
            False.
        
        Examples
        --------
        Input : "aba"
        Output : True

        Input : "abca"
        Output : True
        The string may be made into a palindrome by removing the character 'c'

        Input : "eeccccbebaeeabebccceea"
        Output :
        """
        # A blank string is defined to be palindromic.
        if not s:
            return True
        
        lo = 0
        hi = len(s) - 1
        
        while lo < hi:
            if s[lo] == s[hi]:
                lo += 1
                hi -= 1
            else:
                # Build two new strings by removing one character,
                # one string is built by excluding s[lo],
                # the other string by excluding s[hi]
                test_one = s[:lo] + s[lo + 1:]
                test_two = s[:hi] + s[hi + 1:]
                
                # Test if either one of these strings is a palindrome 
                return test_one == test_one[::-1] or test_two == test_two[::-1]

        # If we have reached this point, it means that the original string is
        # a palindrome.
        return True