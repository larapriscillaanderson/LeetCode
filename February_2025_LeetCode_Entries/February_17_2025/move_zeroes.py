class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # pointer to track position for next non zero number
        nonZeroIndex = 0

        # iterate through the array
        for i in range(len(nums)):
            # if the current element is non-zero,
            # need to move it forward
            if nums[i] != 0:
                # swap the non-zero element with the element at nonZeroIndex
                nums[nonZeroIndex], nums[i] = nums[i], nums[nonZeroIndex]
                # move the nonZeroIndex forward to track the 
                # next available position
                nonZeroIndex += 1

# Example usage:
# nums = [0, 1, 0, 3, 12]  # Input array with some zeroes
# move_zeroes(nums)  
# print(nums)  # Expected output: [1, 3, 12, 0, 0]
