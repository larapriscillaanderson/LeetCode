class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # if strings aren't the same length, they can't be isomorphic
        if len(s) != len(t):
            return False
        
        # need two dictionaries to store mappings
        s_to_t = {}
        t_to_s = {}

        # go through both strings at the same time
        for char_s, char_t in zip(s, t):
            # if seen char_s before, it must always map to the same char_t
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    # if the mapping is inconsistent, return False
                    return False  
        
            # if seen char_t before, it must always map back to the same char_s
            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    # if the mapping is inconsistent, return False
                    return False  

            # If we haven't seen this character before, we create a new mapping
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s

        # made it through the loop without returning False, 
        # the strings are isomorphic, return True
        return True  
        