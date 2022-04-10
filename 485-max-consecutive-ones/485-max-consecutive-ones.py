class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxOnes = ones = 0
        for num in nums:
            ones = ones + 1 if num == 1 else 0
            maxOnes = max(maxOnes, ones)
        return maxOnes
        