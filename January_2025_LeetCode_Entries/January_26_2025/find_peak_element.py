class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # initialize pointers
        # left represents the start of the array
        left = 0
        # right represents the end of the array (given zero indexing)
        right = len(nums) - 1 
        # run a classic binary search loop
        while left < right:
            # calculate the midpoint
            mid = left + (right - left) // 2
            # if the nums[mid] is greater than the value to its right
            # then the peak lies on the left side of the array
            if nums[mid] > nums[mid + 1]:
                # set right to mid
                right = mid
            # if the nums[mid] is less than the value to its right
            # then the peak lies on the right side of the array
            elif nums[mid] < nums[mid + 1]:
                # set left = mid + 1
                left = mid + 1
        # when the loop ends, left == right, a
        # and we have found a peak index, return left
        return left
          