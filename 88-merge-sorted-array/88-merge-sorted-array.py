class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # last index in nums1 (the combined array)
        lastPos = m + n - 1
        
        # iterate until either the filled part of nums1 or nums2 are accounted for
        while m > 0 and n > 0:
            # if the val in nums1 is larger, fill it in at the current index of the combined array
            # decrement pointer for nums1 filled part since that number has been accounted for
            if(nums1[m - 1] > nums2[n - 1]):
                nums1[lastPos] = nums1[m - 1]
                m -= 1
            # if the val in nums2 is larger (or equal), fill it in at the current index of the combined array
            # decrement pointer for nums2 since that number has been accounted for 
            else:
                nums1[lastPos] = nums2[n - 1]
                n -= 1
            # decrement lastPos since the current index in the combined array has been covered by one of the if cases
            lastPos -= 1
        
        # edge case handles when n > 0 after m completes
        # we just fill in the remaining values of n in the combined array 
        while n > 0:
            nums1[lastPos] = nums2[n - 1]
            lastPos -= 1
            n -= 1
            
        return nums1