class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1  # Initialize the carry to 1 for the increment

        for i in range(len(digits) - 1, -1, -1):
            total = digits[i] + carry
            digits[i] = total % 10  # Update the current digit
            carry = total // 10  # Update the carry

        if carry:
            digits.insert(0, carry)  # Insert the carry if it's non-zero

        return digits
        