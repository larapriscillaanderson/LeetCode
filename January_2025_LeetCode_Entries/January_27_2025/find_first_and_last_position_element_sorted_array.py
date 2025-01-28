class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Helper function to find the first occurrence of the target
        def findFirst(nums, target):
            low, high = 0, len(nums) - 1
            first = -1
            while low <= high:
                mid = low + (high - low) // 2  # Calculate mid index
                if nums[mid] == target:
                    first = mid  # Target found, update first position
                    high = mid - 1  # Move left to find earlier occurrences
                elif nums[mid] < target:
                    low = mid + 1  # Move right
                else:
                    high = mid - 1  # Move left
            return first

        # Helper function to find the last occurrence of the target
        def findLast(nums, target):
            low, high = 0, len(nums) - 1
            last = -1
            while low <= high:
                mid = low + (high - low) // 2  # Calculate mid index
                if nums[mid] == target:
                    last = mid  # Target found, update last position
                    low = mid + 1  # Move right to find later occurrences
                elif nums[mid] < target:
                    low = mid + 1  # Move right
                else:
                    high = mid - 1  # Move left
            return last

        # Find the first and last positions
        first_position = findFirst(nums, target)
        last_position = findLast(nums, target)

        # If either position is not found, return [-1, -1]
        if first_position == -1 or last_position == -1:
            return [-1, -1]
        return [first_position, last_position]
        