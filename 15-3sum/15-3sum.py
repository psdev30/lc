class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        triplets = []
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                l, r = i + 1, len(nums) - 1
                while l < r:
                    sum = nums[i] + nums[l] + nums[r]
                    if sum > 0:
                        r -= 1
                    elif sum < 0:
                        l += 1
                    else:
                        triplets.append([nums[i], nums[l], nums[r]])
                        l += 1
                        while l < len(nums) and nums[l] == nums[l - 1]:
                            l += 1

        return triplets
        