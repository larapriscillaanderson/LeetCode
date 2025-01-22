class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # initialize left and right pointers
        left_pointer = 0
        right_pointer = len(nums) - 1

        # run a while loop to run while left is less than right
        while left_pointer <= right_pointer:
            middle = left_pointer + (right_pointer - left_pointer) // 2
            # if the middle is equal to target, just return middle
            if nums[middle] == target:
                return middle
            # if the middle is greater than target
            # adjust the right pointer  
            # target must reside in the left side of array   
            elif nums[middle] > target:
                right_pointer = middle - 1
            # if the middle is less than target
            # adjust the left pointer
            # target must reside in the right side of the array
            else:
                left_pointer = middle + 1
        # otherwise if target is not found, return -1
        return -1

# test cases

# Instantiate the Solution class
# solution = Solution()

# Test cases
# test_case_1 = solution.search([1, 2, 3, 4, 5, 6, 7], 6)  # Expected output: 5
# test_case_2 = solution.search([-10, -5, 0, 3, 8, 12], 3)  # Expected output: 3
# test_case_3 = solution.search([2, 4, 6, 8, 10], 7)        # Expected output: -1 (7 is not in the list)
# test_case_4 = solution.search([1], 1)                     # Expected output: 0 (single element array)

# Print results
# print(f"Test Case 1 Result: {test_case_1}")
# print(f"Test Case 2 Result: {test_case_2}")
# print(f"Test Case 3 Result: {test_case_3}")
# print(f"Test Case 4 Result: {test_case_4}")
