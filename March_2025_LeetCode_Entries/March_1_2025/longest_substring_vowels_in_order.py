# pseudocode

# 1. Initialize variables:
#    - `start = 0` → Left pointer for the sliding window
#    - `max_length = 0` → Stores the length of the longest beautiful substring
#    - `vowel_set = set()` → Keeps track of unique vowels in the current window

# 2. Iterate through the string with an `end` pointer:
#    a. If `word[end]` is smaller than `word[end - 1]` (order is broken):
#       - Reset `start = end`
#       - Reset `vowel_set = {}`

#    b. Add `word[end]` to `vowel_set` to track encountered vowels.

#    c. If `vowel_set` contains all five vowels `{a, e, i, o, u}`:
#       - Update `max_length` as `max(max_length, end - start + 1)`

# 3. Continue expanding the window while maintaining the conditions.

# 4. Return `max_length` as the length of the longest beautiful substring.
