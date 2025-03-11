# pseudocode

# 1. Initialize variables:
#    - `s1_count = Counter(s1)` → Character frequency count of string s1
#    - `window_count = Counter()` → Character frequency count for the sliding window in s2
#    - `left = 0` → Left pointer for the sliding window
#    - `window_size = len(s1)` → Size of the sliding window (same as the length of s1)

# 2. Iterate through string s2 using a right pointer:
#    a. Add the current character `s2[right]` to `window_count`.
#       - Increment the frequency of the character in the window count.

#    b. If the window size exceeds `window_size` (i.e., `right - left + 1 > window_size`):
#       - Shrink the window from the left by subtracting `s2[left]` from `window_count`.
#       - Move the left pointer forward (`left += 1`).

#    c. After adjusting the window, compare `window_count` with `s1_count`:
#       - If they match, return `True` because the current window is a permutation of s1.

# 3. Continue sliding the window across s2 until the end of the string.

# 4. If no valid permutation is found, return `False`.
