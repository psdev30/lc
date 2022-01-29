class Solution(object):
    def containsDuplicate(self, nums):
        #hashmap 
        tracker = dict()
        # iterate thru array, if new value then add to dups tracker
        for val in nums:
            if val not in tracker:
                tracker[val] = True
            # if val is already in tracker, this means it was already seen and is thus a duplicate
            else:
                return True
        return False