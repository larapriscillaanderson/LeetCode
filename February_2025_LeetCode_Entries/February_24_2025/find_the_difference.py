class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # create a hash map to count characters in 's'
        char_count = {}

        # populate the hash map with frequencies of characters in 's'
        for char in s:
            if char in char_count:
                # increment count if letter already exists
                char_count[char] += 1
            else:
                # initialize count for new letter
                char_count[char] = 1
        
        # iterate through 't' and decrement counts
        for char in t:
            if char in char_count:
                # reduce count for each occurrence
                char_count[char] -= 1
                # if count falls into negative, return the extra character
                if char_count[char] < 0:
                    return char
            else:
                # if letter was never in 's', it's the extra one
                return char
                