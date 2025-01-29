# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # initialize pointers
        low = 1
        high = n
        # run a classice binary search while loop
        while low <= high:
            # calculate the midpoint
            mid = low + (high - low) // 2
            # call the API guess and pass in mid
            result = guess(mid)
            if result == 0:
                # found the answer, so return mid
                return mid
            elif result == -1:
                # reposition high
                # search the left half
                high = mid - 1
            else:
                # result == 1
                # reposition low
                # search the right half
                low = mid + 1
        return low
        