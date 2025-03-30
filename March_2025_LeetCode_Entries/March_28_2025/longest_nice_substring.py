class Solution(object):
    def helper_nice(self, s: str) -> bool:
        """Helper function to check if a given function is nice."""
        # convert the string to lowercase and create a set of unique characters
        lowercase_set = set(s.lower())
        # if the number of unique lowercase letters is equal to half the
        # number of unique characters then every character in the string 
        # has its counterpart (upper/lower) version
        return len(lowercase_set) * 2 == len(set(s))

    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        # initialize window size to be entire string length
        window_size = len(s)
        # loop over all possible window sizes, largest to smallest
        while window_size:
            # try all substrings of the current window size
            for i in range(len(s) - window_size + 1):
                # get the current substring of length 'window_size'
                substring = s[i:i + window_size]
                # check if current string is nice using helper function
                if self.helper_nice(substring):
                    # if substring is nice, return it since it is the
                    # first one found
                    return substring
            # if no substring is found, reduce window size and try again
            window_size -= 1
        # if no nice substring is found, return empty string
        return ""
        