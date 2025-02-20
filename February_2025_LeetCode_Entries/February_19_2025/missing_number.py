class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # the array contains n numbers, 
        # meaning the range is [0, n]
        n = len(nums)
        # using integer division
        expected_sum = (n * (n + 1) // 2)
        # sum up all elements in the array
        actual_sum = sum(nums)
        # calculate the missing number
        return expected_sum - actual_sum

'''# Test case 1: Missing number is in the middle
print(missingNumber([3, 0, 1]))  # Output: 2

# Test case 2: Missing number is at the end
print(missingNumber([0, 1, 2, 3, 4, 5, 6, 7, 8]))  # Output: 9

# Test case 3: Missing number is at the beginning
print(missingNumber([1, 2, 3]))  # Output: 0

# Test case 4: Only one number, missing 0
print(missingNumber([1]))  # Output: 0

# Test case 5: Only one number, missing 1
print(missingNumber([0]))  # Output: 1'''
