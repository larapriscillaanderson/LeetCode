class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # convert string to a list to allow for character swap
        s = list(s)
        # initialize left and right pointers
        # first character
        left = 0
        # last character
        right = len(s) - 1
        # loop until left pointer is less than right pointer
        while left < right:
            # move the left pointer until it points to a letter
            if not s[left].isalpha():
                left += 1
            # move the right pointer until it points to a letter
            elif not s[right].isalpha():
                right -= 1
            else:
                # swap the letters at left and right pointers
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        # join the list back into a string and return it
        return ''.join(s)

# Test the function
# solution = Solution()
# test_string = "ab-cd"
# result = solution.reverseOnlyLetters(test_string)
# print(result)  # Expected output: "dc-ba"

# test_string2 = "a-bC-dEf-ghIj"
# result2 = solution.reverseOnlyLetters(test_string2)
# print(result2)  # Expected output: "j-Ih-gfE-dCba"

# test_string3 = "Test1ng-Leet=code-Q!"
# result3 = solution.reverseOnlyLetters(test_string3)
# print(result3)  # Expected output: "Qedo1ct-eeLg=ntse-T!"
