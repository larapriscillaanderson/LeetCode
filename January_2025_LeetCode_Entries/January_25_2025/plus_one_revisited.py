class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Start from the last digit and work backward
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0  # Set current digit to 0 and continue to the next one
        
        # If we finished the loop, all digits were 9
        return [1] + digits
        