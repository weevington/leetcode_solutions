class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Returns whether a string subsequence of another string.

        A subsequence of a string is a new string which is formed from the 
        original string by deleting some (can be none) of the characters 
        without disturbing the relative positions of the remaining characters.
        (ie, "ace" is a subsequence of "abcde" while "aec" is not).
        
        The base case of an empty string s is defined to be True.

        This uses a dynamic programming approach to solve the problem. A matrix
        is constructed which compares. The matrix is of dimensions m * n, where
        m is the length of the first string argument plus one, s, and t is the 
        length of the second string argument t plus one. The matrix is 
        constructed as follows for the example s = "abc", t = "ahbgdc":
        
        The matrix is initially set to all zeroes. 

                                 a   h   b   g   d   c   
                            0    0   0   0   0   0   0
         
                        a   0    0   0   0   0   0   0
        
                        b   0    0   0   0   0   0   0 
        
                        c   0    0   0   0   0   0   0

        Starting from index 1 Loop over the rows of the matrix, then the 
        columns.

                                j=1 .. ..
                                a   h   b   g   d   c   
                            0   0   0   0   0   0   0
         
                    i=1 a   0   1   0   0   0   0   0
        
                ..      b   0   0   0   0   0   0   0 
        
                ..      c   0   0   0   0   0   0   0
        
        Because we have padded the matrix with an extra, row and column of 
        zeroes, we must refer to the string elements with an offset of 1. If 
        character s[i - 1] is equal to the t[j - 1] (in the above example, 
        i = 1 and j = 1, referring to s[0] and ), we add one to the length
        of the longest common sub-sequence, i.e if s[i - 1] == t[j - 1], then
        dp[i][j] = 1 + dp[i - 1][j - 1]

                                    j=2
                                a   h   b   g   d   c   
                            0   0   0   0   0   0   0
         
                    i=1 a   0   1   1   0   0   0   0  
        
                        b   0   0   0   0   0   0   0
        
                        c   0   0   0   0   0   0   0
        
        Now we compare s[0] and j[1]. These are not equal. In general, if
        s[i - 1] != t[j - 1], then the longest common subsequence becomes the
        max of the element in the previous row and same column, or the element
        in the previous column and same row, i.e. 
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

                                       j=3        
                                a   h   b   g   d   c   
                            0   0   0   0   0   0   0
         
                        a   0   1   1   1   1   1   1
        
                    i=2 b   0   1   1   2   0   0   0
        
                        c   0   0   0   0   0   0   0

        The final matrix becomes:

                                                    j=6
                                a   h   b   g   d   c   
                            0   0   0   0   0   0   0
         
                        a   0   1   1   1   1   1   1
        
                        b   0   1   1   2   2   2   2
        
                    i=3 c   0   1   1   2   2   2   3

        We return whether the element in the last row and last column in the
        dp matrix is equal to the length of string s. 

        The run-time complexity of this solution is O(m * n) where m and n are
        mentioned above.


        Parameters
        ----------
        s : str
            Input string to be checked if it is subsequence of second string.
        
        t : str

        Returns
        -------
        is_subsequence : bool
            True if the string s is a subsequence of the string t, else False.

        Examples
        --------
        Input: s = "abc", t =  "ahbgdc"
        Output: True

        Input: s = "axc", t = "ahbgdc"
        Output: false

        Input: s = "goodu", t = "goodburger"
        Output: True 
        """
        # base case of a blank string for s, this is defined to be True
        if not s:
            return True
        
        s_len = len(s)
        t_len = len(t)
        
        # create the dp matrix and initialize it to all zeroes
        dp = [[0 for c in range(t_len + 1)] for r in range(s_len + 1)]
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                # if the characters being compared are the same, then add one
                # to the length of the longest sommon subsequence formed 
                # between s and t
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    # take the longest common subsequence up to that point
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
        # return whether the element of dp in the final row and column is equal
        # to the length of s. Then s is a subsequence of t.
        return dp[-1][-1] == s_len