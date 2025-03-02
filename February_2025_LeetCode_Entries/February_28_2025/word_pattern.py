class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        # first split s string into individual words
        words = s.split()
        
        # if the lengths don't match, return False
        if len(pattern) != len(words):
            return False

        # initialize two dictionaries
        # dictionary to map characters to words
        char_to_word = {}
        # dictionary to map words to characters
        word_to_char = {}

        for char, word in zip(pattern, words):
            if char in char_to_word:
                if char_to_word[char] != word:
                    # if character maps to a different word, 
                    # return False
                    return False
            else:
                # store new mapping
                char_to_word[char] = word 
            
            if word in word_to_char:
                if word_to_char[word] != char:
                    # word maps to a different character
                    return False
                
            else:
                # store new mapping
                word_to_char[word] = char
        
        # if all checks pass, return True
        return True
        