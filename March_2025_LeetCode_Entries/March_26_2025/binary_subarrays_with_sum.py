# pseudocode

# 1. Initialize variables, start with {0: 1} to account for exact matches:
#    - `prefixSumCount = {0: 1}` → Dictionary to store prefix sum frequencies. 
#    - `current_sum = 0` → Running sum of elements.
#    - `count = 0` → Stores the number of valid subarrays.

# 2. Iterate through the array:
#    a. Add `nums[i]` to `current_sum` to maintain the running sum.

#    b. Check if `(current_sum - goal)` exists in `prefixSumCount`:
#       - If yes, it means there are `prefixSumCount[current_sum - goal]` subarrays that sum to `goal`.
#       - Add this count to `count`.

#    c. Store/update `prefixSumCount[current_sum]`:
#       - Increase the frequency of `current_sum` in the dictionary.

# 3. Return `count` as the final result.
