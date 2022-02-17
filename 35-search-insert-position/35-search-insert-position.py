class Solution(object):
    def searchInsert(self, nums, target):     
        lo = 0
        hi = len(nums) - 1
        
        while lo <= hi:
            mid = lo + ((hi - lo) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return lo 