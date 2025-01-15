class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # create a new string to save the alpha numeric characters
        new_string = ""
        for character in s:
            if character.isalnum():
                # if the character is alpha numeric
                # then add it to the new_string
                new_string += character.lower()
                # but make sure to add it as a lowercase value
        return new_string == new_string[::-1]
        # check if the new string is the same as its reversal