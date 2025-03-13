# pseudocode

# Edge Case:
# if length of string p > length of string s:
#   - return empty list

# Step 1: Initialize frequency maps
#   - p_count = frequency_map(p)
#   - window_count = frequency_map(first len(p) characters of s)
#   - result = []

# Step 2: Check the first window
# if window_count == p_count:
#   - add index 0 to result

# Step 3: Start sliding the window
# for i from len(p) to len(s) - 1:
#   (character moving out of the window)
#   - left_char = s[i - len(p)]
#   (character coming into the window)
#   - right_char = s[i]

#   - update window frequency map
#   - decrement count of left_char in window_count
#   - remove left_char from window_count if count becomes 0 
#   - increment count of right_char in window_count

# Step 4: Compare and store valid index 
#   - if window_count == p_count:
#       - add (i - len(p) + 1) to result
# return result
