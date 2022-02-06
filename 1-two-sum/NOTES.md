only works if we're told to return the numbers themselves.. sorting messes up the indices
​
```
#two pointer
#time: O(nlogn + n)
#space: O(1)
nums.sort()
left = 0
right = len(nums) - 1
for i in range(len(nums)):
if(nums[left] + nums[right] == target):
return [left, right]
elif(nums[left] + nums[right] > target):
right -= 1
else:
left += 1
```