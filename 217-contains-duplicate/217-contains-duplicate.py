class Solution(object):
    def containsDuplicate(self, nums):
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         return True
        # return False
    
        tracker = dict()
        for num in nums:
            if num not in tracker:
                tracker[num] = tracker.get(num, 0) + 1
            else:
                return True
        return False
                
        