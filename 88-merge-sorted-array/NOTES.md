* trick is to realize that the end of array is empty for all intents and purposes, so if we start by filling in from there, we don't have to worry about losing track of the overriden values in nums1 and using a temp array to store them
* also need to remember the **edge case:**
* if nums1 is emptied out before nums2, then the values remaining in nums2 aren't filled into the correct spaces in nums1
* this can be handled with another while loop outside the initial m > 0 and n > 0 loop that fills them in going left as long as nums2 (n) is still > 0