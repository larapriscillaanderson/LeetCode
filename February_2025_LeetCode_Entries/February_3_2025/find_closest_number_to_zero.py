class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # begin with the first number
        closest = nums[0]
        # iterate through the array using a for loop
        for num in nums:
        # Compare absolute values
            if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest):
                # update if closer or if equal but larger
                closest = num
        return closest
        