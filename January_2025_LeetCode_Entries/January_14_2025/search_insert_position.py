class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # initialize pointers
        left = 0
        right = len(nums) - 1
        # create a while loop to run while the left value is less than the right
        while left <= right:
            # calculate the midpoint index
            # (right - left) = remainder of items in the list
            # // floor division to ensure no remainder
            midpoint = left + (right - left) // 2
            # if the midpoint is equal to the target, return midpoint
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] < target:
                # then target is greater
                # search to the right of the list
                # the new starting point is the element to the right
                # of the midpoint, so the new left is repositioned
                left = midpoint + 1
            else:
                # otherwise target is smaller
                # search to the left of the list
                # the new ending position is now the element
                # that is directly to the left of the midpoint
                right = midpoint - 1
        # if target not found, left points to the insertion index
        return left
        