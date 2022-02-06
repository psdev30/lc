class Solution(object):
    def maxSubArray(self, nums):
        #brute force
        #time: O(n^2)
        #space: O(1)
#         maxSubarraySum = float('-inf')
#         for i in range(len(nums)):
#             currSubarraySum = 0
#             for z in range(i, len(nums)):
#                 currSubarraySum += nums[z]
#                 maxSubarraySum = max(currSubarraySum, maxSubarraySum)
        
#         return maxSubarraySum

        maxSum = nums[0]
        currSum = nums[0]
        for i in range(1, len(nums)):
            currSum = max(currSum + nums[i], nums[i])
            maxSum = max(currSum, maxSum)
        return maxSum