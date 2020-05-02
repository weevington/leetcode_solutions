class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        """
        You're given strings J representing the types of stones that are jewels, 
        and S representing the stones you have.  Each character in S is a type of
        stone you have. This function returns how many of the stones in a given 
        collection are are also jewels.

        Parameters
        ----------
        J : str
            String representing jewels. Case sensitive, i.e. "aA" represents
            two different stones
        
        S : str
            String representing jewels. Case sensitive, i.e. "aA" represents
            two different stones

        Returns
        -------
        num_jewels : int
            Number of jewels in the collection of stones.

        Examples
        --------
        Input: J = "aA", S = "aAAbbbb"
        Output: 3

        Input: J = "z", S = "ZZ"
        Output: 0
        """
        jewel_dict = {}
        
        for i, s in enumerate(S):
            if s in J:
                if jewel_dict.get(s) is None:
                    jewel_dict[s] = 1
                else:
                    jewel_dict[s] += 1
        
        num_jewels = 0
        for j in jewel_dict.values():
            num_jewels += j
        
        return num_jewels


class Solution:
    def numJewelsInStones(self, J, S):
        """
        You're given strings J representing the types of stones that are jewels, 
        and S representing the stones you have.  Each character in S is a type of
        stone you have. This function returns how many of the stones in a given 
        collection are are also jewels.

        This solution uses a set (hash set) to keep track of the jewels, i.e.,
        there should only be one type of each jewel. It also makes use of the
        sum() function for Python.

        Parameters
        ----------
        J : str
            String representing jewels. Case sensitive, i.e. "aA" represents
            two different stones
        
        S : str
            String representing jewels. Case sensitive, i.e. "aA" represents
            two different stones

        Returns
        -------
        num_jewels : int
            Number of jewels in the collection of stones.

        Examples
        --------
        Input: J = "aA", S = "aAAbbbb"
        Output: 3

        Input: J = "z", S = "ZZ"
        Output: 0
        """
        Jset = set(J)
        return sum(s in Jset for s in S)