class Solution(object):
    def twoSum(self, nums, target):
        #brute force
        #time: O(n^2)
        #space: O(1)
        # for i in range(len(nums)):
        #     sum = nums[i]
        #     for z in range(i + 1, len(nums)):
        #         if(sum + nums[z] == target):
        #             return [i, z]
        
        #hashmap
        tracker = dict()
        for i, num in enumerate(nums):
            needed = target - num
            if(needed in tracker):
                return [tracker[needed], i]
            else:
                tracker[num] = i

        