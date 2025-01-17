class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # first check if x is negative, because negative numbers
        # cannot be palindromes
        if x < 0:
            return False

        # reverse the digits without converting the number to a string
        if str(x) == str(x)[::-1]:
            return True
        return False
        