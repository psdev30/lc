class Solution(object):
    def removeElement(self, nums, val): 
        #slow pointer
        #time: O(n)
        #space: O(1)
        
        k = 0
        for i, num in enumerate(nums):
            if num != val:
                nums[k] = num
                k += 1
        return k
    
        #optimal
        #time: O(n)
        #space: O(1)
        
        end = len(nums) - 1
        k = 0
        while k < end:
            if nums[k] == nums[end]:
                temp = nums[k]
                nums[k] = nums[end]
                nums[end] = temp
                end -= 1
        return k