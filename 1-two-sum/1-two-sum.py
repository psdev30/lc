class Solution(object):
    def twoSum(self, nums, target):
        #brute force
        for i in range(len(nums)):
            sum = nums[i]
            for z in range(i + 1, len(nums)):
                if(sum + nums[z] == target):
                    return [i, z]