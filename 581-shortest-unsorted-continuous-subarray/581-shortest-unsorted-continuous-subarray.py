class Solution(object):
    def findUnsortedSubarray(self, nums):
        l, r = 0, 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                l = i
                break

        for i in range(len(nums) - 1, 0, -1):
            if nums[i] < nums[i - 1]:
                r = i
                break

        if l == 0 and r == 0:
            return 0


        subarrayMin, subarrayMax = min(nums[l : r + 1]), max(nums[l : r + 1])

        for i in range(0, l):
            if nums[i] > subarrayMin:
                l = min(l, i)

        for i in range(r, len(nums)):
            if nums[i] < subarrayMax:
                r = max(r, i)


        return r - l + 1
        