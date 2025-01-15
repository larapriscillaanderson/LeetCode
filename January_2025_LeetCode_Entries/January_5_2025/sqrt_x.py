class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # first check if x is non-zero
        if x <= 1:
            return x
        left, right = 1, x

        while left <= right:
            # run the binary search only while the left is less than the right value
            # continue this by using a midpoint calculation
            mid = left + (right - left) // 2

            if mid * mid == x:
                # if the midpoint squared equals the desired x value, return the midpoint
                return mid
            elif mid * mid < x:
                # if the midpoint squared is less than x,
                # the square root lies to the right of mid, then left becomes mid + 1
                left = mid + 1
            else:
                # if the midpoint squared is more than x,
                # the square root lies to the left of mid, then right becomes mid - 1
                right = mid - 1
                # right will be the largest integer whose square is less 
                # than or equal to x at the end of the loop
        return right
