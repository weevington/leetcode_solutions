


def combinationSum2Recursive(solution, candidates, target):

    for j in range(len(candidates) - 1, -1 , -1):
        print "j = {0}".format(j)
        #arr = []
        #for q, val in enumerate(candidates):
        #    if (target - val) >= 0:
        #        arr.append(val)

        #if sum(arr) == target:
        #    solution.append(arr)



def combinationSum2(candidates, target):

    sortedCandidates = sorted(candidates)
    solArray = []

    combinationSum2Recursive(solArray, candidates, target)

def main():
    mylist = [10, 1, 2, 7, 6, 1, 5]
    mytarget = 8

    combinationSum2(mylist, mytarget)


if __name__ == "__main__":
    main()


#class Solution:
#    # @param candidates, a list of integers
#    # @param target, integer
#    # @return a list of lists of integers
#    def combinationSum2(self, candidates, target):
#        candidates.sort()
#        solution = []
#        self.combinationSum2Rec(candidates, target, 0, 0, [], solution)
#        return solution
#
#    def combinationSum2Rec(self, candidates, target, index, sum, tempList, solution):
#        if sum == target:
#            solution.append(list(tempList))
#            return
#        for i in range(index, len(candidates)):
#            if (i == index or candidates[i - 1] != candidates[i]) and sum + candidates[i] <= target:
#                tempList.append(candidates[i])
#                self.combinationSum2Rec(candidates, target, i + 1, sum + candidates[i], tempList, solution)
#                tempList.pop()