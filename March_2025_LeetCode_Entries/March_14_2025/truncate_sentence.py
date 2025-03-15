class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # split the sentence into words
        words = s.split()
        # extract the first k words using slicing
        sliced_words = words[:k]
        # join the words back into a sentence but with spaces
        result = ' '.join(sliced_words)
        # return the sentence
        return result

# Testing
# print(truncateSentence("Hello world this is me", 3))
# Output: "Hello world this"
# print(truncateSentence("Coding is fun", 2))
# Output: "Coding is"          
# print(truncateSentence("Python", 5))                 
# Output: "Python"  (k > number of words)
