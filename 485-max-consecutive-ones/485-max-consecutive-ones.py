class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxOnes = ones = 0
        for num in nums:
            if num == 1:
                ones += 1
            else:
                maxOnes = max(maxOnes, ones)
                ones = 0
        return max(maxOnes, ones)
        