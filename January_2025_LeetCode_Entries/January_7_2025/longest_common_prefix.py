class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            # if the input array is empty, return an empty string
            return ""
        
        # initialize the prefix value to the first string in the array
        prefix = strs[0]
        
        # iterate through the strings in the array starting from the second one
        for current_string in strs[1:]:
            # find the length of the common prefix 
            # between prefix and the current string
            common_index = 0
            while common_index < len(prefix) and common_index < len(current_string) and prefix[common_index] == current_string[common_index]:
                common_index += 1
            
            # update the prefix to the common part
            prefix = prefix[:common_index]

            # if the prefix becomes empty, return an empty string
            if not prefix:
                return ""

        return prefix
        