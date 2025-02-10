class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # initialize an empty dictionary
        anagrams = {}

        for word in strs:
            # sort the word to create a key
            key = tuple(sorted(word))
            # check if key exists in dictionary
            # if not, initialize with an empty list
            if key not in anagrams:
                anagrams[key] = []
            # append the word to the corresponding anagram group
            anagrams[key].append(word)
        # return grouped anagrams
        return list(anagrams.values())
        