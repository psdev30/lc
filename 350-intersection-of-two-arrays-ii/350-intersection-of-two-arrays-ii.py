from itertools import repeat

class Solution(object):
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        
        n1 = n2 = i = 0
        while n1 < len(nums1) and n2 < len(nums2):
            if nums1[n1] == nums2[n2]:
                nums1[i] = nums1[n1]
                i += 1
                n1 += 1
                n2 += 1
            elif nums1[n1] > nums2[n2]:
                n2 += 1
            else:
                n1 += 1
        return nums1[:i]

                
        
        