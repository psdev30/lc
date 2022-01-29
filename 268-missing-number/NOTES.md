4 solutions:
​
1) Sorting
* sorting is the overhead, but makes it so the array indices line up with the loop iterations
* NOTE: need to do **if** checks first on first + last index, otherwise running the loop to n + 1 causes IOOB exception with the array!
​
2) Hashmap
* use hashmap to loop through nums once and store all numbers that appear
* then loop thru a 2nd time from [0-n] this time and find the one that's not in the hashmap
​
3) Gauss' Formula
* uses gauss' formula `(n(n + 1)) / 2` to find sum of all nums from [0-n] since theoretically every number in that range should be in the array
* subtract that "total" sum from the actual sum of the array, which will reveal which number in the range is missing in practice
​
4) Bit Manipulation
* TODO