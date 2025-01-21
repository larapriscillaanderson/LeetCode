class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # first check if n is negative
        # because negative numbers and zero are not powers of two
        if n <= 0:
            return False
        # use a while loop and continously divide n by 2
        # check if the remainder is zero
        while n % 2 == 0:
            # if n is a power of two
            # repeated division by 2 will eventually yield 1
            n = n // 2
        # if n is not a power of two, the division will stop
        # at a non 1 value
        return n == 1
        