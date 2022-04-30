class Solution(object):
    def threeSumSmaller(self, nums, target):
        nums.sort()
        count = 0
        for i in range(len(nums) - 2):
            l , r = i + 1, len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] +nums[r]
                if sum < target:
                    count += r - l
                    l += 1
                else:
                    r -= 1

        return count
