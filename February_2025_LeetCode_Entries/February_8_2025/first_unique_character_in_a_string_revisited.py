class Solution(object):
    def first_uniq_char(s: str) -> int:
        # initialize an empty dictionary to store character counts
        char_count = {}

        # iterate through the string using a for loop
        for char in s:
            # if the character is not in the dictionary,
            # add it with a count of 1
            char_count[char] = char_count.get(char, 0) + 1

        # iterate through the string again to find the first unique character
        for index, char in enumerate(s):
            if char_count[char] == 1:
                return index  

        # if no unique character exists, return -1
        return -1  
