class Solution(object):
    def singleNumber(self, nums):
        #hashmap
        #time: O(2n) --> O(n)
        #space: O(n)
        # seen = dict()
        # for num in nums:
        #     seen[num] = seen.get(num, 0) + 1
        # for num in seen:
        #     if seen[num] == 1:
        #         return num
        #math
        return 2 * sum(set(nums)) - sum(nums)
        