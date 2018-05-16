

def firstMissingPositive(nums):
    """
    :param self:
    :return:
    :type nums: List[int]
    :rtype: int
    """

    firstMissingPositive = None

    strictlyPosSum = 0
    strictlyPosCount = 0
    posMax = 0
    for q, val in enumerate(nums):
        if (val > 0):
            strictlyPosSum += val
            strictlyPosCount += int(1)
            posMax = max(posMax, val)

    inclusiveSum = int(strictlyPosCount * (strictlyPosCount + 1)) / int(2)

    print "inclusiveSum = {0}".format(inclusiveSum)

    if strictlyPosSum == inclusiveSum:
        firstMissingPositive = posMax + 1
    else:
        firstMissingPositive = abs(strictlyPosSum - inclusiveSum)

    return firstMissingPositive


def main():


    testarray = [3, 4, -1, 1, 8]

    fmp = firstMissingPositive(testarray)
    print "fmp = {0}".format(fmp)


if __name__ == "__main__":
    main()