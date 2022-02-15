#hashmap
* go thru the smaller of the 2 arrays (slight optimization to make size of hashmap the min(m, n)) and store the counts of each number
* go thru the larger of the 2 arrays and for each number that is in the hashmap which has a count > 0, add it to the **result array (nums1, see below)** and decrement the count of the number in the hashmap
* **result array (nums1, see below)**
* start a counter at the beginning of the array, and this counter that overwrites values in the original nums1 is fine bc it is a slow moving pointer that trails the position in the area that is being processed (any value that is being overwritten is guaranteed to have been processed already)
​
#sorting
* sort both arrays; this allows us to run separate pointers thru both arrays
* --> if the vals match, use the result array trick from above and put the matching value at result array index
* --> if nums1 val > nums2 val, move nums2 pointer forward bc there's a chance the next nums2 val could match the current nums1 val (vice versa for nums2 val > nums1 val)
* since we cleverly stored the result in place, we just return nums1.. but only return the array up to the trailing result array index thru slicing!