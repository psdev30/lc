**right to left pass solution**
* if we start from the back instead of the front, we don't have to do the i + 1 check every iteration to make sure we're still in bounds
* we instead compare to i + 1 (which we know will always exist) and subtract if i < i + 1 and add otherwise
* same complexity, cleaner loop (can use for instead of while)
-----------------------------------------------------------------------------------------------------
**left to right pass solution (modified)**
* if we store the special subtraction cases in the hashmap too, it's still fixed space complexity and the loop logic is slightly cleaner (eh)
* same complexity
-----------------------------------------------------------------------------------------------------
**left to right pass solution (better than yours)**
* your original solution but generalized to eliminate repeated code