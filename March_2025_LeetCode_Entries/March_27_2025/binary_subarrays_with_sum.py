class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        # initialize variables
        # dictionary to store prefix sum frequencies
        prefixSumCount = {0:1}
        # keep track of running sum of elements
        current_sum = 0
        # stores the number of valid subarrays
        count = 0

        # iterate through the array
        for num in nums:
            # update running sum
            current_sum += num
            # check if (current sum - goal) exists in prefixSumCount
            if (current_sum - goal) in prefixSumCount:
                # add valid subarrays to count
                count += prefixSumCount[current_sum - goal]
                # update prefixSumCount with the new current sum
            prefixSumCount[current_sum] = prefixSumCount.get(current_sum, 0) + 1
        # return final count of valid subarrays 
        return count 

# Testing
# print(numSubarraysWithSum([1,0,1,0,1], 2))  
# Output: 4
# print(numSubarraysWithSum([0,0,0,0,0], 0))  
# Output: 15
# print(numSubarraysWithSum([1,1,1,1], 2))    
# Output: 3
# print(numSubarraysWithSum([0,1,0,1,0], 1))  
# Output: 6
# print(numSubarraysWithSum([1,1,1], 3))      
# Output: 1
