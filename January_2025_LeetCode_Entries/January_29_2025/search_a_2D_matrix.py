class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # initialize number of rows
        m = len(matrix)
        # initialize number of columns
        n = len(matrix[0])

        # treat matrix as a 1D array
        left = 0
        right = m * n - 1

        # run a classic binary search while loop
        while left <= right:
            # calculate middle index
            mid = (left + right) // 2
            # convert 1D index to 2D row index
            row = mid // n
            # convert 1D index to 2D column index
            col = mid % n

            # run comparisons of middle to target
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
        