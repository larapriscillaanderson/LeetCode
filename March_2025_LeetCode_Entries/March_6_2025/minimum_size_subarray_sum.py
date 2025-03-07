class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # left pointer of sliding window
        left = 0
        # running sum of elements in the window
        current_sum = 0
        # store minimum length of a valid subarray
        min_length = float('inf')

        for right in range(len(nums)):
            # expand window by adding nums[right]
            current_sum += nums[right]
            # shrinking window from left while condition holds
            while current_sum >= target: 
                # update minimum length
                min_length = min(min_length, right - left + 1)
                # remove leftmost element from window
                current_sum -= nums[left]
                # move left pointer foward
                left += 1
        # return result
        return min_length if min_length != float('inf') else 0
        