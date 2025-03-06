# Pseudocode

# 1. Initialize variables:
#    - `left = 0` → Left pointer for the sliding window
#    - `current_sum = 0` → Running sum of elements inside the window
#    - `min_length = infinity` → Stores the minimum length of a valid subarray

# 2. Iterate through the array with a `right` pointer:
#    a. Expand the window by adding `nums[right]` to `current_sum`.
   
#    b. While `current_sum` is greater than or equal to `target`:
#       - Update `min_length` as `min(min_length, right - left + 1)`, since we found a valid subarray.
#       - Shrink the window from the left by subtracting `nums[left]` from `current_sum`.
#       - Move the `left` pointer forward.

# 3. Continue expanding and contracting the window until we reach the end of the array.

# 4. If `min_length` is still `infinity`, return 0 (no valid subarray found).
#    Otherwise, return `min_length` as the smallest subarray length.
