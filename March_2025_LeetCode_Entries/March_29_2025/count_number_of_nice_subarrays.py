# pseudocode

# Function to count subarrays with exactly 'k' odd numbers
# function numberOfSubarrays(nums, k):
    # subarrays = 0  # Stores total count of valid subarrays
    # initial_gap = 0  # Stores the count of even numbers before the first odd
    # qsize = 0  # Tracks the number of odd numbers in the current window
    # start = 0  # Left pointer of the sliding window

    # Move the right pointer (end) through the array
    # for end in range(0, length of nums):
        # if nums[end] is odd:
            # qsize += 1  # Increment odd count when we encounter an odd number

        # If we have exactly 'k' odd numbers in the current window
        # if qsize == k:
            # initial_gap = 0  # Reset count of leading even numbers
            
            # Shrink the window from the left while maintaining k odd numbers
            # while qsize == k:
                # qsize -= (nums[start] is odd)  # Reduce odd count if nums[start] is odd
                # initial_gap += 1  # Count valid even numbers before the first odd
                # start += 1  # Move left pointer forward
            
        # subarrays += initial_gap  # Add the count of valid subarrays to result

    # return subarrays  # Return total count of nice subarrays
