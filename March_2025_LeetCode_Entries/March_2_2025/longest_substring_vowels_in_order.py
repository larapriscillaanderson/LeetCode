class Solution(object):
    def longestBeautifulSubstring(self, word):
        """
        :type word: str
        :rtype: int
        """
        # initializing variables
        # left pointer for the sliding window
        start = 0
        # track the longest valid substring
        max_length = 0
        # store unique vowels in the current window 
        vowel_set = set()

        # iterate through the string with an `end` pointer
        for end in range(len(word)):
            # if the order is broken, must reset window
            if end > 0 and word[end] < word[end - 1]:
                start = end
                vowel_set.clear()
            
            # add the current vowel to the set
            vowel_set.add(word[end])

            # check if all 5 vowels are present
            if vowel_set == {'a', 'e', 'i', 'o', 'u'}:
                max_length = max(max_length, end - start + 1)
        
        # return longest valid substring length
        return max_length
        