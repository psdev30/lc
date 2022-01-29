class Solution(object):
    def missingNumber(self, nums):
        # sorting
        #time: O(nlogn)
        #space: O(1)
        nums.sort()
        n = len(nums)
    
        # checks first index match (avoids index out of bounds in later loop)
        if nums[0] != 0:
            return 0
        # checks last index match
        if nums[n - 1] != n:
            return n
        
        #loop to check for indices in between
        for i in range(1, n):
            if i != nums[i]:
                return i
        
        #hashmap
        #time: O(n)
        #space: O(n)
        tracker = dict()
        n = len(nums)
        # fills the dictionary
        for i, val in enumerate(nums):
            if val not in tracker:
                tracker[val] = i
        for i in range(n + 1):
            if i not in tracker:
                return i
            
        #gauss' formula
        #time: O(n)
        #space: O(1)
        n = len(nums)
        # finds sum of all numbers in the continuous sequence from [0, n]
        expectedSum = (n * (n + 1)) / 2
        # actual sum of the array
        actualSum = sum(nums)
        # the diff btwn actual & expected reveals the missing number
        return expectedSum - actualSum
        
        