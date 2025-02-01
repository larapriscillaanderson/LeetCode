class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # initialize left and right pointers
        left = 0
        right = len(nums) - 1

        # run a classic binary search while loop
        while left < right:
            # calculate the midpoint
            mid = left + (right - left) // 2
            # the minimum is in the right half
            if nums[mid] > nums[right]:
                # adjust the left pointer
                left = mid + 1
            else:
                # the minimum is in the left half
                # (including mid)
                right = mid
        return nums[left]
        