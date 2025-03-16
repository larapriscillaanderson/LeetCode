class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # split the string into words
        words = s.split()
        # reverse each word using slicing
        reversed_words = [word[::-1] for word in words]
        # join the reversed words back with spaces
        result = ' '.join(reversed_words)
        # return the new sentence but reversed in result
        return result

# Testing
# print(reverse_words("Let's do this"))  
# Output: "s'teL od siht"
# print(reverse_words("hello world"))    
# Output: "olleh dlrow"
# print(reverse_words("  Python  is fun "))  
# Output: "nohtyP si nuf"
# print(reverse_words(""))               
# Output: ""
