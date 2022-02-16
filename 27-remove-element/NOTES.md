#good solution
* exact same logic as Remove Duplicates from Sorted Array (slow pointer sticking to values we don't want and then being overriden when a "clean" value is encountered)
​
​
#best solution (slightly optimized)
* notice that when the slow and fast pointer are in alignment bc we haven't run into an `element == val`, we still do the copy `nums[k] = num`
* we can eliminate this extra operation in the case where there are very few, even only 1 element, that equals `val` by instead swapping the element that we want to remove with the end of the array and decreasing the size by 1 (effectively reduces size of array since the remaining portion is invisible based on the index)
* one case to consider with this approach is that the element we swapped in from the end of the array may itself be the target `val`.
* --> we handle this by using a while loop since it forces us to do the pointer increment manually.. we then choose to do the increment only after another check is run on the same index we previously processed (since the target `val` was potentially swapped in again)
* --> only after passing this check that the forbidden `val` was not swapped in (bc if it we process it again), we increment the main pointer and move on to the next index
​