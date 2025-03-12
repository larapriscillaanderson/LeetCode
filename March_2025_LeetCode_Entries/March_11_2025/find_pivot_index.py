class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # calculate the total sum of the array
        total_sum = sum(nums)
        # initialize left sum to track the sum of elements
        # to the left of the current index 
        left_sum = 0

        # iterate through the array, checking each index as a potential pivot
        for i in range(len(nums)):
            # check if left sum is equal to right sum
            # right sum is calculated as total sum - left sum - nums[i]
            if left_sum == total_sum - left_sum - nums[i]:
                # if condition is met, return the pivot index
                return i
            # update left sum by adding the current element
            left_sum += nums[i]
        # if no pivot index is found, return -1 
        return -1 

# Testing
# print(pivotIndex([1,7,3,6,5,6]))  
# Expected output: 3
# print(pivotIndex([2,1,-1]))       
# Expected output: 0
# print(pivotIndex([1,2,3]))        
# Expected output: -1
# print(pivotIndex([0,0,0,0,1]))    
# Expected output: 4
