class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # initialize two pointers
        # start left at the beginning of the array
        left = 0
        # start right at the end of the array
        right = len(numbers) - 1
        # loop until the two pointers meet
        while left < right:
            # calculate the sum of two numbers
            current_sum = numbers[left] + numbers[right]
            # if the sum matches the target,
            # return their 1-based indices
            if current_sum == target:
                # convert 0-based index to 1-based index
                return [left + 1, right + 1]
            # if the sum is too small, move the left pointer to the right
            elif current_sum < target:
                # increment the left pointer
                left += 1
            # if the sum is too big, move the right pointer to the left
            else:
                # decrement the right pointer
                right -= 1 
                