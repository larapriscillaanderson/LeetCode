class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # initialize count for total nice subarrays
        subarrays = 0  
        # tracks count of even numbers before first odd in the subarray
        initial_gap = 0
        # tracks number of odd numbers in the current window
        qsize = 0
        # left pointer of the sliding window  
        start = 0  

        # move the right pointer end through the array
        for end in range(len(nums)):
            # if current element is odd, increment qsize
            if nums[end] % 2 == 1:
                # odd number found so increment qsize
                qsize += 1

            # ehen we have exactly k odd numbers in our window
            if qsize == k:
                # eeset count of even numbers before the first odd
                initial_gap = 0
                
                # move start pointer forward while keeping k odd numbers
                while qsize == k:
                    # if nums[start] is odd, reduce qsize
                    qsize -= nums[start] % 2 
                    # count valid even numbers at the beginning 
                    initial_gap += 1 
                    # move left pointer forward 
                    start += 1
                
            # add the count of valid subarrays ending at end
            subarrays += initial_gap
        # return total count of nice subarrays
        return subarrays

# Testing
# solution = Solution()

# Test Case 1 (Example 1)
# nums1 = [1,1,2,1,1]
# k1 = 3
# print(solution.numberOfSubarrays(nums1, k1))  
# Expected output: 2

# Test Case 2 (Example 2)
# nums2 = [2,4,6]
# k2 = 1
# print(solution.numberOfSubarrays(nums2, k2))  
# Expected output: 0

# Test Case 3 (Example 3)
# nums3 = [2,2,2,1,2,2,1,2,2,2]
# k3 = 2
# print(solution.numberOfSubarrays(nums3, k3))  
# Expected output: 16
