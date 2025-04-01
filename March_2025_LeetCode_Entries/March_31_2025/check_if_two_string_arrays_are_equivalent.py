class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
         # join all elements in word1 into a single string
        str1 = "".join(word1)
        
        # join all elements in word2 into a single string
        str2 = "".join(word2)
        
        # compare the two strings and return the result
        return str1 == str2
        