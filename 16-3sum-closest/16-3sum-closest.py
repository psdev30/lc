class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closestSum = float('inf')
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == target:
                    return sum                    
                if sum > target:
                    r -= 1
                elif sum < target:
                    l += 1
                if abs(target - sum) < abs(target - closestSum):
                    closestSum = sum
                elif abs(target - sum) == abs(target - closestSum):
                    closestSum = min(sum, closestSum)

        return closestSum
