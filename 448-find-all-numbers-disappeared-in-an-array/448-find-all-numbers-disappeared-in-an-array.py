class Solution(object):
    def findDisappearedNumbers(self, nums):
        #hashmap
        #time: O(2n) --> O(n)
        #space: O(n)
        # res = []
        # n = len(nums)
        # # use dictionary to store all numbers in array
        # tracker = dict()
        # for num in nums:
        #     tracker[num] = True
        # # iterate thru specified [1, n] range and whatever's not in the tracker must not have been in the array
        # for i in range(1, n + 1):
        #     if i not in tracker:
        #         res.append(i)
        # return res
    
        #set (same as hashmap just cleaner)
        #time: O(2n) --> O(n)
        #space: O(n)
        # res = []
        # n = len(nums)
        # tracker = set(nums)
        # for i in range(1, n + 1):
        #     if i not in tracker:
        #         res.append(i)
        # return res
    
        #set one-liner
        return set(range(1, len(nums) + 1)) - set(nums)
        
        