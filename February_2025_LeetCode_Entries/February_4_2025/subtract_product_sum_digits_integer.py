class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        # first convert n to a list of digits
        digits = [int(digit) for digit in str(n)]
        # initialize product as 1 because there will be multiplication
        product = 1
        # initialize sum as 0 since there will be addition
        sum_digits = 0

        # iterate through each digit in the list
        for digit in digits:
            # multiply current product by the digit
            product *= digit
            # add the digit to the sum
            sum_digits += digit
        # return the difference between the product and the sum
        return product - sum_digits
        