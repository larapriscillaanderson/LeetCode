class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # helper function to calculate the sum of squares of digits
        def sum_of_squares(num):
            # this will hold the sum of squares
            total = 0
            # loop through each digit of num
            while num > 0:
                # get the last digit of num (using modulus operator)
                digit = num % 10
                # add the square of the digit to total  
                total += digit * digit  
                # remove the last digit of num (using floor division)
                num //= 10 
            # return the sum of squares
            return total
        
        # initialize set to track numbers already encountered
        seen = set()

        # keep running the while loop until n becomes 1
        while n != 1:
            # get the sum of squares of digits of the current n
            n = sum_of_squares(n)
            # check if we've already seen this number  
            if n in seen: 
                # if number is seen, within cycle, return False
                return False 
            # add current number to the set to track it
            seen.add(n)
        # if loop ends, reached 1, return True
        return True
        