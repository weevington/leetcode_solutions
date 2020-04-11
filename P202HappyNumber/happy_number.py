class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Parameters
        ----------
        n : [int]
            Input integer.

        Returns
        -------
        happy : bool
            True if the number is a "happy" number.
        """
        happy = False

        h = 0
        num = n

        while num > 0:
            h += (num % 10)**2
            num = num // 10
            if num == 0:
                if h == 1:
                    happy = True
                    break
                elif h == 4:
                    break
                else:
                    num = h
                    h = 0

        return happy