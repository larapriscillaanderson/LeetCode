class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # initialize a dictionary to track counts
        count_map = {}
        # create threshold limit for counting
        # the majority element must appear more than this value
        n = len(nums) // 2
        # iterate through each number using a for loop
        for num in nums:
            # if num is already in count_map, increment by 1
            # if not, then initialize its count by setting it to 0
            # then add 1
            count_map[num] = count_map.get(num, 0) + 1
            # check if num appears more than n // 2 times
            if count_map[num] > n:
                # return the element
                return num
                