class Solution(object):
    def productExceptSelf(self, nums):
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = nums[i - 1] * res[i - 1]
        R = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * R
            R *= nums[i]
        return res