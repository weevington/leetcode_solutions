

def mysearch(nums, target):
    minValIndex = int(-1)

    arrlen = len(nums)
    if arrlen == 0:
        return minValIndex
    elif arrlen == 1:
        return 0

    floorIndex = 0
    ceilIndex = len(nums) - 1

    while (floorIndex < ceilIndex):

        guessIndex = floorIndex + int(ceilIndex - floorIndex) / int(2)
        print "floorIndex = {0}, " \
              "ceilIndex  = {1}" \
              "guessIndex = {2} ".format(floorIndex, ceilIndex, guessIndex)
        if nums[floorIndex] == target:
            minValIndex = floorIndex
            break
        elif nums[ceilIndex] == target:
            minValIndex = ceilIndex
            break
        elif nums[guessIndex] == target:
            minValIndex = guessIndex
            break

        if target <= nums[guessIndex]:
            # go left
            ceilIndex = guessIndex
        else:
            # go right
            floorIndex = guessIndex

        if ceilIndex == floorIndex + 1:
            break

    return minValIndex


def main():
    #myarray = list([3, 4, 5, 6, 1, 2])
    myarray = [4, 5, 6, 7, 0, 1, 2, 3]
    targetIndex = mysearch(myarray, target = 6)
    print "targetIndex = {0}".format(targetIndex)


if __name__ == "__main__":
    main()