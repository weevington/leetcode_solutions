
def two_sum(nums: list, target: int) -> list:
        """
        Given an array of integers, return indices of the two numbers such that
        they add up to a specific target.

        Parameters
        ----------
        nums : list
            list containing integers
        target : int
    
        Returns
        -------
        list containing indices of integers which add up to target
        """
        complements = {}
        
        for i, num in enumerate(nums):
            comp = target - num
            if comp in complements:
                return [complements[comp], i]  
            else:
                complements[num] = i
                
        return []


def two_sum_two_ptr(nums: list, target: int) -> list:
        """
        Given an array of integers, return indices of the two numbers such that
        they add up to a specific target. This approach uses two pointers to
        avoid using extra memory.

        Parameters
        ----------
        nums : list
            list containing integers
        target : int
    
        Returns
        -------
        list containing indices of integers which add up to target
        """
        srt_nums = sorted(nums)
        trail =  0
        lead = len(srt_nums) - 1

        while (trail < lead):
            test_sum = srt_nums[trail] + srt_nums[lead] 
            if test_sum == target:
                return [trail, lead]
            elif test_sum > target:
                lead -= 1
            else:
                trail += 1 
                
        return []


def main():
    nums = [2, 7, 11, 15]
    target = 9

    print("two_sum(nums) = {}".format(two_sum(nums, target)))
    print("two_sum_two_ptr(nums) = {}".format(two_sum_two_ptr(nums, target)))


if __name__ == "__main__":
    main()