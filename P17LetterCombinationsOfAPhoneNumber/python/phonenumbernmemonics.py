class Solution(object):
    def letterCombHelper(self, maxIndex, letterCombs, digits, tString, digCharMap, index):
        if index == maxIndex:
            letterCombs.append(tString)
            return

        currDigit = digits[index]
        chars = digCharMap[currDigit]

        for k in range(len(chars)):
            tString += chars[k]
            self.letterCombHelper(maxIndex, letterCombs, digits, tString, digCharMap, index + 1)
            tString = tString[:-1]

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        dMap = {"0": "",
                "1": "",
                "2": "abc",
                "3": "def",
                "4": "ghi",
                "5": "jkl",
                "6": "mno",
                "7": "pqrs",
                "8": "tuv",
                "9": "wxyz"}

        combinations = []

        maxIndex = len(digits)

        self.letterCombHelper(maxIndex, combinations, digits, "", dMap, 0)

        return combinations