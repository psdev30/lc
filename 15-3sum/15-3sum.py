class Solution(object):
    def threeSum(self, nums):
        triplets = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            needed = -1 * nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[left] + nums[right]
                if sum > needed:
                    right -= 1
                elif sum < needed:
                    left += 1
                else:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return triplets
        