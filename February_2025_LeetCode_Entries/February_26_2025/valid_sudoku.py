# pseudocode

# 1. Initialize three hash maps (sets) to track seen numbers.
#   - `rows` to track numbers in each row (a list of sets)
#   - `columns` to track numbers in each column (a list of sets)
#   - `boxes` to track numbers in each 3 x 3 sub-box (a list of sets)

# 2. Iterate through each cell (r, c) in the 9 x 9 board:
#   a. If the cell is empty ('.'), continue to the next cell.
#   b. Get the current number at board[r][c].
#   c. Determine which 3 x 3 box the cell belongs to using:
#       box_index = (r // 3) * 3 + (c // 3)

# 3. Check if the number already exists in the corresponding:
#   - `rows[r]` set: if yes, return False (duplicate in row)
#   - `cols[c]` set: if yes, return False (duplicate in column)
#   - `boxes[box_index]` set: if yes, return False (duplicate in 3 x 3 sub-box)

# 4. If the number is not a duplicate, add it to:
#   - `rows[r]`
#   - `cols[c]`
#   - `boxes[box_index]`

# 5. If all cells are processed without conflicts, return True (board is valid)
