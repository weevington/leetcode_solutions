class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Given two words word1 and word2, returns the minimum number 
        of operations required to convert word1 to word2, where operations
        are defined to be: (1) insert a character, (2) delete a character 
        (3) replace a character.

        The solution uses dynamic programming to come up with an O(m * n)
        solution where m and n are the length of word1 and word2,
        respectively.

        To understand the dynamic programming solution, consider the example
        word1 = execution, word2 = intention

        Create a matrix of size (m + 1) * (n + 1) like so:        
                                   word1
                            e   x   e   c   u   t   i   o   n
                 i=0    0   1   2   3   4   5   6   7   8   9
                  
                 i=1  i 1   1   2   3   3   4   5   6   7   8  
                   
                 i=2  n 2   2   2   3   4   4   5   6   7   8 
                
               w i=3  t 3   3   3   3   3   4   5   6   7   8
               o   
               r i=4  e 4   4   4   4   4   4   5   6   7   8
               d
               2 i=5  n 5   5   5   5   5   5   5   6   7   8

                 i=6  t 6   6   6   5   6   6   5   6   7   8 

                 i=7  i 7   6   7   6   6   7   6   5   6   7

                 i=8  o 8   7   7   7   7   7   7   6   5   6

                 i=9  n 9   8   7   8   8   7   8   7   6   5
        
        Loop through the characters of the second word (i = 1..n + 1). Loop 
        through the characters of the second string (j = 1...m + 1). Consider 
        the case where i = 0 and j = 0. How many edits would it take to change
        'i' to 'e'? Just 1 edit. Now consider the case i = 1, j = 2. How many
        edits can be made from "i" to "ex"? Two, one to change the "i" to "e"
        and another one to append the "x". In the most general case, if the two
        letters being compared are equal, then the i,jth entry of the dp matrix
        is dp[i][j] = dp[i - 1][j - 1], else
        dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        Return the element in the last row and last column of the matrix as 
        the answer.

        Parameters
        ----------
        word1 : str

        word2 : str

        Returns
        -------
        edit_distance : int
            Minimum number of operations used to transform word1 into word2
        
        Examples
        --------
        Input: word1 = "horse", word2 = "ros"
        Output: 3
        Explanation: 
        horse -> rorse (replace 'h' with 'r')
        rorse -> rose (remove 'r')
        rose -> ros (remove 'e')
        """        
        len_one = len(word1)
        len_two = len(word2)

        # Create matrix which will keep a running count of the minimum number
        # of edits needed 
        dp = [[0 for c in range(len_one + 1)] for r in range(len_two + 1)]

        # In this case, the rows correspond to the letters of word2
        # while the columns correspond to the letters of word1
        for i in range(0, len_two + 1):
            for j in range(0, len_one + 1):
                # The first row column should just be a linear increasing
                # function of j. It is the equivalent of saying starting 
                # from nothing, how many edits must be made to have a string
                # of length j
                if j == 0:
                    dp[i][j] = i
                # Same for i. See the example matrix.
                elif i == 0:
                    dp[i][j] = j
                else:
                    # need i - 1 and j - 1, otherwise an index errror will occur.
                    # Remember that our matrix is of size len_one + 1)] for r in range(len_two + 1
                    if word2[i - 1] == word1[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

        return dp[-1][-1]
