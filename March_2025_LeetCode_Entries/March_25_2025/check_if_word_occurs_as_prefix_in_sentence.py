class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        # split the sentence into words
        words = sentence.split()
        # manually track the index (1-indexed)
        index = 1
        # iterate through the words
        for word in words:
            # check if word starts with given prefix
            if word.startswith(searchWord):
                # if so return the 1-indexed position of the word
                return index
            # increment index after checking each word
            index += 1
        # if no word starts with the given prefix, return -1
        return -1


# Testing
# sentence = "i love programming"
# prefix = "pro"
# print(isPrefixOfWord(sentence, prefix))  
# Output: True
