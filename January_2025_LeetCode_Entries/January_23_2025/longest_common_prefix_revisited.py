class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""  # Return empty string if the list is empty
        
        # Assume the first string is the prefix
        prefix = strs[0]
        
        # Loop through each string in the array
        for current_string in strs:
            # Check each character of the prefix against the current string
            while not current_string.startswith(prefix):
                # Shorten the prefix by one character from the end
                prefix = prefix[:-1]
                
                # If prefix becomes empty, return ""
                if prefix == "":
                    return ""
        
        return prefix
