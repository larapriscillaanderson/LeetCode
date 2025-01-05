class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dictionary to store counts
        count = {}  
        for num in nums:
            if num in count:
                # increment count if the number exists
                count[num] += 1  
            else:
                # initialize count if the number is new
                count[num] = 1  
        for num, freq in count.items():
            # if the frequency is found to be 1 for the desired number
            if freq == 1:
                # return the number
                return num