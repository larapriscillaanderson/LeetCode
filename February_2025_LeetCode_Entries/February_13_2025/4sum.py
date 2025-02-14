# pseudocode

# 1. sort the array to handle duplicates
# 2. loop through the array with index i (first number)
# - if i is not the first element and nums[i] is the same as nums[i-1],
# skip to avoid duplicates
# 3. loop through the array with index j (second number)
# - if j is not the first after i and nums[j] is the same as nums[j-1],
# skip to avoid duplicates
# 4. use two pointers (left, right) to find two more numbers that sum to 
# (target - nums[i] - nums[j])
# - while left pointer < right pointer:
#   a. calculate sum of nums[i], nums[j], nums[left], and nums[right]
#   b. if the sum matches target, store the quadruplet in the result
#   c. move left and right pointers while skipping duplicates
#   d. if sum is too small, move left pointer to increase sum
#   e. if sum is too large, move right pointer to decrease sum
# 5. return the list of unique quadruplets