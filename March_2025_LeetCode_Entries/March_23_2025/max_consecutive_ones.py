class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # initialize variable to keep track of longest streak of 1s
        max_count = 0
        # initialize variable to count the current streak of 1s
        current_count = 0
        
        for num in nums:
            if num == 1:
                # increment the current count if a 1 is found
                current_count += 1
                # take the maximum of the two variables as a check
                max_count = max(max_count, current_count)
            else:
                # if a 0 is found, reset the current count
                current_count = 0
        # return the longest streak of 1s found
        return max_count

# Testing
# print(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))  
# Output: 3
