class Solution(object):
    def containsDuplicate(self, nums):
        #sorting
        #time: O(nlogn)
        #space: O(1)
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
    
        #hashmap
        #time: O(2n) --> O(n)
        #space: O(n)
        
        # create dict to store all seen numbers
        tracker = dict()
        for num in nums:
            if num not in tracker:
                tracker[num] = tracker.get(num, 0) + 1
            # if number we're currently on is already in dict, then it has to be a duplicate
            else:
                return True
        return False
                
        