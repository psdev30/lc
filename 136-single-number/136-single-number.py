class Solution(object):
    def singleNumber(self, nums):
        #hashmap
        #time: O(2n) --> O(n)
        #space: O(n)
        
        # create dict to store counts of numbers in array
        seen = dict()
        for num in nums:
            # if number isn't in dict it gets initial value of 0
            seen[num] = seen.get(num, 0) + 1
        # whatever value in dict that's 1, its corresponding key is the 'single number'
        for num in seen:
            if seen[num] == 1:
                return num
            
        #math
        #time: O(n)
        #space: O(n)
        return 2 * sum(set(nums)) - sum(nums)
    
        #bit manipulation
        #TODO
        