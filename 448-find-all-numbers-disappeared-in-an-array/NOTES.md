* tried to go down sorting path similar to the suboptimal approach in missing numbers.. didn't work
* **brute force**
* use hashmap to store all array values and the numbers in the given [1, n] range aren't in the hashmap are part of the disappeared numbers list
* **using a set here is better since we don't care about duplicate values**
​
* **Optimal solution**
* use the fact that all numbers in array are from **[1, n]**
* notice mapping... all numbers in array are in range [1, n] & array indices are [0, n -1]
* changing sign of numbers does not change the actual number itself
* negating values serves the purpose of "marking" that the index its located at is in the array
* but if we negate a number and process it in the loop later, the data is technically different..
* abs() the number to get its "true" representation.. need to do this before processing each number to get the right index ((the number - 1)th index)
* also need abs() while negating the value at the above calculated index bc it's possible a duplicate of the number was found earlier in the array and negated the value at the same index the current number is trying to
* once the array has been completely processed and "marked," go thru the array again
* this time, whenever there is a positive number (0 is out of the [1, n] range) this means the number **index + 1** (need to undo the num - 1 in the initial marking) was not in the array, so it is one of the "disappeared numbers!"