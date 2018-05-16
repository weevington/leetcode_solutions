
def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if not nums:
        return [[]]

    x = subsets(nums[1:])
    print "x = {0}".format(x)

    return x + [[nums[0]] + y for y in x]

def main():
    nums = [1, 2, 3]

    allsubsets = subsets(nums)

    print "allsubsets = {0}".format(sorted(allsubsets))


if __name__ == "__main__":
    main()