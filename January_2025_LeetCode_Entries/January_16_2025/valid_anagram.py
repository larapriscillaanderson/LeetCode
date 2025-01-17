class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # first check if the lengths of the strings are equal.
        # because anagrams would have the same number of characters.
        if len(s) != len(t):
            return False
        # initialize empty dictionary to store frequency of characters
        freq_dict = {}
        # loop through the first string s
        for char in s:
            # if the character exists in the dictionary
            if char in freq_dict:
                # increment the count by 1
                freq_dict[char] += 1
            else:
                # otherwise just initialize the count to 1
                freq_dict[char] = 1
        # loop through the second string t
        for char in t:
            # if the character does not exist in the dictionary
            # or if the frequency is zero
            if char not in freq_dict or freq_dict[char] == 0:
                return False
            # decrement the character frequency
            freq_dict[char] -= 1
        # if all conditions were met for an anagram, return True
        return True
        