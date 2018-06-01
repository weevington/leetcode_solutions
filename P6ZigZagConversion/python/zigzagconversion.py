class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        sLen = len(s)

        ans = ""
        width = int(2 * numRows - 2)

        for i in range(numRows):
            if i > sLen:
                break
            k = i
            qStep = 0
            while k < sLen:
                ans += s[k]
                if i == 0 or i == numRows - 1:
                    k += width
                else:
                    if qStep % 2 == 0:
                        k += (width - i * 2)
                    else:
                        k += i * 2
                    qStep += 1

        return ans

def main():

    sol = Solution()

    testInput = "PAYPALISHIRING"
    nRows = 3

    testOutput = sol.convert(testInput, 3)

    assert(testOutput == "PAHNAPLSIIGYIR")
    print "assertion passed"



if __name__ == "__main__":
    main()