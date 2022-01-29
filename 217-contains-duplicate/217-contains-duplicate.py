class Solution(object):
    def containsDuplicate(self, nums):
        #hashmap 
        #time: O(n)
        #space: O(n)
        tracker = dict()
        # iterate thru array, if new value then add to dups tracker
        for val in nums:
            if val not in tracker:
                tracker[val] = True
            # if val is already in tracker, this means it was already seen and is thus a duplicate
            else:
                return True
        return False
    
        #sorting
        #time: O(nlogn + n) --> O(nlogn)
        #space: O(1)
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False