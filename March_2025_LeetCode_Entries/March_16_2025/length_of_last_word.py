class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # split the string by spaces
        words = s.split()
        # return the length of the last word, or 0 if no words
        return len(words[-1]) if words else 0

# Testing
# print(lengthOfLastWord("Hello World"))  
# Output: 5
# print(lengthOfLastWord("   fly me   to   the moon   "))  
# Output: 4
# print(lengthOfLastWord("   "))  
# Output: 0
# print(lengthOfLastWord("word"))  
# Output: 4
# print(lengthOfLastWord(""))  
# Output: 0
