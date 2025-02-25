# pseudocode

# 1. Initialize a variable `boomerangs_count` to 0 (this will hold the total count of boomerangs)

# 2. For each point `i` in the points list:
#    - Create a dictionary `distance_count` to store the frequency of distances from point `i` to other points

# 3. For each point `j` (not equal to `i`):
#    a. Calculate the squared Euclidean distance between points `i` and `j`:
#       d = (x[j] - x[i])^2 + (y[j] - y[i])^2
#    b. Increment `distance_count[d]` (count how many times this distance has appeared)

# 4. After processing all points `j` for point `i`:
#    a. For each value `m` in `distance_count` (the frequency of a particular distance):
#       - If `m >= 2`, add `m * (m - 1)` to `boomerangs_count` (because order matters in boomerangs)

# 5. Return `boomerangs_count` as the total number of boomerangs
