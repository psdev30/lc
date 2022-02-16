class Solution(object):
    def removeElement(self, nums, val): 
        k = 0
        for i, num in enumerate(nums):
            if num != val:
                nums[k] = num
                k += 1
        return k