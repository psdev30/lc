from itertools import repeat

class Solution(object):
    def intersect(self, nums1, nums2):
        #hashmap

        if len(nums1) > len(nums2):
            return Solution.intersect(self, nums2, nums1)
        
        counter = dict()
        intersection = []
        
        for num in nums2:
            counter[num] = counter.get(num, 0) + 1
        for num in nums1:
            if num in counter:
                if counter[num] > 0:
                    intersection.append(num)
                    counter[num] -= 1
        
        return intersection
        
        #sorting
        #time: O(nlogn + mlogm + min(n1, n2)) --> O(nlogn + mlogm)
        #space: O(n + m)
        
#         nums1.sort()
#         nums2.sort()
        
#         n1 = n2 = i = 0
#         while n1 < len(nums1) and n2 < len(nums2):
#             if nums1[n1] == nums2[n2]:
#                 nums1[i] = nums1[n1]
#                 i += 1
#                 n1 += 1
#                 n2 += 1
#             elif nums1[n1] > nums2[n2]:
#                 n2 += 1
#             else:
#                 n1 += 1
#         return nums1[:i]

                
        
        