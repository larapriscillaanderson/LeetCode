class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # intiialize an empty dictionary
        character_count = {}
        # iterate through the string using a for loop
        for char in s:
            # if the character is not in the dictionary,
            # add it with a count of 1
            character_count[char] = character_count.get(char, 0) + 1
            # otherwise, increment its count
        # iterate through the string again to find the first unique character
        for i in range(len(s)):
            # if the character's count is 1, return the index
            if character_count[s[i]] == 1:
                return i
        # if no unique character exists, return -1 
        return -1
        