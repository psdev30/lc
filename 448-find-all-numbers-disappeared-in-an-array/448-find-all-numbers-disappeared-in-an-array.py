class Solution(object):
    def findDisappearedNumbers(self, nums):
        res = []
        n = len(nums)
        tracker = dict()
        for num in nums:
            tracker[num] = True
        for i in range(1, n + 1):
            if i not in tracker:
                res.append(i)
        return res
        
        