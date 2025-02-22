# pseudocode

# 1. Start with two pointers:
#    - left pointer at the beginning of the array (index 0)
#    - right pointer at the end of the array (last index)

# 2. While left pointer is less than right pointer:
#    a. Calculate the sum of numbers[left] + numbers[right]
#    b. If the sum matches the target:
#       - Return [left + 1, right + 1] (because it's 1-based indexing)
#    c. If the sum is too small (less than target):
#       - Move the left pointer to the right (increase left)
#    d. If the sum is too big (greater than target):
#       - Move the right pointer to the left (decrease right)

# 3. The loop stops when left >= right (shouldn’t happen because guaranteed a solution)

# 4. Return the answer (don’t need extra storage since just using two pointers)
