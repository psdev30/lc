class Solution(object):
    def containsDuplicate(self, nums):
        tracker = dict()
        for val in nums:
            if val not in tracker:
                tracker[val] = True
            else:
                return True
        return False