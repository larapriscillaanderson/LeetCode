class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # create empty dictionary to store characters and their frequencies
        freq_dict = {}
        # loop through each character in the string and update the frequency
        for char in s:
            if char in freq_dict:
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1
    
        # count how many characters have an odd frequency
        odd_count = 0
        for count in freq_dict.values():
            if count % 2 != 0:
                odd_count += 1
    
        # if more than one character has an odd frequency, return False
        # else, return True (a palindrome permutation is possible)
        return odd_count <= 1
        