class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # initialize three hash map sets to track seen numbers
        # each index stores a set for a row
        rows = [set() for _ in range(9)]
        # each index stores a set for a column
        cols = [set() for _ in range(9)]
        # each index stores a set for a 3 x 3 box
        boxes = [set() for _ in range(9)]

        # iterate through each cell in the 9 x 9 board
        for r in range(9):
            for c in range(9):
                num = board[r][c]

                # if the cell is empty, skip it
                if num == '.':
                    continue
                
                # use formula to determine which 3 x 3 box the cell belongs to
                box_index = (r // 3) * 3 + (c // 3)

                # check for duplicate numbers 
                # check row
                if num in rows[r]:
                    return False
                # check column
                if num in cols[c]:
                    return False
                # check 3 x 3 box
                if num in boxes[box_index]:
                    return False
                
                # add the number to its respective row, column, and 3 x 3 box
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_index].add(num)
        
        # if all cells were checked without conflicts,
        # the board is valid, and can return True
        return True
        