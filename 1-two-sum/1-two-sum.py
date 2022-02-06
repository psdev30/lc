class Solution(object):
    def twoSum(self, nums, target):
        #brute force
        #time: O(n^2)
        #space: O(1)
        
        # brute force method that checks thru all possible 2 num combos 
        for i in range(len(nums)):
            sum = nums[i]
            for z in range(i + 1, len(nums)):
                if(sum + nums[z] == target):
                    return [i, z]
        
        #hashmap
        #time: O(n)
        #space: O(n)
        
        # create dictionary for O(1) search time
        tracker = dict()
        # as we iterate thru the array, calc the needed number (target - current num)
        for i, num in enumerate(nums):
            needed = target - num
            # then check the dict in O(1) avg. time to see if the needed value exists
            if(needed in tracker):
                return [tracker[needed], i]
            # if the needed value isn't there, then add the current num we're on as it might be part of the solution later
            else:
                tracker[num] = i

        