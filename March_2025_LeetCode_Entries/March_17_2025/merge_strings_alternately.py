class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = []
        min_length = min(len(word1), len(word2))

        # merge characters alternatively
        for i in range(min_length):
            result.append(word1[i])
            result.append(word2[i])

        # append remaining characters from the longer word
        result.append(word1[min_length:])
        result.append(word2[min_length:])

        return "".join(result)
