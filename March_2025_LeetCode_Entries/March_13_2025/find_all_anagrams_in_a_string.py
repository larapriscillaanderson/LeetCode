class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # edge case handling if length of string p > length string s
        if len(p) > len(s):
            # return empty list
            return []
        
        # create frequency maps manually
        def build_freq_map(string):
            freq_map = {}
            for char in string:
                freq_map[char] = freq_map.get(char, 0) + 1
            return freq_map

        p_count = build_freq_map(p)
        # create frequency map for first window of s
        # first (len(p)) characters
        window_count = build_freq_map(s[:len(p)])
        # initialize empty list to store starting indices of found anagrams
        result = []

        # check the first window
        if window_count == p_count:
            result.append(0)

        # start sliding the window 
        for i in range(len(p), len(s)):
            # remove character moving out
            left_char = s[i - len(p)]
            # expanding window with character moving in
            right_char = s[i]

            # update window frequency map 
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                # remove character from dictionary is count is 0
                del window_count[left_char]

            if right_char in window_count:
                window_count[right_char] += 1
            else:
                window_count[right_char] = 1

            # compare and store valid index
            if window_count == p_count:
                result.append(i - len(p) + 1)

        return result

# Testing
# s = "cbaebabacd"
# p = "abc"
# print(find_anagrams(s, p))  # Output: [0, 6]
