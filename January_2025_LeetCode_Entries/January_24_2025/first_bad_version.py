# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # initialize pointers
        left_pointer = 1
        right_pointer = n
    
        while left_pointer < right_pointer:  
            # create midpoint calculation
            midpoint = left_pointer + (right_pointer - left_pointer) // 2  
            if isBadVersion(midpoint):  
                # if the mid version is bad, 
                # search the left half (including mid)
                right_pointer = midpoint
            else:
                # if the mid version is good, 
                # search the right half (excluding mid)
                left_pointer = midpoint + 1
    
        # at the end, left will point to the first bad version
        return left_pointer
        