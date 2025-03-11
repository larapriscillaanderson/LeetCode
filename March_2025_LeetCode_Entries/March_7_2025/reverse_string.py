class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # initialize left and right pointers
        # first character
        left = 0
        # last character
        right = len(s) - 1
        # loop until left pointer is less than right pointer
        while left < right:
            # swap the elements at left and right
            s[left], s[right] = s[right], s[left]
            # increment left pointer to move forward
            left += 1
            # decrement right pointer to move backwards
            right -= 1

# Testing
# s = ["h", "e", "l", "l", "o"]
# reverseString(s)
# print(s)  
# Output should be ['o', 'l', 'l', 'e', 'h']
