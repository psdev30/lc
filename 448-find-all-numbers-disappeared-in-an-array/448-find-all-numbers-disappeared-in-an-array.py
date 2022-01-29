class Solution(object):
    def findDisappearedNumbers(self, nums):
        #hashmap
        #time: O(2n) --> O(n)
        #space: O(n)
#         res = []
#         n = len(nums)
#         # use dictionary to store all numbers in array
#         tracker = dict()
#         for num in nums:
#             tracker[num] = True
#         # iterate thru specified [1, n] range and whatever's not in the tracker must not have been in the array
#         for i in range(1, n + 1):
#             if i not in tracker:
#                 res.append(i)
#         return res
    
#         #set (same as hashmap just cleaner)
#         #time: O(2n) --> O(n)
#         #space: O(n)
#         res = []
#         n = len(nums)
#         tracker = set(nums)
#         for i in range(1, n + 1):
#             if i not in tracker:
#                 res.append(i)
#         return res
    
#         #set (one-liner version)
#         return set(range(1, len(nums) + 1)) - set(nums)
    
        #in-place
        #time: O(2n) --> O(n)
        #space: O(1) (output array doesn't count)
        res = []
        for num in nums:
            # calculate and adjust the index 
            nums[abs(num) - 1] = abs(nums[abs(num) - 1]) * -1
        # pass thru the array again and any positive values that are left indicate that index + 1 is a disappeared number
        for i, val in enumerate(nums):
            if val > 0:
                res.append(i + 1)
        return res
            
            
    
        
        
        