class Solution(object):
    def singleNumber(self, nums):
        seen = dict()
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        for num in seen:
            if seen[num] == 1:
                return num
        