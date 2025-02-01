class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        # initialize maximum words to keep a count
        max_words = 0

        for sentence in sentences:
            # split each sentence and count words
            word_count = len(sentence.split(" "))
            # update the maximum word count
            max_words = max(max_words, word_count)
        # return the maximum number of words
        return max_words 
        