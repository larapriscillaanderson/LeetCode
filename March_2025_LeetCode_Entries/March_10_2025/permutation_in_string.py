class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # edge case: if s1 is longer than s2, 
        # it's impossible to have a permutation of s1 in s2
        if len(s1) > len(s2):
            return False

        # initialize frequency arrays for 'a' to 'z'
        s1_freq = [0] * 26  # frequency count for s1
        window_freq = [0] * 26  # frequency count for the current window in s2

        # helper function to convert a character to an index 
        # (0 for 'a', 25 for 'z')
        def char_to_index(c):
            return ord(c) - ord('a')

        # populate the frequency array for s1
        for char in s1:
            s1_freq[char_to_index(char)] += 1

        # initialize the sliding window by adding the first len(s1) characters from s2
        window_size = len(s1)

        # populate the initial window frequency for the first `window_size` characters in s2
        for right in range(window_size):
            window_freq[char_to_index(s2[right])] += 1

        # if the initial window matches the frequency of s1, return True
        if window_freq == s1_freq:
            return True

        # start sliding the window: move the window one character at a time
        for right in range(window_size, len(s2)):
            # add the character at the 'right' pointer to the window
            window_freq[char_to_index(s2[right])] += 1

            # remove the character at the 'left' pointer from the window
            left = right - window_size
            window_freq[char_to_index(s2[left])] -= 1

            # after adjusting the window, check if the frequencies match
            if window_freq == s1_freq:
                return True

        # if no permutation is found, return False
        return False
        